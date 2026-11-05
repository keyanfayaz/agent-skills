"""Guards for findings from the final review of the first build."""

import json
import re
import tempfile
import unittest
from pathlib import Path

from make_fixtures import build
from skillcheck import COACHING, REPO, SKILL_DIR, parse_frontmatter, section


SKILL_MD = (SKILL_DIR / "SKILL.md").read_text()
FIRST = (SKILL_DIR / "references" / "first-session.md").read_text()
ENV = (SKILL_DIR / "references" / "environments.md").read_text()
SETUP = (SKILL_DIR / "references" / "build-setup.md").read_text()
BUILD_SKILL = (SKILL_DIR / "references" / "build-skill.md").read_text()
README = (COACHING / "README.md").read_text()


class ReviewFixes(unittest.TestCase):
    def test_talk_only_client_is_asked_before_opening_instructions(self):
        self.assertRegex(section(FIRST, "Quick win"), r"(?i)ask before opening")

    def test_saved_files_never_overwritten(self):
        saving = section(SKILL_MD, "Saving files")
        self.assertRegex(saving, r"(?i)if the name is taken")

    def test_removal_never_restores_stale_backups(self):
        wrong = section(SKILL_MD, "If something goes wrong")
        self.assertRegex(wrong, r"(?i)remove only what you added")
        self.assertRegex(wrong, r"(?i)only if the file hasn't changed since")

    def test_history_rules_match_real_files(self):
        self.assertIn('"role":"user","content":"', ENV)
        for marker in ["isSidechain", "isCompactSummary", "subagents"]:
            self.assertIn(marker, ENV)

    def test_sample_spreads_across_weeks(self):
        self.assertRegex(ENV, r"(?i)spread the sample across")

    def test_privacy_promise_is_accurate(self):
        for text in (SKILL_MD, README):
            self.assertNotRegex(text, r"(?i)nothing leaves (your|the) computer|keeps everything on your computer")
        self.assertRegex(SKILL_MD, r"(?i)nothing goes anywhere except")

    def test_description_fits_chat_app_limit(self):
        fields, _ = parse_frontmatter(SKILL_MD)
        self.assertLessEqual(len(fields["description"]), 200)
        self.assertRegex(section(BUILD_SKILL, "Write the SKILL.md"), r"at most 200 characters")

    def test_setup_never_trims_existing_instructions(self):
        self.assertNotIn("a page at most", SETUP)
        self.assertRegex(section(SETUP, "Instructions file"), r"(?i)don't trim")

    def test_every_skill_build_reads_the_skill_guide(self):
        self.assertRegex(section(SKILL_MD, "Choose the session"), r"(?i)whenever you build a skill")

    def test_exposed_keys_are_replaced(self):
        self.assertRegex(section(SKILL_MD, "Privacy and safety"), r"(?i)replace the key")

    def test_reload_skills_repeats(self):
        self.assertRegex(ENV, r"(?i)again after each change")

    def test_install_prompt_windows_and_unzipped_downloads(self):
        self.assertIn("curl.exe", README)
        self.assertRegex(README, r"(?i)already unzipped")


BUILD_SKILL_TEXT = BUILD_SKILL


class CorrectnessReview(unittest.TestCase):
    def test_quick_win_never_moves_keys_itself(self):
        quick_win = section(FIRST, "Quick win")
        self.assertNotIn("moving an exposed key", quick_win)
        self.assertRegex(quick_win, r"(?i)replace an exposed key")

    def test_not_tried_yet_is_kept_in_the_profile(self):
        # Chat-app reports live outside the Project; only the profile comes back next session.
        self.assertRegex(section(SKILL_MD, "Wrap up"), r'(?i)"not tried yet" in the report and in the profile')
        self.assertRegex(section(SKILL_MD, "Choose the session"), r'(?i)profile.{0,40}"not tried yet"')

    def test_skill_interview_asks_one_thing_per_question(self):
        items = re.findall(r"^\d+\. .+$", section(BUILD_SKILL_TEXT, "Capture the steps"), re.MULTILINE)
        self.assertGreaterEqual(len(items), 5)
        for item in items:
            self.assertNotRegex(item, r", and (what|who|where|how)\b", item)

    def test_environments_read_before_counting(self):
        look = section(SKILL_MD, "Look around")
        self.assertLess(look.index("references/environments.md"), look.index("**Which tool you're in:**"))

    def test_backup_names_say_where_they_came_from(self):
        self.assertRegex(section(SKILL_MD, "Saving files"), r"(?i)folder it came from")

    def test_project_folder_naming(self):
        self.assertRegex(ENV, r"(?i)every character other than letters and digits")


class FixtureMatchesRealFiles(unittest.TestCase):
    def test_claude_history_is_compact_and_has_side_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            build("B", Path(tmp))
            projects = Path(tmp) / ".claude" / "projects"
            top = sorted(projects.glob("*/*.jsonl"))
            self.assertTrue(top)
            self.assertIn('"type":"user"', top[0].read_text().splitlines()[0])
            side = list(projects.glob("*/*/subagents/*.jsonl"))
            self.assertTrue(side, "no subagent transcript in the fixture")
            self.assertTrue(json.loads(side[0].read_text().splitlines()[0])["isSidechain"])
            self.assertTrue(any('"isCompactSummary":true' in p.read_text() for p in top))


if __name__ == "__main__":
    unittest.main()
