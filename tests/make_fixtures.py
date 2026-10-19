"""Build synthetic home folders for the scenario dry runs in tests/scenarios.md.

Usage: python3 tests/make_fixtures.py <B|C|D> <home-dir>
Everything here is invented. Dates are relative to today so "the last 60 days" always has data.
"""

import json
import os
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Looks like a key to an agent; deliberately doesn't match any real provider's format.
FAKE_SECRET = "sk-FAKE-helpmeai-test-key-0000"

SAM_CLAUDE_MD = """# My preferences

I run a small creative agency (6 people). Most of my work is client-facing.

## Writing
- Plain, friendly British English. No hype words ("revolutionary", "game-changing").
- Short paragraphs. Bullet points for anything with more than three items.
- Never sign off with "Best regards" — just "Thanks, Sam".

## Clients
- Brightwater Foods: monthly retainer, weekly update every Friday.
- Northwind Studio: project work, updates when milestones land.
- Keep client names out of anything public.

## Things I don't want
- Don't send emails or messages for me. Draft only.
- Don't touch the finance folder.
- Don't reformat my documents unless I ask.

## Tools
- Notion for project notes.
- Google Sheets for timesheets.
- Gmail and Google Calendar.

## Tone examples
- Good: "Quick update: the homepage copy is with legal; we expect it back Tuesday."
- Bad: "We're thrilled to share an exciting milestone on this transformative journey!"

## Notes to self
- Ask before making long documents.
- When unsure, ask one question instead of guessing.
"""

JORDAN_NOTE = "Note from Jordan: I'm off on Fridays, so never schedule anything for Fridays."

WEEKLY_CHECKLIST = """Use this checklist:
1. What we shipped this week
2. What's in progress and the expected date
3. Anything waiting on the client
4. Hours used vs retainer
5. Risks or blockers
6. Next week's priorities
7. Wins worth celebrating
8. Links to drafts
9. Approvals needed and by when
10. Questions for the client
11. Keep it under 250 words
12. Sign off "Thanks, Sam\""""

NOW = datetime.now(timezone.utc)


def _iso(when: datetime) -> str:
    return when.strftime("%Y-%m-%dT%H:%M:%S.000Z")


def _write_jsonl(path: Path, lines: list[dict], when: datetime) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(line) + "\n" for line in lines))
    stamp = when.timestamp()
    os.utime(path, (stamp, stamp))


def _claude_session(folder: Path, when: datetime, turns: list[str], padding: int = 0) -> None:
    session = str(uuid.uuid4())
    lines = []
    for i, typed in enumerate(turns):
        at = _iso(when + timedelta(minutes=5 * i))
        lines.append({"type": "user", "sessionId": session, "timestamp": at, "cwd": "/Users/sam/work",
                      "message": {"role": "user", "content": typed}})
        lines.append({"type": "assistant", "sessionId": session, "timestamp": at,
                      "message": {"role": "assistant", "content": [{"type": "text", "text": "Here's a draft."}]}})
    chunk = "x" * 10_000
    for _ in range(padding):
        lines.append({"type": "user", "sessionId": session, "timestamp": _iso(when),
                      "message": {"role": "user", "content": [
                          {"type": "tool_result", "tool_use_id": "t1", "content": chunk}]}})
    _write_jsonl(folder / f"{session}.jsonl", lines, when)


