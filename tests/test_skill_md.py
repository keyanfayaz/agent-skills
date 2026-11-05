import re
import unittest

from skillcheck import SKILL_DIR, headings, own_file_mentions, parse_frontmatter

BODY_HEADINGS = [
    "What this is", "Start here", "Look around", "Ask before looking", "Choose the session",
    "How to talk", "Privacy and safety", "Saving files", "Wrap up", "If something goes wrong",
]


class SkillMd(unittest.TestCase):
    def setUp(self):
        self.text = (SKILL_DIR / "SKILL.md").read_text()
        self.fields, self.body = parse_frontmatter(self.text)

    def test_name_rules(self):
        name = self.fields["name"]
        self.assertEqual(name, SKILL_DIR.name)
        self.assertEqual(name, "help-me-ai")
        self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)

    def test_description(self):
        description = self.fields["description"]
        self.assertTrue(1 <= len(description) <= 1024, len(description))
        self.assertIn("Use when", description)
        self.assertIn("/help-me-ai", description)

    def test_description_is_upload_safe(self):
        # Chat-app uploads reject "invalid characters" without naming them; stay plain.
        description = self.fields["description"]
        self.assertTrue(description.isascii(), "description must be plain ASCII")
        self.assertNotRegex(description, r"[<>]")

    def test_metadata(self):
        metadata = self.fields["metadata"]
        self.assertRegex(metadata["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(metadata["consultant"], "Keyan")

    def test_length(self):
        self.assertLess(len(self.text.splitlines()), 500)

    def test_headings(self):
        self.assertEqual(headings(self.body), BODY_HEADINGS)

    def test_every_skill_file_is_indexed(self):
        on_disk = {
            str(p.relative_to(SKILL_DIR))
            for folder in ("references", "assets")
            for p in (SKILL_DIR / folder).glob("*.md")
        }
        self.assertEqual(own_file_mentions(self.text), on_disk)


if __name__ == "__main__":
    unittest.main()
