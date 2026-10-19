# AGENTS.md

This repo publishes Agent Skills that a consultant (Keyan) shares with clients. Clients install a skill into their own Claude Code, Codex or Claude chat app, and their agent coaches them to get more out of AI. The first and main skill is `help-me-ai`.

The reasoning behind every design choice is in [docs/design.md](docs/design.md). Read it before changing how the skill behaves, and update it when a decision changes.

## Layout

```
README.md                  client-facing: what it is, how to install and start
AGENTS.md                  this file
docs/design.md             design spec and decisions
skills/help-me-ai/
  SKILL.md                 front door: shared rules + which file to load for each session
  references/*.md          one focused guide per session type, plus rubric and per-tool facts
  assets/*.md              templates for the client's profile, reports and consultant summary
scripts/build-zip.sh       builds help-me-ai.zip for releases
.github/workflows/         release workflow: a version tag creates the release with the zip
tests/                     standard-library checks, scenario fixtures and checklists
```

## Rules

- **Agent Skills format** (agentskills.io): `name` is 1–64 characters, lowercase letters, digits and single hyphens, and matches the folder; `description` is 1–1024 characters and says what the skill does and when to use it; `SKILL.md` stays under 500 lines; reference files are one level deep. Only `SKILL.md` points to other files.
- **No dependencies on client machines.** Nothing under `skills/` may tell an agent to run git, Node/npx, Python, pip, brew or uv. Shell use is limited to `curl`, `tar`, `unzip`, PowerShell and basic file commands. Git is for maintaining this repo only.
- **Client-facing language** is plain and jargon-free. The skill never shows the client its own file names, or the words "mode", "rubric" or "access level".
- **Keep the repo client-readable.** Anything committed may be read by a client. Don't commit tool-specific working folders or notes; working files go in the gitignored `.plans/` folder.
- **Fixed names:** skill `help-me-ai`; client data folder `~/help-me-ai/`; repo `keyanfayaz/agent-skills`; chat-app Project "Help Me AI"; rubric areas Context, Reuse, Connections, Delegation, Safety, Habits with levels Starting, Building, Strong.

## Before every commit

```bash
python3 -m unittest discover tests
```

## Releasing

1. Bump `metadata.version` in `skills/help-me-ai/SKILL.md` and commit.
2. `git tag vX.Y.Z && git push origin main vX.Y.Z` — the tag must equal `v` + the version.
3. The release workflow builds `help-me-ai.zip` and creates the release with it attached. The install link (`…/releases/latest/download/help-me-ai.zip`) then serves the new version. Edit the release notes on GitHub if you like.
4. Run the release checklist in `tests/scenarios.md`.
