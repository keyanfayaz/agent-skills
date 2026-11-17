# Agent Skills

My engineering workflows and preferences for Codex and Claude Code.

- [Create PR](plugins/engineering/skills/create-pr/SKILL.md) drafts, opens, or updates a pull request using the final diff and actual verification results.
- [Coding style](plugins/engineering/skills/create-pr/references/coding-style.md) covers implementation, docstrings, and comments.
- [Setup preferences](plugins/engineering/skills/create-pr/references/setup-preferences.md) shows how to apply personal and project guidance.

The plugin bundles the skill and both references. To use the skill on its own, copy the entire `create-pr` directory into your client's skills directory. It follows the [Agent Skills specification](https://agentskills.io/specification).

## Install

### Codex

```sh
codex plugin marketplace add keyanfayaz/agent-skills
codex plugin add engineering@keyan-agent-skills
```

Start a new session and use `$engineering:create-pr`.

### Claude Code

```sh
claude plugin marketplace add keyanfayaz/agent-skills
claude plugin install engineering@keyan-agent-skills
```

Start a new session and use `/engineering:create-pr`.
