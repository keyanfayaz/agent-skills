import re
import unittest

from skillcheck import (
    FORBIDDEN_CLIENT_COMMANDS,
    SKILL_DIR,
    parse_frontmatter,
    tracked_files,
)


class FrontmatterParsing(unittest.TestCase):
    def test_parse_frontmatter_nested(self):
        fields, body = parse_frontmatter(
            '---\nname: x\nmetadata:\n  version: "0.1.0"\n---\nbody'
        )
        self.assertEqual(fields, {"name": "x", "metadata": {"version": "0.1.0"}})
        self.assertEqual(body, "body")

    def test_parse_frontmatter_missing_raises(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("no frontmatter")


class RepoRules(unittest.TestCase):
    def test_no_local_tooling_state_is_shipped(self):
        forbidden = {".plans", "node_modules", "__pycache__", ".DS_Store"}
        offenders = [str(p) for p in tracked_files() if forbidden.intersection(p.parts)]
        self.assertEqual(offenders, [])

    def test_client_files_have_no_dependency_commands(self):
        hits = []
        for path in SKILL_DIR.rglob("*") if SKILL_DIR.exists() else []:
            if not path.is_file():
                continue
            text = path.read_text(errors="ignore")
            for pattern in FORBIDDEN_CLIENT_COMMANDS:
                for match in re.finditer(pattern, text):
                    hits.append(f"{path.name}: {match.group(0)!r}")
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
