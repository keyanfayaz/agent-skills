import re
import unittest

from skillcheck import SKILL_DIR, headings

AREAS = ["Context", "Reuse", "Connections", "Delegation", "Safety", "Habits"]
AREA_KEYS = [a.lower() for a in AREAS]


def read(rel: str) -> str:
    return (SKILL_DIR / rel).read_text()


def frontmatter_text(text: str) -> str:
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "no frontmatter"
    return match.group(1)


class Rubric(unittest.TestCase):
    def test_rubric_areas_in_order(self):
        self.assertEqual(headings(read("references/rubric.md")), AREAS)

    def test_rubric_levels_per_area(self):
        parts = re.split(r"^## .+$", read("references/rubric.md"), flags=re.MULTILINE)[1:]
        self.assertEqual(len(parts), len(AREAS))
        for area, body in zip(AREAS, parts):
            for label in ["Starting", "Building", "Strong", "Evidence", "Ask"]:
                self.assertIn(f"**{label}**", body, f"{area} is missing {label}")


class Templates(unittest.TestCase):
    def test_profile_template(self):
        text = read("assets/profile.md")
        front = frontmatter_text(text)
        for key in ["schema: 1", "name:", "tools:", "access:", "skill_version:", "levels:", "date:"]:
            self.assertIn(key, front)
        for key in AREA_KEYS:
            self.assertRegex(front, rf"\b{key}:")
        self.assertIn("# {{name}}'s AI profile", text)
        self.assertEqual(headings(text), ["About", "Setup", "Path", "Log"])

    def test_report_template(self):
        text = read("assets/report.md")
        self.assertIn("# Session {{n}}: {{title}} ({{date}})", text)
        self.assertIn("help-me-ai {{version}}", text)
        self.assertEqual(headings(text), ["What we did", "What changed", "What you learned", "What's next"])

    def test_consultant_summary_template(self):
        text = read("assets/consultant-summary.md")
        front = frontmatter_text(text)
        for key in ["schema: 1", "date:", "client:", "tools:", "access:", "skill_version:",
                    "levels_before:", "levels_after:"]:
            self.assertIn(key, front)
        for key in AREA_KEYS:
            self.assertEqual(len(re.findall(rf"\b{key}:", front)), 2, f"{key} needs before and after")
        self.assertIn("# Summary for {{consultant}}", text)
        self.assertEqual(headings(text), ["Snapshot", "What we built", "Path progress",
                                          "Questions or blockers", "Anything else for {{consultant}}"])
        self.assertIn("<!--", text)


if __name__ == "__main__":
    unittest.main()
