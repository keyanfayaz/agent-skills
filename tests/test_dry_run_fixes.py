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
