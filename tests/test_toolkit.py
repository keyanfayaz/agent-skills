"""Check that both hosts install the same plugin and its archives are portable."""

import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from zipfile import ZipFile


REPO = Path(__file__).resolve().parents[1]


class Toolkit(unittest.TestCase):
    def test_marketplaces_resolve_to_matching_plugin_manifests(self):
        codex = json.loads((REPO / ".agents/plugins/marketplace.json").read_text())
        claude = json.loads((REPO / ".claude-plugin/marketplace.json").read_text())
        claude_plugins = {entry["name"]: entry for entry in claude["plugins"]}
        self.assertEqual(codex["name"], claude["name"])
        self.assertEqual({entry["name"] for entry in codex["plugins"]}, claude_plugins.keys())

        for entry in codex["plugins"]:
            with self.subTest(plugin=entry["name"]):
                claude_entry = claude_plugins[entry["name"]]
                plugin_path = entry["source"]["path"]
                self.assertEqual(plugin_path, claude_entry["source"])
                plugin = REPO / plugin_path
                portable = json.loads((plugin / "plugin.json").read_text())
                codex_manifest = json.loads((plugin / ".codex-plugin/plugin.json").read_text())
                claude_manifest = json.loads((plugin / ".claude-plugin/plugin.json").read_text())
                self.assertEqual(portable["name"], plugin.name)
                for manifest in (codex_manifest, claude_manifest, claude_entry):
                    for key in ("name", "version", "description"):
                        self.assertEqual(manifest[key], portable[key], key)
                self.assertEqual(
                    codex_manifest["interface"], portable["extensions"]["com.openai"]["interface"]
                )
                self.assertEqual((plugin / codex_manifest["skills"]).resolve(), plugin / "skills")
                self.assertTrue(list((plugin / "skills").glob("*/SKILL.md")))

    def test_archives_ship_all_skills_and_project_guidance(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([str(REPO / "scripts/build-zip.sh"), tmp], check=True, capture_output=True)
            subprocess.run(
                ["python3", "-B", str(REPO / "scripts/build-plugins.py"), tmp],
                check=True,
                capture_output=True,
            )
            with ZipFile(Path(tmp) / "engineering.zip") as packaged:
                packaged.extractall(Path(tmp) / "packaged")

            plugin = Path(tmp) / "packaged/engineering"
            for manifest in ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
                self.assertTrue((plugin / manifest).is_file(), manifest)
            for name in ("create-pr", "review-change", "verify-app"):
                with self.subTest(skill=name), ZipFile(Path(tmp) / (name + ".zip")) as standalone:
                    standalone.extractall(Path(tmp) / "standalone")
                    skill = Path(tmp) / "standalone" / name
                    markdown = (skill / "SKILL.md").read_text()
                    self.assertRegex(markdown, rf"\A---\nname: {name}\ndescription: [^\n]+\n---\n")
                    for path in skill.rglob("*.md"):
                        relocated = plugin / "skills" / name / path.relative_to(skill)
                        self.assertEqual(path.read_bytes(), relocated.read_bytes())
                    self.check_links(skill)

            for reference in ("coding-style.md", "setup-preferences.md"):
                self.assertTrue((plugin / "skills/create-pr/references" / reference).is_file())
            for resource in ("templates/AGENTS.md", "docs/setup.md", "docs/preferences.md", "docs/pending.md"):
                self.assertTrue((plugin / resource).is_file(), resource)
            self.check_links(plugin)

    def check_links(self, root):
        for path in root.rglob("*.md"):
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if not link.startswith(("https://", "http://", "#")):
                    target = (path.parent / link).resolve()
                    self.assertIn(root.resolve(), target.parents)
                    self.assertTrue(target.is_file(), target)
