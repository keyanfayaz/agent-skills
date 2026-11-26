# Project instructions

<!-- Replace every [TODO], remove inapplicable sections, and check each command. -->

## Project context

- Purpose and users: [TODO]
- Stack and package manager: [TODO]
- Key directories and architecture boundaries: [TODO]
- Canonical references and read order: [TODO]
- Scope and non-goals: [TODO]

## Setup and commands

Run from: [TODO]

- Setup: `[TODO]`
- Development: `[TODO]`
- Lint/format: `[TODO]`
- Type-check: `[TODO or N/A]`
- Focused tests: `[TODO]`
- Full tests: `[TODO]`
- Build: `[TODO or N/A]`

Use the existing package manager and lockfile.

## Working conventions

- Read relevant code and nearby tests before editing.
- Keep work scoped and preserve unrelated changes.
- Follow the repository's established patterns and formatter/linter configuration.
- Project naming, type, error-handling, and comment conventions: [TODO or omit]
- Update documentation when behavior or setup changes.
- Test expectations for changed behavior: [TODO]

## Skills and references

- Relevant skills and when to use them: [TODO]
- Project-local skills: `.agents/skills/<skill-name>/SKILL.md`, if used.
- Canonical reference files: [TODO; use .agents/references/ if appropriate]

Keep the root guide concise. Add narrower AGENTS files only where a subtree needs different guidance. Load references relevant to the task.

## Verification profile

- Application type and supported platforms: [TODO or N/A]
- Start command and local URL: [TODO or N/A]
- Critical journeys and acceptance criteria: [TODO]
- Roles and test-data prerequisites: [TODO or N/A]
- Browsers/devices/viewports: [TODO or N/A]
- Evidence output location: [TODO]
- Required completion checks: [TODO]

Report exact checks and results. Distinguish source inspection, compilation, and executed runtime tests. State the prerequisite for any blocked check.

## Commits and pull requests

- Commit timing and format: [TODO; follow this project's convention]
- Branch and PR title conventions: [TODO or omit]
- Keep each commit and PR focused on one coherent change.
- Use a short commit subject. If a body helps, use at most 4–5 bullets, each 1–2 sentences.
- A PR description contains only a `# Summary` section with at most 7–8 bullets, each 1–2 sentences. Put validation, risks, and screenshot references in those bullets.

## Definition of done

The requested behavior is verified proportionally to risk, documentation is current, and the handoff states changes, evidence, and remaining gaps.
