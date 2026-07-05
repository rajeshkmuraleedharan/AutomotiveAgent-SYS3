#!/usr/bin/env bash
# Mechanical lint pass over wiki/ topic pages
# Usage: commands/wiki/lint-wiki.sh [file.md ...]
#        commands/wiki/lint-wiki.sh --all

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

PYTHON="$REPO_ROOT/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

cd "$REPO_ROOT"
if [[ "${1:-}" == "--all" ]]; then
    "$PYTHON" "$REPO_ROOT/scripts/lint-wiki.py" --all
else
    "$PYTHON" "$REPO_ROOT/scripts/lint-wiki.py" "$@"
fi
