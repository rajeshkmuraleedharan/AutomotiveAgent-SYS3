#!/usr/bin/env bash
# Mechanical lint pass over wiki/ topic pages
# Usage: commands/wiki/lint-wiki.sh [file.md ...]
#        commands/wiki/lint-wiki.sh --all
#        commands/wiki/lint-wiki.sh --all --fix   # also apply safe auto-fixes

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

PYTHON="$REPO_ROOT/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

cd "$REPO_ROOT"
"$PYTHON" "$REPO_ROOT/scripts/lint-wiki.py" "$@"
