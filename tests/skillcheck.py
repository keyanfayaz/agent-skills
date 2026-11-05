"""Shared helpers for the repo's checks. Standard library only."""

import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COACHING = REPO / "plugins" / "ai-coaching"
SKILL_DIR = COACHING / "skills" / "help-me-ai"

# Commands a client's machine may not have. The skill must never tell an agent to run them.
FORBIDDEN_CLIENT_COMMANDS = [
    r"\bgit (clone|init|pull|commit)\b",
    r"\bpip3? install\b",
    r"\bnpm (install|i)\b",
    r"\bnpx\b",
    r"\bbrew install\b",
    r"\bpython3? \S+\.py\b",
    r"\buvx?\s",
]


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse a leading `---` block: `key: value` lines plus one level of nested map."""
    match = re.match(r"---\n(.*?)\n---\n?", text, re.DOTALL)
    if not match:
        raise ValueError("no frontmatter")
    fields: dict = {}
    current = None
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) and current is not None:
            key, _, value = line.strip().partition(":")
            fields[current][key.strip()] = _unquote(value)
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        if value.strip():
            fields[key] = _unquote(value)
            current = None
        else:
            fields[key] = {}
            current = key
    return fields, text[match.end():]


def headings(text: str, level: int = 2) -> list[str]:
    """Heading texts at `level`, in order, ignoring fenced code blocks."""
    found, in_fence = [], False
    marker = "#" * level + " "
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        elif not in_fence and line.startswith(marker):
            found.append(line[len(marker):].strip())
    return found


def section(text: str, title: str) -> str:
    """The text under a `## title` heading, up to the next `## ` heading."""
    match = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    assert match, f"no section {title!r}"
    return match.group(1)


def own_file_mentions(text: str) -> set[str]:
    """`references/<file>.md` and `assets/<file>.md` paths in `text` that exist in the skill."""
    mentions = set(re.findall(r"\b(?:references|assets)/[A-Za-z0-9_.-]+\.md\b", text))
    return {m for m in mentions if (SKILL_DIR / m).is_file()}


def tracked_files() -> list[Path]:
    """Files git would ship: committed or new, minus anything .gitignore excludes."""
    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=REPO, capture_output=True, text=True, check=True,
    ).stdout
    return [REPO / line for line in out.splitlines() if (REPO / line).is_file()]
