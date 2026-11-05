# Agent Skills

- This repository publishes self-contained plugins for Claude Code and Codex.
- Keep reusable workflows in `plugins/<plugin>/skills/<skill>/`; keep personal profiles and client state outside the repository.
- Use standard Agent Skills frontmatter and short, task-specific instructions; keep platform manifests thin and consistent.
- Keep every plugin usable without installing another toolkit; optional recommendations belong in references.
- Coaching-specific rules live in `plugins/ai-coaching/AGENTS.md`; preserve its standalone ZIP and published release tags.
- Before committing, run `python3 -B -m unittest discover tests`, then build the standalone skill and plugin archives.
- Change plugin versions independently; existing `v*` releases remain reserved for Help Me AI.
