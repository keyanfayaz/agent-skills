---
name: create-pr
description: Draft, open, or update a pull request using the final diff, repository template, and actual verification results. Use when asked to prepare, create, or revise a PR.
---

# Create PR

1. Read the repository instructions and PR template. Check the base, the head, the complete diff between them, and which verification actually ran.
2. Write a title and body that explain the final change and why it matters to a reviewer seeing it for the first time. Follow the user's writing preferences and the repo's template. Use short bullets and `Summary` and `Validation` headings when the template leaves the format open.
3. List actual checks and any material gaps in coverage. Include before-and-after examples, screenshots, or links when they help the reviewer. Omit session history and abandoned approaches.
4. For a request to draft copy, return the title and body. For a request to open or update a PR, check for an existing PR for that head, then use the repository's PR tool or `gh` to perform the requested action. If a push is needed, verify the head contains the intended changes before pushing it.
5. Pass the body as a structured field or with `gh --body-file` to preserve line breaks. Read back the saved PR, check its title, formatting, and base, and return its link.

See [setup preferences](references/setup-preferences.md) when asked how to save writing preferences. See [coding style](references/coding-style.md) when the request also involves changing code.
