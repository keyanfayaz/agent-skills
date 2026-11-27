# Agent Skills

I use the Engineering plugin in Codex and Claude Code to review a change, check that it works, and prepare the pull request. Install it once and use its skills across projects.

- [Review change](plugins/engineering/skills/review-change/SKILL.md) checks a diff against the requested behavior and reports findings with their trigger, location, and impact.
- [Verify](plugins/engineering/skills/verify/SKILL.md) takes a Linear ticket and checks each acceptance criterion against the build.
- [Smoke test](plugins/engineering/skills/smoke-test/SKILL.md) runs the app's core flows on a build. It needs no ticket.
- [Create PR](plugins/engineering/skills/create-pr/SKILL.md) drafts, opens, or updates a pull request using the final diff and actual verification results.

For example, if a signup ticket requires an error for an expired invite, use **Verify** with that ticket number and a preview build. To check whether users can still sign in and complete the app's main task after a deployment, use **Smoke test**.

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

For a ticket, use `$engineering:verify ENG-123` in Codex or `/engineering:verify ENG-123` in Claude Code, replacing the example ID with your own. For a build check, use `$engineering:smoke-test` or `/engineering:smoke-test` and identify the build.

Existing [verify-app](plugins/engineering/skills/verify-app/SKILL.md) calls still work. Switch to `verify` for ticket checks or `smoke-test` for core flows. To use a skill on its own, copy its whole folder from [skills](plugins/engineering/skills) into a supported skills directory. Each follows the [Agent Skills specification](https://agentskills.io/specification).

## Project guidance

Use the optional [project setup guide](plugins/engineering/docs/setup.md) and [AGENTS.md template](plugins/engineering/templates/AGENTS.md) when a repo needs its own commands, conventions, or verification instructions. The plugin also includes [coding style](plugins/engineering/skills/create-pr/references/coding-style.md), [setup preferences](plugins/engineering/skills/create-pr/references/setup-preferences.md), [working conventions](plugins/engineering/docs/preferences.md), and [open decisions](plugins/engineering/docs/pending.md).

The review and verification skills and project guidance came from [KF Stack](https://github.com/keyanfayaz/kf-stack/tree/d04fe99d8f783b5da2618f9e7aa313ea8dfef424). The optional [Things AppleScript adapter](https://github.com/keyanfayaz/things-applescript) is maintained separately.
