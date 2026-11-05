---
name: write-pr
description: Draft or revise a pull request title and description from the final diff and actual validation, applying the user's optional writing preferences.
---

# Write a PR

- Read the final diff, relevant repository template, and actual verification results.
- Read optional writing preferences from `~/.config/agent-skills/profile.json`, then the selected project's `.agent-skills.json`; explicit requests take precedence.
- Lead with the resulting behavior and why it matters; describe the final change for a reviewer who has not seen the conversation.
- Use the configured format and detail level; with brief bullets, use one sentence per bullet and a second only when essential.
- Use `Summary` and `Validation` headings when helpful; add sections only for distinct reviewer needs.
- Include actual checks and material untested behavior; remove session history, repeated caveats, and abandoned approaches.
- Add before/after examples, screenshots, or links when they clarify the change.
- Use a structured body argument or `gh --body-file` to preserve newlines; inspect the saved body for broken links, fences, and literal `\n`.
- Drafting does not itself authorize creating, updating, or merging a PR; follow the user's requested scope.
