#!/usr/bin/env bash
# Export SYS.3 requirements to Codebeamer CSV format
# Usage: commands/sys3/cb-export.sh requirements/gptp-reqs.md [--output cb-import.csv]

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

PYTHON="$REPO_ROOT/.venv/bin/python3"
[[ -x "$PYTHON" ]] || PYTHON="python3"
OUTPUT="${CB_EXPORT_FILE:-cb-import.csv}"

FILES=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --output) OUTPUT="$2"; shift 2 ;;
        *) FILES+=("$1"); shift ;;
    esac
done

if [[ ${#FILES[@]} -eq 0 ]]; then
    echo "Usage: $0 <file.md> [file.md ...] [--output cb-import.csv]" >&2
    exit 1
fi

"$PYTHON" "$REPO_ROOT/scripts/cb-formatter.py" "${FILES[@]}" --output "$OUTPUT"
echo "Exported to: $OUTPUT"
