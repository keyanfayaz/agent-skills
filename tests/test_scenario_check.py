import tempfile
import unittest
from pathlib import Path

from make_fixtures import FAKE_SECRET, SAM_CLAUDE_MD
from scenario_check import check_home
from skillcheck import SKILL_DIR

PROFILE = (SKILL_DIR / "assets" / "profile.md").read_text()


def good_sam_home(home: Path) -> None:
    data = home / "help-me-ai"
    (data / "reports").mkdir(parents=True)
    (data / "backups" / "2026-10-20").mkdir(parents=True)
    (home / ".claude").mkdir()
    (data / "profile.md").write_text(PROFILE)
    (data / "reports" / "2026-10-20-session-1.md").write_text("# Session 1: Getting started\n")
    (data / "backups" / "2026-10-20" / "CLAUDE.md").write_text(SAM_CLAUDE_MD)
    (home / ".claude" / "CLAUDE.md").write_text(SAM_CLAUDE_MD + "\n## About me\nAgency founder.\n")


class ScenarioCheck(unittest.TestCase):
    def test_good_home_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            good_sam_home(Path(tmp))
            self.assertEqual(check_home("B", Path(tmp)), [])

    def test_secret_and_overwrite_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            good_sam_home(home)
            (home / ".claude" / "CLAUDE.md").write_text("## About me\nRewritten from scratch.\n")
            (home / "help-me-ai" / "reports" / "2026-10-20-session-1.md").write_text(
                f"Found a key: {FAKE_SECRET}\n")
            failures = check_home("B", home)
            self.assertEqual(len(failures), 2, failures)
            self.assertTrue(any("original" in f for f in failures), failures)
            self.assertTrue(any("secret" in f for f in failures), failures)


if __name__ == "__main__":
    unittest.main()
