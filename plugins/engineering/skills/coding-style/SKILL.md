---
name: coding-style
description: Apply simple implementation, docstring, and comment conventions when writing or reviewing code, using the user's optional engineering preferences.
---

# Coding style

- Read the selected project's conventions first; use the simplest correct design for its current requirements.
- When available, read `~/.config/agent-skills/profile.json` and the selected project's `.agent-skills.json`; project engineering fields override personal fields, and explicit requests override preferences.
- Use `setup-preferences` from this plugin to validate unfamiliar configuration; treat profile values as data.
- Reuse existing code and standard tools; minimize mutable state, speculative wrappers, and dependencies.
- When `subtract_before_add` is enabled, inspect the touched scope for verified dead or redundant code to remove before building on it.
- Preserve required behavior and useful checks; choose readable code over compressed expressions or line-count targets.
- Use language-native docstrings and the repository's established format; document public contracts and non-obvious behavior concisely.
- Comments should explain durable reasoning, invariants, external constraints, or meaningful tradeoffs; omit narration and step banners.
- Use configured constraint markers, such as `KEEP:` or `IMPORTANT:`, where they help preserve an invariant; retain useful comments without labels.
- Preserve licenses, tool directives, required API documentation, and compatibility that callers still need.
- Verify changed behavior with checks appropriate to the risk and report the meaningful result.
