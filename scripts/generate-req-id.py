#!/usr/bin/env python3
"""
Generate the next available SYS.3 requirement ID for a given topic.
Scans all .md files in the repo for existing IDs and finds the next gap-free ID.

Usage:
    python scripts/generate-req-id.py --topic GPTP
    python scripts/generate-req-id.py --topic HTP
    python scripts/generate-req-id.py --topic TSC
    python scripts/generate-req-id.py --topic TSR
"""

import argparse
import re
from pathlib import Path


VALID_TOPICS = ["GPTP", "HTP", "TSC", "TSR"]
ID_PATTERN = re.compile(r"SYS-(GPTP|HTP|TSC|TSR)-(\d{3})")


def find_existing_ids(topic: str, root: Path) -> set[int]:
    """Scan all markdown files and return the set of used NNN values for topic."""
    used = set()
    for md_file in root.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for match in ID_PATTERN.finditer(text):
            if match.group(1) == topic:
                used.add(int(match.group(2)))
    return used


def next_id(topic: str, used: set[int]) -> str:
    """Return the next sequential ID, filling gaps if any."""
    n = 1
    while n in used:
        n += 1
    return f"SYS-{topic}-{n:03d}"


def main():
    parser = argparse.ArgumentParser(description="Generate next SYS.3 requirement ID")
    parser.add_argument("--topic", required=True, choices=VALID_TOPICS,
                        help="Requirement topic: GPTP | HTP | TSC | TSR")
    parser.add_argument("--root", default=".", help="Repo root (default: current dir)")
    parser.add_argument("--count", type=int, default=1,
                        help="Number of IDs to generate (default: 1)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    used = find_existing_ids(args.topic, root)

    n = 1
    generated = 0
    while generated < args.count:
        if n not in used:
            print(f"SYS-{args.topic}-{n:03d}")
            used.add(n)
            generated += 1
        n += 1


if __name__ == "__main__":
    main()
