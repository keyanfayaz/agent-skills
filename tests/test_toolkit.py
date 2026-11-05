"""Check install boundaries, profile resolution, and archive compatibility."""

import importlib.util
import json
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from zipfile import ZipFile

from skillcheck import REPO, SKILL_DIR, parse_frontmatter


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SETUP = REPO / "plugins/engineering/skills/setup-preferences"
profiles = load_module("profiles", SETUP / "scripts/resolve_profile.py")
packages = load_module("packages", REPO / "scripts/build-plugins.py")


class Profiles(unittest.TestCase):
    def test_partial_layers_preserve_defaults_and_project_overrides_personal(self):
        personal = {"schema_version": 1, "writing": {"format": "bullets", "detail": "brief"}}
        project = {"schema_version": 1, "writing": {"detail": "thorough"}}
        explicit = {"schema_version": 1, "writing": {"format": "prose"}}
        result = profiles.resolve(personal, project, explicit)
        self.assertEqual(result["writing"], {"format": "prose", "detail": "thorough", "sentences_per_bullet": 2})
        self.assertTrue(result["engineering"]["subtract_before_add"])
        self.assertEqual(personal["writing"]["format"], "bullets")

    def test_arrays_replace_and_false_is_preserved(self):
        result = profiles.resolve(
            {"schema_version": 1, "engineering": {"constraint_markers": ["KEEP", "IMPORTANT"]}},
            {"schema_version": 1, "engineering": {"constraint_markers": [], "subtract_before_add": False}},
        )
        self.assertEqual(result["engineering"], {"constraint_markers": [], "subtract_before_add": False})

    def test_invalid_configuration_is_rejected(self):
        invalid = [{}, {"schema_version": 2}, {"schema_version": True},
                   {"schema_version": 1, "writing": {"detail": "invented"}},
                   {"schema_version": 1, "writing": {"sentences_per_bullet": 0}},
                   {"schema_version": 1, "writing": {"sentences_per_bullet": True}},
                   {"schema_version": 1, "engineering": {"subtract_before_add": "false"}},
                   {"schema_version": 1, "engineering": {"constraint_markers": [1]}},
                   {"schema_version": 1, "command": "unexpected"}]
        for layer in invalid:
            with self.subTest(layer=layer), self.assertRaises(ValueError):
                profiles.resolve(layer)

    def test_example_and_cli_resolve_without_writing(self):
        example = json.loads((REPO / "examples/profile.json").read_text())
        self.assertEqual(example, json.loads((SETUP / "assets/profile.example.json").read_text()))
        result = subprocess.run(["python3", "-B", str(SETUP / "scripts/resolve_profile.py"),
                                 "--profile", str(REPO / "examples/profile.json")],
                                capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(result.stdout), profiles.resolve(example))


class Toolkit(unittest.TestCase):
    def test_catalogs_install_the_same_self_contained_plugins(self):
        codex = json.loads((REPO / ".agents/plugins/marketplace.json").read_text())
        claude = json.loads((REPO / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual({p["name"] for p in codex["plugins"]}, {p["name"] for p in claude["plugins"]})
        for entry in codex["plugins"]:
            plugin = REPO / entry["source"]["path"]
            manifests = [json.loads(path.read_text()) for path in (
                plugin / "plugin.json", plugin / ".codex-plugin/plugin.json", plugin / ".claude-plugin/plugin.json")]
            for key in ("name", "version", "description"):
                self.assertEqual(len({m[key] for m in manifests}), 1)
            self.assertTrue(list((plugin / "skills").glob("*/SKILL.md")))
            for skill in (plugin / "skills").glob("*/SKILL.md"):
                fields, _ = parse_frontmatter(skill.read_text())
                self.assertEqual(fields["name"], skill.parent.name)
                self.assertLessEqual(len(fields["description"]), 200)
                for link in re.findall(r"\]\(([^)]+)\)", skill.read_text()):
                    if not link.startswith(("https://", "http://", "#")):
                        target = (skill.parent / link).resolve()
                        self.assertIn(plugin.resolve(), target.parents)
                        self.assertTrue(target.is_file(), target)

    def test_relocated_packages_resolve_preferences_and_keep_coaching_intact(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            archives = packages.build(output)
            self.assertEqual(len(archives), 3)
            for archive in archives:
                with ZipFile(archive) as package:
                    package.extractall(output / "unpacked")
            relocated = output / "unpacked/engineering/skills/setup-preferences"
            result = subprocess.run(["python3", "-B", str(relocated / "scripts/resolve_profile.py"),
                                     "--profile", str(relocated / "assets/profile.example.json")],
                                    capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout)["writing"]["detail"], "brief")
            moved = output / "unpacked/ai-coaching/skills/help-me-ai"
            for path in SKILL_DIR.rglob("*"):
                if path.is_file():
                    self.assertEqual(path.read_bytes(), (moved / path.relative_to(SKILL_DIR)).read_bytes())

    def test_packaging_rejects_output_inside_a_plugin(self):
        with self.assertRaises(ValueError):
            packages.build(REPO / "plugins/engineering/output")


if __name__ == "__main__":
    unittest.main()
