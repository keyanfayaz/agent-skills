# Grounded preferences

These are observations from existing local files, adapted into reusable guidance. They are not a complete personal policy. Detailed source locations and fingerprints are retained locally outside Git. Existing files demonstrate conventions; they do not establish authorship of every sentence.

| ID | Convention | Evidence and scope |
| --- | --- | --- |
| P1 | Keep a concrete root AGENTS guide with project context, commands, conventions, verification inputs, and completion criteria. Add narrower guides only where needed. | Existing personal skills-library template and setup notes. |
| P2 | Package a skill as a named folder with `SKILL.md`; carry its resources together. Use optional `scripts/`, `references/`, and `assets/` only when useful. | Existing personal skills-library layout and setup notes. |
| P3 | Use the shared plugin across projects. When a project needs local skills or references, keep them in that project's chosen skill directory or `.agents/references/`. Load only what the task needs. | Existing project guides used `.agents/skills/` and an index for project-specific resources. |
| P4 | Keep commits and PRs small. Short commit subjects; useful bodies capped at 4–5 bullets, each 1–2 sentences. PR descriptions use only `# Summary`, at most 7–8 bullets, each 1–2 sentences. | Existing personal AGENTS template. Commit prefix, branch naming, and commit timing were left unspecified. |
| P5 | Review against the request, acceptance criteria, and non-goals. Prioritize concrete correctness and regression impact; provide a trigger, location, impact, and fix direction. | Existing personal review skill and template. |
| P6 | Verify the observable behavior and show evidence. Report compile results separately from runtime tests; name blocked prerequisites. Use screenshots for relevant visual behavior. | Existing personal verification skill and user-owned project verification guide. |
| P7 | Keep generated writing restrained, direct, and free of filler. | Local memory and writing workflow, originally scoped to business writing. Carry the restraint preference cautiously; project voice rules stay with that project. |
| P8 | Keep workflows lean and make the smallest code change that meets the request. | Explicit preference for repo setup and engineering work. |

The reusable skills here are concise adaptations of the personal review and verification workflows. Project implementations, commercial facts, detailed brand rules, internal instructions, and runtime memory content are not bundled.