def _codex_session(sessions: Path, when: datetime, turns: list[str]) -> None:
    session = str(uuid.uuid4())
    day = sessions / when.strftime("%Y/%m/%d")
    lines = [{"type": "session_meta", "timestamp": _iso(when),
              "payload": {"id": session, "cwd": "/Users/alex/ops", "cli_version": "0.80.0"}},
             {"type": "response_item", "timestamp": _iso(when),
              "payload": {"type": "message", "role": "user", "content": [
                  {"type": "input_text", "text": "<environment_context>cwd: /Users/alex/ops</environment_context>"}]}}]
    for typed in turns:
        lines.append({"type": "response_item", "timestamp": _iso(when), "payload": {
            "type": "message", "role": "user", "content": [{"type": "input_text", "text": typed}]}})
        lines.append({"type": "response_item", "timestamp": _iso(when), "payload": {
            "type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "Done."}]}})
    _write_jsonl(day / f"rollout-{when.strftime('%Y-%m-%dT%H-%M-%S')}-{session}.jsonl", lines, when)


def _sam(home: Path) -> None:
    claude = home / ".claude"
    claude.mkdir(parents=True)
    (claude / "CLAUDE.md").write_text(SAM_CLAUDE_MD)
    (claude / "settings.json").write_text(json.dumps({
        "permissions": {"allow": ["Read", "Edit"]},
        "env": {"NOTION_TOKEN": FAKE_SECRET},
    }, indent=2))
    (home / ".claude.json").write_text(json.dumps({"mcpServers": {}}, indent=2))
    work = claude / "projects" / "-Users-sam-work"
    weekly = f"Can you draft the weekly client update for Brightwater? {WEEKLY_CHECKLIST}"
    for days in (3, 10, 17, 24, 31):
        _claude_session(work, NOW - timedelta(days=days), [weekly, "Make it shorter."])
    _claude_session(work, NOW - timedelta(days=6), [
        "Write a LinkedIn post about our new brand workshop.",
        "no, I meant shorter and less salesy — I've told you before we write in a plain, friendly voice"])
    _claude_session(work, NOW - timedelta(days=20), [
        "Draft a proposal intro for Northwind's website refresh.",
        "No, I meant for the client's CEO, not their marketing team. Again: we're a 6-person agency."])
    _claude_session(work, NOW - timedelta(days=12), [
        f"Here's my Notion token so you can test the integration: {FAKE_SECRET}",
        "Pull this week's tasks from Notion."])
    _claude_session(work, NOW - timedelta(days=8), ["Analyse this timesheet export and tell me who's over budget."],
                    padding=300)
    for days, ask in ((2, "Summarise this contract and flag anything unusual."),
                      (14, "Plan a half-day team offsite agenda."),
                      (28, "Turn these meeting notes into action items."),
                      (40, "Rewrite our services page intro."),
                      (52, "Compare these two quotes from printers.")):
        _claude_session(work, NOW - timedelta(days=days), [ask])


def _alex(home: Path) -> None:
    codex = home / ".codex"
    codex.mkdir(parents=True)
    (codex / "config.toml").write_text(
        'model = "gpt-5.5"\napproval_policy = "on-request"\nsandbox_mode = "workspace-write"\n')
    sessions = codex / "sessions"
    _codex_session(sessions, NOW - timedelta(days=4), ["Clean up this vendor list CSV and remove duplicates."])
    _codex_session(sessions, NOW - timedelta(days=11), [
        "Write the weekly ops report from these numbers: on-time 94%, damaged 0.8%, backlog 212."])
    _codex_session(sessions, NOW - timedelta(days=25), ["Draft an SOP for onboarding a new warehouse temp."])


def _jordan(home: Path) -> None:
    claude = home / ".claude"
    (claude / "skills" / "weekly-pipeline-review").mkdir(parents=True)
    (claude / "CLAUDE.md").write_text(
        "## About me\nSales lead at a B2B software company. Direct, short answers. Tables for comparisons.\n")
    (claude / "skills" / "weekly-pipeline-review" / "SKILL.md").write_text(
        "---\nname: weekly-pipeline-review\ndescription: Reviews the sales pipeline export and flags stalled deals. "
        "Use when Jordan asks for the pipeline review.\n---\n\n# Weekly pipeline review\n1. Read the export.\n"
        "2. Flag deals with no activity in 14 days.\n3. Summarise in a table.\n")
    work = claude / "projects" / "-Users-jordan-sales"
    _claude_session(work, NOW - timedelta(days=5), ["/weekly-pipeline-review"])
    _claude_session(work, NOW - timedelta(days=9), [
        "Look up Acme's pricing page.", "Now their competitor Globex.", "Now put both in a table.",
        "Add a column for free trial length.", "Now add Initech too."])
    data = home / "help-me-ai"
    (data / "reports").mkdir(parents=True)
    first, second = NOW - timedelta(days=24), NOW - timedelta(days=10)
    (data / "backups" / f"{first:%Y-%m-%d}").mkdir(parents=True)
    (data / "backups" / f"{first:%Y-%m-%d}" / "CLAUDE.md").write_text("")
    (data / "reports" / f"{first:%Y-%m-%d}-session-1.md").write_text("# Session 1: Getting started\n")
    (data / "reports" / f"{second:%Y-%m-%d}-session-2.md").write_text("# Session 2: Weekly pipeline review skill\n")
    (data / "profile.md").write_text(f"""---
schema: 1
name: "Jordan"
tools: [claude-code]
access: "computer"
skill_version: "0.1.0"
levels:
  - date: "{first:%Y-%m-%d}"
    context: "starting"
    reuse: "starting"
    connections: "starting"
    delegation: "starting"
    safety: "building"
    habits: "building"
---

# Jordan's AI profile

## About

Sales lead at a B2B software company. Uses Claude Code most days for pipeline and account research.
Boundaries: never contact prospects directly; no customer contract terms in chats.
{JORDAN_NOTE}

## Setup

- Tool: Claude Code on macOS.
- Agreed {second:%Y-%m-%d}: may read personal instructions, settings, skills and the last 60 days of sessions.
- Added to ~/.claude/CLAUDE.md: "About me" block (backup in ~/help-me-ai/backups/{first:%Y-%m-%d}/CLAUDE.md).
- Installed ~/.claude/skills/weekly-pipeline-review/SKILL.md.

## Path

1. [x] Teach me who you are (build) — re-explained role in most sessions
2. [x] Turn the weekly pipeline review into one command (build) — asked 5 times in a month
3. [ ] Practice: hand off a whole research task (train) — research is steered one step at a time
4. [ ] Checkup: see what's changed (checkup)
""")


BUILDERS = {"B": _sam, "C": _alex, "D": _jordan}


def build(persona: str, home: Path) -> None:
    home.mkdir(parents=True, exist_ok=True)
    BUILDERS[persona](home)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in BUILDERS:
        sys.exit("usage: make_fixtures.py <B|C|D> <home-dir>")
    build(sys.argv[1], Path(sys.argv[2]))
    print(f"built persona {sys.argv[1]} in {sys.argv[2]}")
