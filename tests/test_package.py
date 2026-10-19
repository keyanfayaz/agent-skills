import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

from skillcheck import REPO, SKILL_DIR

BUILD = REPO / "scripts" / "build-zip.sh"


def build(out_dir: Path) -> Path:
    subprocess.run([str(BUILD), str(out_dir)], cwd=REPO, check=True, capture_output=True)
    return out_dir / "help-me-ai.zip"


class Package(unittest.TestCase):
    def test_zip_layout(self):
        with tempfile.TemporaryDirectory() as tmp:
            names = zipfile.ZipFile(build(Path(tmp))).namelist()
        files = {n for n in names if not n.endswith("/")}
        self.assertTrue(all(n.startswith("help-me-ai/") for n in names), names)
        self.assertIn("help-me-ai/SKILL.md", files)
        self.assertFalse([n for n in names if n.endswith(".DS_Store")])
        on_disk = {
            "help-me-ai/" + str(p.relative_to(SKILL_DIR))
            for p in SKILL_DIR.rglob("*") if p.is_file() and p.name != ".DS_Store"
        }
        self.assertEqual(files, on_disk)

    def test_zip_extracts_with_tar(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = build(Path(tmp))
            dest = Path(tmp) / "out"
            dest.mkdir()
            subprocess.run(["tar", "-xf", str(archive), "-C", str(dest)], check=True)
            self.assertTrue((dest / "help-me-ai" / "SKILL.md").is_file())

    def test_release_workflow(self):
        text = (REPO / ".github" / "workflows" / "release.yml").read_text()
        for needle in ["types: [published]", "scripts/build-zip.sh", "help-me-ai.zip", "contents: write"]:
            self.assertIn(needle, text)


if __name__ == "__main__":
    unittest.main()
