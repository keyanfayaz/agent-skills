"""Guards for problems found in the scenario dry runs (see tests/scenarios.md)."""

import re
import unittest

from skillcheck import SKILL_DIR


def section(text: str, title: str) -> str:
    match = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    assert match, f"no section {title!r}"
    return match.group(1)


SKILL_MD = (SKILL_DIR / "SKILL.md").read_text()
FIRST = (SKILL_DIR / "references" / "first-session.md").read_text()


class DryRunFixes(unittest.TestCase):
    def test_wrap_up_offers_summary_then_shows_then_saves(self):
        # Show-before-saving held in no dry run because wrap-up saved first (review problems 1, 3, 18).
        steps = re.findall(r"^\d+\. \*\*(.+?)\*\*", section(SKILL_MD, "Wrap up"), re.MULTILINE)
        self.assertEqual(steps, ["Check it works.", "Offer the consultant summary.",
                                 "Show, then save.", "Say what's next.", "How to come back."])

    def test_intake_items_ask_one_question_each(self):
        # Bundled intake items broke one-question-per-message in every first session (problem 2).
        items = re.findall(r"^\d+\. .+$", section(FIRST, "Intake"), re.MULTILINE)
        self.assertGreaterEqual(len(items), 5)
        for item in items:
            self.assertEqual(item.count("?"), 1, item)

    def test_consent_example_respects_sample_cap(self):
        # The example asked to read ~140 sessions; the reading rule caps it at 50 (problem 15).
        self.assertIn("up to 50", section(SKILL_MD, "Ask before looking"))

    def test_access_values_are_plain_words(self):
        # full | partial | conversation are internal labels the client can see in their files (problem 19).
        for name in ("profile.md", "consultant-summary.md"):
            text = (SKILL_DIR / "assets" / name).read_text()
            self.assertIn("computer | apps | chat", text, name)
            self.assertNotIn("partial", text, name)

    def test_backups_never_copy_secrets(self):
        # Backing up a settings file that holds a key would copy the key (problem 4).
        saving = section(SKILL_MD, "Saving files")
        self.assertRegex(saving, r"(?i)never back up or change a file that still contains a secret")


if __name__ == "__main__":
    unittest.main()


ENV = (SKILL_DIR / "references" / "environments.md").read_text()
RUBRIC = (SKILL_DIR / "references" / "rubric.md").read_text()
BUILD_SKILL = (SKILL_DIR / "references" / "build-skill.md").read_text()
SUMMARY = (SKILL_DIR / "assets" / "consultant-summary.md").read_text()


class DryRunFixesRound2(unittest.TestCase):
    def test_no_scripts_on_client_machines(self):
        # Round 2, B: the agent wrote and ran a Python script to read history.
        self.assertRegex(section(SKILL_MD, "Privacy and safety"), r"(?i)never write or run scripts")
        self.assertRegex(ENV, r"(?i)never write or run a script")

    def test_quick_win_starts_from_what_they_asked_for(self):
        # Round 2, B: the default quick win could override the client's own goal for today.
        self.assertIn("worth it", section(FIRST, "Quick win"))

    def test_wrap_up_shows_report_in_full(self):
        # Round 2, B and D: only an outline of the report was shown before saving.
        self.assertRegex(section(SKILL_MD, "Wrap up"), r"(?i)the session report in full")

    def test_wrap_up_shows_new_profile_in_full(self):
        self.assertRegex(section(SKILL_MD, "Wrap up"), r"(?i)a new profile in full")

    def test_chat_preferences_not_pasted_over(self):
        # Round 2, A: nothing stopped a client replacing their existing preferences.
        self.assertRegex(section(FIRST, "Quick win"), r"(?i)already has text")

    def test_one_question_rule_covers_drafts(self):
        # Round 2, C: "Does it look right, and shall I create it?"
        self.assertRegex(section(SKILL_MD, "How to talk"), r"(?i)never join two questions")

    def test_untried_changes_followed_up(self):
        self.assertRegex(section(SKILL_MD, "Choose the session"), r"(?i)not tried yet")

    def test_project_created_before_saving(self):
        self.assertRegex(section(SKILL_MD, "Saving files"), r"(?i)before the wrap-up")

    def test_plain_area_names_for_clients(self):
        self.assertIn("how well it knows you", RUBRIC)

    def test_summary_excludes_company_names(self):
        self.assertRegex(SUMMARY, r"(?i)other people's or companies' names")

    def test_skill_keeps_existing_checklist_items(self):
        self.assertRegex(section(BUILD_SKILL, "Capture the steps"), r"(?i)keep every item")

    def test_codex_and_mcp_notes(self):
        codex = ENV.split("## Codex", 1)[1].split("## Claude chat app", 1)[0]
        self.assertIn("~/help-me-ai/", codex)
        claude = ENV.split("## Claude Code", 1)[1].split("## Codex", 1)[0]
        self.assertRegex(claude, r"(?i)MCP entries can hold keys")
