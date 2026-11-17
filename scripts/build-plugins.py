#!/usr/bin/env python3
"""Build one self-contained ZIP per plugin, preserving platform manifests."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def build(output, root=Path(__file__).resolve().parents[1]):
    """Package regular plugin files; reject symlinks and nested output paths."""
    output = Path(output).resolve()
    plugins = root / "plugins"
    if plugins.resolve() in (output, *output.parents):
        raise ValueError("Output must be outside plugins")
    output.mkdir(parents=True, exist_ok=True)
    archives = []
    for plugin in sorted(plugins.iterdir()):
        if not (plugin / "plugin.json").is_file():
            continue
        archive = output / (plugin.name + ".zip")
        with ZipFile(archive, "w", ZIP_DEFLATED) as package:
            for path in sorted(plugin.rglob("*")):
                if path.is_symlink():
                    raise ValueError("Plugin symlinks are unsupported")
                if path.is_file() and path.name != ".DS_Store" and "__pycache__" not in path.parts:
                    package.write(path, plugin.name + "/" + str(path.relative_to(plugin)))
        archives.append(archive)
    return archives


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    for archive in build(parser.parse_args().output):
        print(archive)
