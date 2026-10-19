import re
import unittest

from skillcheck import SKILL_DIR, headings

REFS = SKILL_DIR / "references"
TOOL_SECTIONS = ["Claude Code", "Codex", "Claude chat app"]
FIELDS = [
    "Personal instructions", "Settings", "Skills folder", "Session history",
    "Connected tools", "Usage report", "Scheduled tasks", "Install notes", "Sources",
]


def sections(text: str) -> dict[str, str]:
    """Map each `## ` heading to the text under it."""
    parts = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


class Environments(unittest.TestCase):
    def setUp(self):
        self.text = (REFS / "environments.md").read_text()

    def test_environments_sections(self):
        self.assertEqual(headings(self.text), TOOL_SECTIONS + ["Windows"])

    def test_environments_fields(self):
        body = sections(self.text)
        for tool in TOOL_SECTIONS:
            for field in FIELDS:
                self.assertIn(f"**{field}**", body[tool], f"{tool} is missing {field}")

    def test_environments_key_paths(self):
        for path in ["~/.claude/CLAUDE.md", "~/.claude/skills/", "~/.agents/skills/",
                     "~/.codex/AGENTS.md", "~/.claude/projects/", "~/.codex/sessions/"]:
            self.assertIn(path, self.text)

    def test_environments_verified_and_sourced(self):
        self.assertRegex(self.text, r"Last verified: \d{4}-\d{2}-\d{2}")
        body = sections(self.text)
        for tool in TOOL_SECTIONS:
            sources = body[tool].split("**Sources**", 1)[1]
            self.assertIn("https://", sources, f"{tool} has no source links")


if __name__ == "__main__":
    unittest.main()
