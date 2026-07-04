#!/usr/bin/env bash
# Validate SYS.3 requirement YAML blocks in specified files (or all .md files)
# Usage: commands/sys3/validate-schema.sh [file.md ...]
#        commands/sys3/validate-schema.sh --all

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

PYTHON="$REPO_ROOT/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

if [[ "${1:-}" == "--all" ]]; then
    "$PYTHON" "$REPO_ROOT/scripts/validate-requirements.py" --all
else
    "$PYTHON" "$REPO_ROOT/scripts/validate-requirements.py" "$@"
fi
