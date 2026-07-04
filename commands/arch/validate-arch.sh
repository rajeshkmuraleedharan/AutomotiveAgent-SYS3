#!/usr/bin/env bash
# Validate ARC architecture element YAML blocks in specified files (or all .md files)
# Usage: commands/arch/validate-arch.sh [file.md ...]
#        commands/arch/validate-arch.sh --all

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

PYTHON="$REPO_ROOT/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

cd "$REPO_ROOT"
if [[ "${1:-}" == "--all" ]]; then
    "$PYTHON" "$REPO_ROOT/scripts/validate-architecture.py" --all
else
    "$PYTHON" "$REPO_ROOT/scripts/validate-architecture.py" "$@"
fi
