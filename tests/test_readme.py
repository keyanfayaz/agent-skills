import re
import unittest

from skillcheck import REPO, headings

DOWNLOAD_URL = "https://github.com/keyanfayaz/agent-skills/releases/latest/download/help-me-ai.zip"


class Readme(unittest.TestCase):
    def setUp(self):
        self.text = (REPO / "README.md").read_text()
        self.client_part = self.text.split("## For maintainers", 1)[0]

    def test_install_prompt_present(self):
        self.assertIn('Please install the "help-me-ai" skill for me, then start it.', self.text)
        self.assertIn(DOWNLOAD_URL, self.text)
        self.assertIn("~/.claude/skills/", self.text)
        self.assertIn("~/.agents/skills/", self.text)

    def test_no_git_in_client_install(self):
        self.assertNotRegex(self.client_part, r"\bgit (clone|pull)\b")

    def test_technical_install(self):
        self.assertIn("npx skills add keyanfayaz/agent-skills --skill help-me-ai -g", self.text)

    def test_headings(self):
        self.assertEqual(headings(self.text), [
            "What this is", "Install", "Start", "What it will and won't do",
            "Update or remove", "For maintainers",
        ])
        self.assertEqual(headings(self.text, level=3), [
            "Claude Code or Codex", "Claude app (claude.ai)", "For technical users",
        ])


if __name__ == "__main__":
    unittest.main()
