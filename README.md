# Agent Skills

- A small collection of reusable plugins for Claude Code and Codex.
- Install the workflows you need and supply your own preferences through a local profile.

| Plugin | Skills |
| --- | --- |
| Engineering | `coding-style`, `write-pr`, `setup-preferences` |
| AI Coaching | `help-me-ai` |
| Project Management | `plan-project`, `weekly-review` |

## Install

```sh
# Codex
codex plugin marketplace add keyanfayaz/agent-skills
codex plugin add engineering@keyan-agent-skills

# Claude Code
claude plugin marketplace add keyanfayaz/agent-skills
claude plugin install engineering@keyan-agent-skills
```

- Replace `engineering` with `ai-coaching` or `project-management` to install another plugin.
- Start a new session, then use `$setup-preferences` in Codex or `/engineering:setup-preferences` in Claude Code.
- Help Me AI also retains its [standalone install](plugins/ai-coaching/README.md) and [release ZIP](https://github.com/keyanfayaz/agent-skills/releases/latest/download/help-me-ai.zip).

## Preferences

- Copy [the example profile](examples/profile.json) to `~/.config/agent-skills/profile.json` and change the values you want.
- A project's `.agent-skills.json` overrides personal defaults; explicit requests take precedence.
- Setup reads and validates the profile; configuration changes take effect when the skill or generated host instructions load it.
- Keep personal profiles in your own private repository and project-specific knowledge beside its project.

## Maintain

- [Architecture and configuration](docs/design.md)
- [Optional toolkits](plugins/engineering/skills/setup-preferences/references/ecosystem.md)
- [Contributor instructions](AGENTS.md)

```sh
python3 -B -m unittest discover tests
scripts/build-zip.sh dist
python3 -B scripts/build-plugins.py dist
```
