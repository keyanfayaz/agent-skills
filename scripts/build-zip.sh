#!/usr/bin/env bash
# Build OUT_DIR/help-me-ai.zip with the help-me-ai/ folder at the top level.
# Every install route uses this one file. Usage: scripts/build-zip.sh OUT_DIR
set -euo pipefail

out=${1:?usage: build-zip.sh OUT_DIR}
root=$(cd "$(dirname "$0")/.." && pwd)
skill="$root/skills/help-me-ai"
[ -f "$skill/SKILL.md" ] || { echo "missing $skill/SKILL.md" >&2; exit 1; }

mkdir -p "$out"
out=$(cd "$out" && pwd)
rm -f "$out/help-me-ai.zip"
(cd "$root/skills" && zip -r -X -q "$out/help-me-ai.zip" help-me-ai -x '*.DS_Store')
echo "$out/help-me-ai.zip"
