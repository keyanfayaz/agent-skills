# Agent Skills

- This repository publishes engineering workflows for Codex and Claude Code.
- Apply the [coding style](plugins/engineering/skills/create-pr/references/coding-style.md) when changing code.
- Use the [Agent Skills specification](https://agentskills.io/specification) for each skill under `plugins/engineering/skills/`. Keep the plugin manifests and marketplace entries in sync.
- Before committing, run `python3 -B -m unittest discover tests`, `scripts/build-zip.sh dist`, and `python3 -B scripts/build-plugins.py dist`.
