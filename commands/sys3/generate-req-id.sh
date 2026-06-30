#!/usr/bin/env bash
# Generate the next available SYS.3 requirement ID
# Usage: commands/sys3/generate-req-id.sh GPTP [count]
#        commands/sys3/generate-req-id.sh HTP 5

set -euo pipefail

TOPIC="${1:-}"
COUNT="${2:-1}"

if [[ -z "$TOPIC" ]]; then
    echo "Usage: $0 <GPTP|HTP|TSC|TSR> [count]" >&2
    exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
python3 "$REPO_ROOT/scripts/generate-req-id.py" --topic "$TOPIC" --count "$COUNT" --root "$REPO_ROOT"
