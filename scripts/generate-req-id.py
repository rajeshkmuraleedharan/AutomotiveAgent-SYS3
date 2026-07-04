#!/usr/bin/env python3
"""
Generate the next available artefact ID for a given prefix and topic.
Scans all .md files in the repo for existing IDs and finds the next gap-free ID.

Prefixes:
    SYS  — SYS.3/SYS.2 requirements (topics: GPTP | HTP | TSC | TSR)
    ARC  — architecture elements (topic: any AREA, shares the SYS vocabulary)
    CON  — concepts (topic: feature short name)

Usage:
    python scripts/generate-req-id.py --topic GPTP
    python scripts/generate-req-id.py --prefix ARC --topic GPTP
    python scripts/generate-req-id.py --prefix CON --topic HOLDOVER --count 3
"""

import argparse
import re
from pathlib import Path


VALID_SYS_TOPICS = ["GPTP", "HTP", "TSC", "TSR"]
VALID_PREFIXES = ["SYS", "ARC", "CON"]
TOPIC_FORMAT = re.compile(r"^[A-Z0-9]+$")


def find_existing_ids(prefix: str, topic: str, root: Path) -> set[int]:
    """Scan all markdown files and return the set of used NNN values for prefix-topic."""
    pattern = re.compile(rf"\b{prefix}-{topic}-(\d{{3}})\b")
    used = set()
    for md_file in root.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in pattern.finditer(text):
            used.add(int(match.group(1)))
    return used


def main():
    parser = argparse.ArgumentParser(description="Generate next artefact ID")
    parser.add_argument("--prefix", default="SYS", choices=VALID_PREFIXES,
                        help="ID prefix: SYS (default) | ARC | CON")
    parser.add_argument("--topic", required=True,
                        help="Topic/area, e.g. GPTP, HTP, TSC, TSR (SYS is restricted to these)")
    parser.add_argument("--root", default=".", help="Repo root (default: current dir)")
    parser.add_argument("--count", type=int, default=1,
                        help="Number of IDs to generate (default: 1)")
    args = parser.parse_args()

    topic = args.topic.upper()
    if args.prefix == "SYS" and topic not in VALID_SYS_TOPICS:
        parser.error(f"SYS topic must be one of {VALID_SYS_TOPICS}")
    if not TOPIC_FORMAT.fullmatch(topic):
        parser.error("topic must be A–Z/0–9 only")

    root = Path(args.root).resolve()
    used = find_existing_ids(args.prefix, topic, root)

    n = 1
    generated = 0
    while generated < args.count:
        if n not in used:
            print(f"{args.prefix}-{topic}-{n:03d}")
            used.add(n)
            generated += 1
        n += 1


if __name__ == "__main__":
    main()
