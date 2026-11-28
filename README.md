# Agent Skills

I use the Engineering plugin in Codex and Claude Code to set up repositories, review changes, verify apps, and prepare pull requests. Install it once and use its skills across projects.

- [Initialize repo](plugins/engineering/skills/initialize-repo/SKILL.md) sets up Git, connects GitHub when requested, and provides short README templates for apps and tools.
- [Review change](plugins/engineering/skills/review-change/SKILL.md) checks a diff against the requested behavior and reports findings with their trigger, location, and impact.
- [Verify app](plugins/engineering/skills/verify-app/SKILL.md) walks the affected user journeys and records what passed, failed, or still needs a runtime check.
- [Create PR](plugins/engineering/skills/create-pr/SKILL.md) drafts, opens, or updates a pull request using the final diff and actual verification results.

For example, after changing a signup form, ask **Review change** to check the diff against the acceptance criteria. Use **Verify app** to try a valid signup and an invalid submission, then ask **Create PR** to include the observed results.

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

Use `initialize-repo`, `review-change`, or `verify-app` in place of `create-pr`. To use a skill on its own, copy its whole folder from [skills](plugins/engineering/skills) into a supported skills directory. Each follows the [Agent Skills specification](https://agentskills.io/specification).

## Project guidance

Use the optional [project setup guide](plugins/engineering/docs/setup.md) and [AGENTS.md template](plugins/engineering/templates/AGENTS.md) when a repo needs its own commands, conventions, or verification instructions. The plugin also includes [coding style](plugins/engineering/skills/create-pr/references/coding-style.md), [setup preferences](plugins/engineering/skills/create-pr/references/setup-preferences.md), [working conventions](plugins/engineering/docs/preferences.md), and [open decisions](plugins/engineering/docs/pending.md).

The review and verification skills and project guidance came from [KF Stack](https://github.com/keyanfayaz/kf-stack/tree/d04fe99d8f783b5da2618f9e7aa313ea8dfef424). The optional [Things AppleScript adapter](https://github.com/keyanfayaz/things-applescript) is maintained separately.

## Add a skill

Add `plugins/engineering/skills/<skill-name>/SKILL.md` with a matching `name` and a `description` that says when to use it. Keep any linked resources in that skill's folder, and add the skill to the list above.

With Python 3 and `zip` installed, run the tests and build both kinds of archives from the repo root.

```sh
python3 -B -m unittest discover tests
scripts/build-zip.sh dist
python3 -B scripts/build-plugins.py dist
```
