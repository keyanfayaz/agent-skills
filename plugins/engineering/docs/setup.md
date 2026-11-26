# Use in a project

Use the shared Engineering plugin across projects. Follow these optional steps when a project needs persistent instructions of its own.

1. Inspect the target project's existing AGENTS files and skill organization.
2. Open [the AGENTS template](../templates/AGENTS.md). Merge useful sections into an existing guide, or create a root guide if the project has none. Replace every `[TODO]`, remove inapplicable sections, and verify commands against the project.
3. Use the installed [review-change](../skills/review-change/SKILL.md) and [verify-app](../skills/verify-app/SKILL.md) skills wherever they apply. For standalone use, copy the chosen skill folder into a directory the client reads. Compare any same-named skill before replacing it.
4. Where useful, mention relevant skills in the project's guide. Fill the verification profile with real commands, journeys, roles, and an evidence location.
5. Keep project facts and private references in that project. Where useful, point the root guide to its own `.agents/references/` files instead of expanding the guide.
6. Review the diff and run the project's relevant checks before relying on the new instructions.

## Skill layout

```text
skill-name/
  SKILL.md          # name and description frontmatter, then workflow
  scripts/          # optional repeatable executable work
  references/       # optional task-specific reading
  assets/           # optional output resources
```

A self-contained skill needs only `SKILL.md`. The discovery description should say what it does and when it applies. Link supporting files from the workflow and copy them with the folder. Keep one maintained source for each fact.

For standalone use, verify the client discovers the skill in a fresh session. The Engineering plugin includes these workflows and the project template in one package.
