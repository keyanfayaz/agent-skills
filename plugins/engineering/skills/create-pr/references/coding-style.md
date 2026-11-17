# Coding style

- Read the project's conventions first. Use the simplest correct design for its current requirements.
- Reuse existing code and standard tools. Minimize mutable state, speculative wrappers, and dependencies.
- Look for verified dead or redundant code in the scope you are already changing. Remove it when it simplifies the change and preserves behavior.
- Preserve required behavior and useful checks. Favor readable code over compressed expressions or line-count targets.
- Use language-native docstrings and the repository's established format. Document public contracts and non-obvious behavior concisely.
- Use comments to explain durable reasoning, invariants, external constraints, or meaningful tradeoffs. Omit narration and step banners.
- Use markers such as `KEEP:` or `IMPORTANT:` where they help preserve an invariant. Keep useful comments without labels.
- Preserve licenses, tool directives, required API documentation, and compatibility that callers still need.
- Verify changed behavior with checks appropriate to the risk and report the meaningful result.
