# Agent Skills

- This repository publishes engineering workflows for Codex and Claude Code.
- Apply the [coding style](plugins/engineering/skills/create-pr/references/coding-style.md) when changing code.
- Use the [Agent Skills specification](https://agentskills.io/specification) for each skill under `plugins/engineering/skills/`. Keep the plugin manifests and marketplace entries in sync.
- Before committing, run `python3 -B -m unittest discover tests`, `scripts/build-zip.sh dist`, and `python3 -B scripts/build-plugins.py dist`.
- Read the [working conventions](plugins/engineering/docs/preferences.md) before changing shared guidance. Record unresolved choices in [open decisions](plugins/engineering/docs/pending.md). Project-specific facts and commands belong in the target project's instructions.
- Use [review-change](plugins/engineering/skills/review-change/SKILL.md) for requested reviews and [verify-app](plugins/engineering/skills/verify-app/SKILL.md) for application verification. For this plugin, check skill frontmatter, relative links, examples, code fences, and the resulting archives.
- Keep commits focused, with a short subject. Limit an optional body to 4–5 bullets of 1–2 sentences. For this repo, write PR descriptions under a single `# Summary` heading with at most 7–8 bullets. Include the delivered work, actual checks, and any material gaps.
