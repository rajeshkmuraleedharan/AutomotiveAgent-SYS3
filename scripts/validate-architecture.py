#!/usr/bin/env python3
"""
Validate ARC architecture element YAML blocks against the architecture schema
(.github/instructions/architecture-schema.instructions.md).

Checks: ID grammar, type/asil vocabulary, mandatory realizes with resolution
against the repo's SYS-* requirement population, allocation-target ASIL
ceilings, and ASIL inheritance from realized requirements.

Usage:
    python scripts/validate-architecture.py file.md [file.md ...]
    python scripts/validate-architecture.py --all          # scan all .md files
    python scripts/validate-architecture.py --no-resolve   # skip realizes-resolution
"""

import argparse
import re
import sys
from pathlib import Path

import yaml  # pip install pyyaml

ARC_ID = re.compile(r"^ARC-[A-Z0-9]+-\d{3}$")
SYS_ID = re.compile(r"\bSYS-[A-Z0-9]+-\d{3}\b")
YAML_BLOCK = re.compile(r"^---\n(.*?)\n---", re.DOTALL | re.MULTILINE)

VALID_TYPE = {"system", "subsystem", "component", "interface"}
VALID_ASIL = {"QM", "A", "B", "C", "D"}

# ASIL ceiling per allocation target; None = not checked (hardware)
TARGET_CEILING = {
    "QNX:KryoP0": "B", "QNX:KryoP1": "B", "QNX:KryoE0": "B", "QNX:KryoE1": "B",
    "SAIL:SafeRTOS": "D", "QNX:Hexagon": "QM", "QNX:Adreno": "QM",
    "Hardware:88Q5050": None, "Hardware:88Q22xx": None, "Hardware:PMIC": None,
}

RANK = {"QM": 0, "A": 1, "B": 2, "C": 3, "D": 4}


def yaml_blocks(text: str) -> list[dict]:
    blocks = []
    for raw in YAML_BLOCK.findall(text):
        try:
            data = yaml.safe_load(raw)
        except yaml.YAMLError:
            continue
        if isinstance(data, dict):
            blocks.append(data)
    return blocks


def collect_requirements(root: Path) -> dict[str, str]:
    """Map every SYS-* requirement id found in repo YAML blocks to its ASIL."""
    reqs: dict[str, str] = {}
    for md in root.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for block in yaml_blocks(text):
            block_id = str(block.get("id", ""))
            if SYS_ID.fullmatch(block_id):
                reqs[block_id] = str(block.get("asil", "QM"))
    return reqs


def validate_element(data: dict, reqs: dict[str, str] | None) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    arc_id = str(data.get("id", "?"))
    prefix = f"[{arc_id}]"

    if not ARC_ID.fullmatch(arc_id):
        errors.append(f"{prefix} invalid ARC id format (expected ARC-{{AREA}}-NNN)")

    el_type = data.get("type")
    if el_type not in VALID_TYPE:
        errors.append(f"{prefix} invalid type: {el_type!r} (expected {sorted(VALID_TYPE)})")

    asil = data.get("asil", "QM")
    if asil not in VALID_ASIL:
        errors.append(f"{prefix} invalid asil: {asil!r}")

    realizes = data.get("realizes") or []
    if not realizes:
        errors.append(f"{prefix} missing realizes — every element realizes >= 1 SYS-* requirement")
    elif reqs is not None:
        max_req_rank = -1
        for rid in realizes:
            rid = str(rid)
            if rid not in reqs:
                errors.append(f"{prefix} realizes {rid} — requirement not found in repo")
            else:
                max_req_rank = max(max_req_rank, RANK.get(reqs[rid], 0))
        if max_req_rank > RANK.get(asil, 0) and not data.get("decomposition"):
            warnings.append(
                f"{prefix} asil {asil} below max realized requirement ASIL "
                f"({[k for k, v in RANK.items() if v == max_req_rank][0]}) "
                f"— add decomposition: note + safety-analyst sign-off"
            )

    targets = data.get("allocates_to") or []
    if el_type == "component" and not targets:
        errors.append(f"{prefix} component without allocates_to")
    for target in targets:
        target = str(target)
        if target not in TARGET_CEILING:
            errors.append(f"{prefix} invalid allocation target: {target!r}")
            continue
        ceiling = TARGET_CEILING[target]
        if ceiling is not None and RANK.get(asil, 0) > RANK[ceiling]:
            errors.append(f"{prefix} ASIL-{asil} exceeds {target} ceiling (ASIL-{ceiling})")

    if not data.get("description"):
        warnings.append(f"{prefix} missing description")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validate ARC architecture element blocks")
    parser.add_argument("files", nargs="*", help="Markdown files to validate")
    parser.add_argument("--all", action="store_true", help="Scan all .md files in repo")
    parser.add_argument("--no-resolve", action="store_true",
                        help="Skip realizes-resolution against the repo")
    args = parser.parse_args()

    root = Path(".").resolve()
    paths = list(root.rglob("*.md")) if args.all else [Path(f) for f in args.files]
    if not paths:
        print("No files to validate. Use --all or pass file paths.", file=sys.stderr)
        sys.exit(1)

    reqs = None if args.no_resolve else collect_requirements(root)

    all_errors, all_warnings, element_count = [], [], 0
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for block in yaml_blocks(text):
            if ARC_ID.fullmatch(str(block.get("id", ""))) or str(block.get("id", "")).startswith("ARC-"):
                element_count += 1
                errors, warnings = validate_element(block, reqs)
                all_errors += [f"[{path}]{e}" for e in errors]
                all_warnings += [f"[{path}]{w}" for w in warnings]

    for warning in all_warnings:
        print(f"WARN  {warning}")
    if all_errors:
        for error in all_errors:
            print(f"ERROR {error}")
        sys.exit(1)
    print(f"{element_count} architecture element(s) valid "
          f"({len(all_warnings)} warning(s)).")


if __name__ == "__main__":
    main()
