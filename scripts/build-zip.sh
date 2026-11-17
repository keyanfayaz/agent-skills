#!/usr/bin/env bash
# Build OUT_DIR/create-pr.zip with the create-pr/ folder at the top level.
# Usage: scripts/build-zip.sh OUT_DIR
set -euo pipefail

out=${1:?usage: build-zip.sh OUT_DIR}
root=$(cd "$(dirname "$0")/.." && pwd)
skills="$root/plugins/engineering/skills"
skill="$skills/create-pr"
[ -f "$skill/SKILL.md" ] || { echo "missing $skill/SKILL.md" >&2; exit 1; }

mkdir -p "$out"
out=$(cd "$out" && pwd)
rm -f "$out/create-pr.zip"
(cd "$skills" && zip -r -X -q "$out/create-pr.zip" create-pr -x '*.DS_Store')
echo "$out/create-pr.zip"
