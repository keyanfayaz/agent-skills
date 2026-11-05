# AI Coaching

- `help-me-ai` coaches clients through practical AI improvements; its behavior is defined in [the design](docs/design.md).
- Preserve the skill name, `~/help-me-ai/` client data folder, and existing privacy, consent, backup, and recovery behavior.
- Client-facing language stays plain; the skill never exposes its internal file names or the words "mode", "rubric", or "access level".
- The standalone skill requires no new client runtimes; do not instruct clients to install git, Node, Python, or other dependencies.
- Keep `SKILL.md` under 500 lines and descriptions at most 200 characters; only the entrypoint links to its reference and asset files.
- Client progress and reports stay outside this repository; local working notes belong in gitignored `.plans/`.
- Plugin packaging and the standalone ZIP share the same skill source; the ZIP retains `help-me-ai/` as its top-level folder.
- Run `python3 -B -m unittest discover tests` from the repository root before committing.
