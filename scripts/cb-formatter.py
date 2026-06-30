#!/usr/bin/env python3
"""
Convert SYS.3 requirement YAML blocks to Codebeamer CSV import format.

Usage:
    python scripts/cb-formatter.py requirements/gptp-reqs.md --output cb-import.csv

NOTE: Column order matches TODO — update after CB project configuration.
"""

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml  # pip install pyyaml

YAML_BLOCK = re.compile(r"^---\n(.*?)\n---\s*\n\*\*[^\*]+\*\*\s*\n\n(.*?)(?=^---|\Z)",
                        re.DOTALL | re.MULTILINE)

# TODO: Update these column names to match your Codebeamer SYS.3 tracker field names
CB_COLUMNS = [
    "Summary",          # id + title
    "Description",      # SHALL statement (plain text)
    "ASIL",
    "Verification Method",
    "Verification Criteria",
    "Rationale",
    "Safety Mechanism",
    "References",
    "Allocated To",
    "Status",
    "Tags",
]


def extract_title(req_text: str) -> str:
    m = re.search(r"\*\*[^\*]+ — ([^\*]+)\*\*", req_text)
    return m.group(1).strip() if m else ""


def yaml_to_cb_row(data: dict, req_text: str) -> dict:
    title = extract_title(req_text)
    req_id = data.get("id", "")

    refs = data.get("references", [])
    refs_str = "\n".join(refs) if isinstance(refs, list) else str(refs)

    allocates = data.get("allocates_to", [])
    allocates_str = ", ".join(allocates) if isinstance(allocates, list) else str(allocates)

    tags = data.get("tags", [])
    tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags)

    # Strip YAML block markers from req_text to get plain description
    plain_text = re.sub(r"^---.*?---\s*\n", "", req_text, flags=re.DOTALL).strip()
    plain_text = re.sub(r"\*\*[^\*]+\*\*\s*\n\n", "", plain_text, count=1)

    return {
        "Summary": f"{req_id} — {title}" if title else req_id,
        "Description": plain_text,
        "ASIL": data.get("asil", ""),
        "Verification Method": data.get("verification", ""),
        "Verification Criteria": data.get("verification_criteria", "").strip(),
        "Rationale": data.get("rationale", "").strip(),
        "Safety Mechanism": data.get("safety_mechanism", "").strip(),
        "References": refs_str,
        "Allocated To": allocates_str,
        "Status": "Draft",
        "Tags": tags_str,
    }


def process_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    rows = []
    for match in YAML_BLOCK.finditer(text):
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            rows.append(yaml_to_cb_row(data, match.group(0)))
    return rows


def main():
    parser = argparse.ArgumentParser(description="Format SYS.3 YAML to Codebeamer CSV")
    parser.add_argument("files", nargs="+", help="Markdown files with YAML requirement blocks")
    parser.add_argument("--output", default="cb-import.csv", help="Output CSV file")
    args = parser.parse_args()

    all_rows = []
    for f in args.files:
        all_rows.extend(process_file(Path(f)))

    if not all_rows:
        print("No requirement blocks found.", file=sys.stderr)
        sys.exit(1)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CB_COLUMNS)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Wrote {len(all_rows)} requirements to {args.output}")


if __name__ == "__main__":
    main()
