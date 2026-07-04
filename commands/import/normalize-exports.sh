#!/usr/bin/env bash
# Normalize Codebeamer/JIRA/Confluence exports from imports/inbox/ into markdown
# Usage: commands/import/normalize-exports.sh                 # process the inbox
#        commands/import/normalize-exports.sh --dry-run
#        commands/import/normalize-exports.sh --tool jira --in export.csv

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

PYTHON="$REPO_ROOT/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"

cd "$REPO_ROOT"
"$PYTHON" "$REPO_ROOT/scripts/normalize-imports.py" "$@"
