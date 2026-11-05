# Toolkit design

- One repository hosts several independently installable plugins; skills express individual workflows.
- Each plugin owns its manifests, resources, and version; installed packages never depend on repository-level files.
- Platform manifests adapt the same source for Codex and Claude Code.
- Help Me AI's [coaching design](../plugins/ai-coaching/docs/design.md), standalone ZIP, and `~/help-me-ai/` state remain separate from toolkit preferences.

## Configuration

- Format: JSON with `schema_version: 1`, defined by the bundled [schema](../plugins/engineering/skills/setup-preferences/assets/profile.schema.json).
- Precedence: bundled defaults, personal profile, project overrides, explicit request.
- Personal profile: `~/.config/agent-skills/profile.json`; project overrides: `.agent-skills.json` at the selected project's root.
- Objects merge recursively; supplied arrays replace earlier arrays; missing fields preserve earlier values.
- Unknown fields, unsupported versions, and wrong types are rejected; a request cannot override host permissions.
- Configuration is data, not executable instructions; it affects behavior only when a skill or generated host rule explicitly loads it.
- The optional standard-library resolver prints effective preferences without modifying files:

```sh
python3 plugins/engineering/skills/setup-preferences/scripts/resolve_profile.py \
  --profile examples/profile.json --project /path/to/project/.agent-skills.json
```

- `setup-preferences` can perform the same merge with existing file tools when Python is unavailable.
- New domain plugins can use their own configuration when needed; version this shared schema before extending its contract.

## Releases and history

- Existing `v0.1.0` and `v0.1.1` tags and their attached Help Me AI ZIPs remain unchanged.
- New `v*` tags still release only the standalone coaching skill; plugin archives are built and validated separately.
- Use descriptive plugin version tags such as `engineering-v0.1.0`; publish those releases with `gh release create ... --latest=false` so the standalone ZIP's latest URL keeps working.
- Pre-toolkit history is preserved on `archive/main-before-toolkit-20261105`; the replacement baseline has the exact same tree as the former `main`.
- Existing clones of the former history should use a fresh clone or explicitly reconcile against the new `main`.
