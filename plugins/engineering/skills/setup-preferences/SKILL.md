---
name: setup-preferences
description: Set up or inspect a user's writing and engineering profile, resolve project overrides, and optionally connect the profile to their host's persistent instructions.
---

# Set up preferences

- Read [the schema](assets/profile.schema.json) and [defaults](assets/defaults.json); use [the example](assets/profile.example.json) as a starting point, not as inferred user preferences.
- Load the user's supplied profile or `~/.config/agent-skills/profile.json` when present, then `.agent-skills.json` in the selected project when present.
- Validate each supplied layer against schema version 1; report unsupported fields, versions, or types instead of silently accepting them.
- Merge objects recursively and replace arrays; preserve omitted fields, then apply explicit task requests as the highest-priority instructions.
- Show the effective preferences in a few bullets, distinguishing defaults from user choices.
- If Python is already available, [the resolver](scripts/resolve_profile.py) performs the same validation and merge; it prints JSON and changes no files.
- Otherwise use the host's existing file tools; no new runtime is required.
- When asked to save or activate preferences, preserve existing files and add a short host instruction to read the profile and applicable skills; keep exact locations in the handoff.
- Use the installed skill's actual location in generated host instructions; do not assume the repository checkout exists on another machine.
- For chat hosts without local file access, ask the user to attach the profile and apply it within the supported project or conversation.
- When the user wants broader workflows, consult [optional toolkits](references/ecosystem.md); keep them optional and reuse installed capabilities when appropriate.
