#!/usr/bin/env python3
"""
Normalize offline tool exports (Codebeamer / JIRA / Confluence) into markdown.

Raw exports are dropped into imports/inbox/. This script parses them into
agent-readable markdown under imports/normalized/{tool}/, appends a row to
imports/normalized/manifest.md, and moves the raw file to imports/archive/.

Usage:
    python scripts/normalize-imports.py                       # process everything in imports/inbox/
    python scripts/normalize-imports.py --in FILE [--in ...]  # process specific file(s)
    python scripts/normalize-imports.py --tool jira --in f.xlsx   # force tool detection
    python scripts/normalize-imports.py --dry-run             # parse + report, write nothing
    python scripts/normalize-imports.py --keep                # don't archive raw files

Tool auto-detection:
    .csv/.xlsx  -> JIRA if the header row has "Issue key", else Codebeamer
    .html/.htm  -> Confluence
    .docx       -> Confluence page (use --tool codebeamer for CB Word table exports)
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

from importers import codebeamer, common, confluence, jira

MODULES = {"codebeamer": codebeamer, "jira": jira, "confluence": confluence}
SUPPORTED = {".csv", ".xlsx", ".docx", ".html", ".htm"}


def _header_cells(path: Path) -> list[str]:
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as f:
            import csv

            return next(csv.reader(f), [])
    if path.suffix.lower() == ".xlsx":
        import openpyxl

        ws = openpyxl.load_workbook(path, read_only=True).active
        first = next(ws.iter_rows(values_only=True), ())
        return [str(c) for c in first if c is not None]
    return []


def detect_tool(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in (".html", ".htm", ".docx"):
        return "confluence"
    headers = {common.norm_key(h) for h in _header_cells(path)}
    return "jira" if "issuekey" in headers else "codebeamer"


def archive(path: Path) -> Path:
    target = common.archive_dir() / path.name
    if target.exists():
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        target = target.with_name(f"{path.stem}-{stamp}{path.suffix}")
    shutil.move(str(path), str(target))
    return target


def process(path: Path, tool: str | None, dry_run: bool, keep: bool) -> bool:
    tool = tool or detect_tool(path)
    module = MODULES[tool]
    try:
        out_path, text, count = module.import_file(path)
    except Exception as e:
        print(f"ERROR  {path.name}: {e}", file=sys.stderr)
        return False

    if dry_run:
        print(f"DRY    {path.name} -> {out_path.relative_to(common.repo_root())} "
              f"[{tool}, {count} item(s)]")
        return True

    out_path.write_text(text, encoding="utf-8")
    common.update_manifest(tool, path, out_path, count)
    note = ""
    if not keep:
        archived = archive(path)
        note = f" (raw -> imports/archive/{archived.name})"
    print(f"OK     {path.name} -> {out_path.relative_to(common.repo_root())} "
          f"[{tool}, {count} item(s)]{note}")
    return True


def main():
    parser = argparse.ArgumentParser(description="Normalize Codebeamer/JIRA/Confluence exports")
    parser.add_argument("--in", dest="files", action="append", default=[],
                        help="Specific export file(s); default: scan imports/inbox/")
    parser.add_argument("--tool", choices=sorted(MODULES),
                        help="Force the tool instead of auto-detecting")
    parser.add_argument("--dry-run", action="store_true", help="Parse and report, write nothing")
    parser.add_argument("--keep", action="store_true", help="Don't move raw files to archive")
    args = parser.parse_args()

    if args.files:
        paths = [Path(f) for f in args.files]
        missing = [p for p in paths if not p.exists()]
        if missing:
            sys.exit(f"Not found: {', '.join(str(p) for p in missing)}")
        # explicit files are only archived when they sit in the inbox
        inbox = common.repo_root() / "imports" / "inbox"
        keep_flags = {p: args.keep or inbox not in p.resolve().parents for p in paths}
    else:
        inbox = common.repo_root() / "imports" / "inbox"
        paths = sorted(p for p in inbox.iterdir()
                       if p.is_file() and p.suffix.lower() in SUPPORTED)
        if not paths:
            print(f"Nothing to do — drop exports into {inbox.relative_to(common.repo_root())}/")
            return
        keep_flags = {p: args.keep for p in paths}

    results = [process(p, args.tool, args.dry_run, keep_flags[p]) for p in paths]
    if not all(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
