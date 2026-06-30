#!/usr/bin/env bash
# Quick ASPICE SYS.3 compliance check — finds requirements missing mandatory fields
# Usage: commands/review/aspice-check.sh [--all | file.md ...]

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

echo "=== ASPICE SYS.3 Compliance Check ==="
echo

# Run schema validation (covers mandatory fields, ASIL, weak verbs)
if [[ "${1:-}" == "--all" ]]; then
    python3 "$REPO_ROOT/scripts/validate-requirements.py" --all
else
    python3 "$REPO_ROOT/scripts/validate-requirements.py" "$@"
fi

EXIT_CODE=$?

echo
if [[ $EXIT_CODE -eq 0 ]]; then
    echo "PASS — all requirements meet mandatory field requirements."
else
    echo "FAIL — see errors above. Fix before submitting for design review."
fi

exit $EXIT_CODE
