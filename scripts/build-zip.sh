#!/usr/bin/env bash
# Build one standalone ZIP per skill, with its directory at the top level.
# Usage: scripts/build-zip.sh OUT_DIR
set -euo pipefail

out=${1:?usage: build-zip.sh OUT_DIR}
root=$(cd "$(dirname "$0")/.." && pwd)
skills="$root/plugins/engineering/skills"

mkdir -p "$out"
out=$(cd "$out" && pwd)
cd "$skills"
for manifest in */SKILL.md; do
    skill=${manifest%/SKILL.md}
    rm -f "$out/$skill.zip"
    zip -r -X -q "$out/$skill.zip" "$skill" -x '*.DS_Store'
    echo "$out/$skill.zip"
done
