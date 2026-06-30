#!/usr/bin/env python3
"""
Validate SYS.3 requirement YAML attribute blocks against the canonical schema.
Reports missing mandatory fields and common anti-patterns.

Usage:
    python scripts/validate-requirements.py requirements/gptp-reqs.md
    python scripts/validate-requirements.py --all    # scan all .md files
"""

import argparse
import re
import sys
from pathlib import Path

import yaml  # pip install pyyaml


REQUIRED_ALWAYS = ["id", "level", "asil", "source", "verification", "verification_criteria"]
REQUIRED_ASIL_A_PLUS = ["rationale", "references", "safety_mechanism"]
REQUIRED_ASIL_B_PLUS = ["allocates_to"]

VALID_ASIL = {"QM", "A", "B", "C", "D"}
VALID_VERIFICATION = {"TEST", "ANALYSIS", "INSPECTION", "DEMONSTRATION"}
VALID_ALLOCATES = {
    "QNX:KryoP0", "QNX:KryoP1", "QNX:KryoE0", "QNX:KryoE1",
    "SAIL:SafeRTOS", "QNX:Hexagon", "QNX:Adreno",
    "Hardware:88Q5050", "Hardware:88Q22xx", "Hardware:PMIC",
}

WEAK_VERBS = re.compile(r"\b(should|may|might|could|as appropriate|as required|reasonable)\b", re.I)
YAML_BLOCK = re.compile(r"^---\n(.*?)\n---", re.DOTALL | re.MULTILINE)


def asil_rank(asil: str) -> int:
    return {"QM": 0, "A": 1, "B": 2, "C": 3, "D": 4}.get(asil, -1)


def validate_block(raw_yaml: str, file_path: str, block_num: int) -> list[str]:
    errors = []
    try:
        data = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        return [f"[{file_path}] block {block_num}: YAML parse error: {e}"]

    if not isinstance(data, dict):
        return [f"[{file_path}] block {block_num}: not a dict"]

    req_id = data.get("id", f"block-{block_num}")
    prefix = f"[{req_id}]"

    for field in REQUIRED_ALWAYS:
        if not data.get(field):
            errors.append(f"{prefix} missing required field: {field}")

    asil = data.get("asil", "QM")
    if asil not in VALID_ASIL:
        errors.append(f"{prefix} invalid asil value: {asil!r}")

    if data.get("verification") and data["verification"] not in VALID_VERIFICATION:
        errors.append(f"{prefix} invalid verification: {data['verification']!r}")

    rank = asil_rank(asil)
    if rank >= 1:  # ASIL-A+
        for field in REQUIRED_ASIL_A_PLUS:
            if not data.get(field):
                errors.append(f"{prefix} ASIL-{asil}: missing {field}")

    if rank >= 2:  # ASIL-B+
        for field in REQUIRED_ASIL_B_PLUS:
            if not data.get(field):
                errors.append(f"{prefix} ASIL-{asil}: missing {field}")

    vc = data.get("verification_criteria", "")
    if vc and WEAK_VERBS.search(vc):
        errors.append(f"{prefix} verification_criteria contains weak language")

    return errors


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    blocks = YAML_BLOCK.findall(text)
    all_errors = []
    for i, block in enumerate(blocks, 1):
        all_errors.extend(validate_block(block, str(path), i))
    return all_errors


def main():
    parser = argparse.ArgumentParser(description="Validate SYS.3 requirement YAML blocks")
    parser.add_argument("files", nargs="*", help="Markdown files to validate")
    parser.add_argument("--all", action="store_true", help="Scan all .md files in repo")
    args = parser.parse_args()

    paths = []
    if args.all:
        paths = list(Path(".").rglob("*.md"))
    else:
        paths = [Path(f) for f in args.files]

    if not paths:
        print("No files to validate. Use --all or pass file paths.", file=sys.stderr)
        sys.exit(1)

    all_errors = []
    for p in paths:
        all_errors.extend(validate_file(p))

    if all_errors:
        for err in all_errors:
            print(err)
        sys.exit(1)
    else:
        print(f"All {len(paths)} file(s) valid.")


if __name__ == "__main__":
    main()
