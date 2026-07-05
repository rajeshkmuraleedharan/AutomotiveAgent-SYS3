#!/usr/bin/env python3
"""
Mechanical lint pass over wiki/ topic pages.

Checks: index/topic-file consistency, 5-section schema conformance, dangling ID
references (IDs cited but not found anywhere in imports/normalized/ or
knowledge-base/), dangling ADR links, date-based staleness (topic's Last updated
predates a manifest.md row touching that topic's IDs with no matching History
line), and Current-State bloat (split candidates).

This is the mechanical half of the lint pass — see .github/prompts/wiki-lint.prompt.md
for the LLM-judgment half (contradictions, content-drift staleness, stale Open
Questions). This script never detects semantic contradictions; that's out of scope
for a mechanical checker by design (see rules/wiki-rules.md).

With --fix, applies ONLY the two auto-fixable findings from rules/wiki-rules.md's
Auto-Fix Categorization table (missing wiki/index.md row; Last-updated date behind
the page's own History) — everything else (dangling IDs/ADR links, bloat) is
reported only, never auto-applied, because it needs human/LLM judgment.

Usage:
    python scripts/lint-wiki.py file.md [file.md ...]
    python scripts/lint-wiki.py --all             # scan all wiki/topics/*.md files
    python scripts/lint-wiki.py --all --fix       # also apply safe auto-fixes
"""

import argparse
import re
import sys
from pathlib import Path

SECTION_ORDER = ["Current State", "Open Questions", "Decisions", "Cross-References", "History"]
HEADER_RE = re.compile(r"Area:\s*(\S+)\s*\|\s*Status:\s*([^|]+)\|\s*Last updated:\s*(\S+)")
SECTION_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
ID_RE = re.compile(r"\b(?:SYS|ARC|CON)-[A-Z0-9]+-\d{3}\b|\b[A-Z][A-Z0-9]{2,}-\d+\b")
ADR_RE = re.compile(r"\bADR-(\d{3})\b")
BULLET_RE = re.compile(r"^- ", re.MULTILINE)
BLOAT_THRESHOLD = 15


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def index_rows(root: Path) -> dict[str, str]:
    """Parse wiki/index.md table -> {topic_link_target: status}."""
    index_path = root / "wiki" / "index.md"
    if not index_path.exists():
        return {}
    rows = {}
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "Topic" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        match = re.search(r"\(([^)]+)\)", cells[0])
        if match:
            rows[Path(match.group(1)).stem] = cells[2]
    return rows


def parse_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    header = HEADER_RE.search(text)
    sections = {}
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[m.group(1).strip()] = text[start:end].strip()
    return {
        "text": text,
        "area": header.group(1) if header else None,
        "status": header.group(2).strip() if header else None,
        "last_updated": header.group(3) if header else None,
        "sections": sections,
        "section_order": [m.group(1).strip() for m in matches],
    }


def known_ids(root: Path) -> set[str]:
    """Every ID appearing anywhere under imports/normalized/ or knowledge-base/."""
    ids = set()
    for base in (root / "imports" / "normalized", root / "knowledge-base"):
        if not base.exists():
            continue
        for md in base.rglob("*.md"):
            try:
                ids.update(ID_RE.findall(md.read_text(encoding="utf-8")))
            except (UnicodeDecodeError, OSError):
                continue
    return ids


def manifest_rows(root: Path) -> list[dict]:
    manifest = root / "imports" / "normalized" / "manifest.md"
    if not manifest.exists():
        return []
    rows = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "Imported" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        rows.append({"date": cells[0], "file": cells[4].strip("`")})
    return rows


def lint_page(path: Path, root: Path, ids: set[str], manifest: list[dict],
              existing_topics: set[str]) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    page = parse_page(path)
    prefix = f"[{path.name}]"

    if not page["area"] or not page["status"] or not page["last_updated"]:
        errors.append(f"{prefix} missing or malformed header line (Area: ... | Status: ... | Last updated: ...)")

    present = [s for s in page["section_order"] if s in SECTION_ORDER]
    if present != SECTION_ORDER:
        missing = [s for s in SECTION_ORDER if s not in page["sections"]]
        if missing:
            errors.append(f"{prefix} missing section(s): {missing}")
        elif present != SECTION_ORDER:
            errors.append(f"{prefix} sections out of order: {present}")

    cross_refs = page["sections"].get("Cross-References", "")
    for ref_id in set(ID_RE.findall(cross_refs)):
        if ref_id not in ids:
            errors.append(f"{prefix} dangling ID in Cross-References: {ref_id} not found in imports/normalized/ or knowledge-base/")

    decisions = page["sections"].get("Decisions", "")
    for adr_num in ADR_RE.findall(decisions):
        adr_files = list((root / "project-context" / "decisions").glob(f"ADR-{adr_num}-*.md"))
        if not adr_files:
            errors.append(f"{prefix} dangling ADR link: ADR-{adr_num} not found in project-context/decisions/")

    current_state = page["sections"].get("Current State", "")
    bullet_count = len(BULLET_RE.findall(current_state))
    if bullet_count > BLOAT_THRESHOLD:
        warnings.append(f"{prefix} Current State has {bullet_count} bullets (> {BLOAT_THRESHOLD}) — split candidate")

    if page["area"]:
        history = page["sections"].get("History", "")
        relevant = [r for r in manifest if page["area"] in known_ids_in_file(root, r["file"], page["area"])]
        for row in relevant:
            if row["date"][:10] > (page["last_updated"] or "") and row["file"] not in history and row["date"] not in history:
                warnings.append(f"{prefix} possibly stale: manifest row {row['date']} ({row['file']}) postdates "
                                f"Last updated ({page['last_updated']}) with no matching History line")

    topic_link = path.stem
    if topic_link not in existing_topics:
        warnings.append(f"{prefix} not referenced in wiki/index.md")

    return errors, warnings


def fix_missing_index_row(path: Path, root: Path) -> str | None:
    """Append a wiki/index.md row for a topic page missing one. Returns a fix summary or None."""
    page = parse_page(path)
    if not page["area"] or not page["status"] or not page["last_updated"]:
        return None  # can't safely build a row without a valid header
    index_path = root / "wiki" / "index.md"
    slug = path.stem
    row = (f"| [{slug}](topics/{path.name}) | {page['area']} | {page['status']} | "
           f"{page['last_updated']} | (see page History) |\n")
    text = index_path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    index_path.write_text(text + row, encoding="utf-8")
    return f"added wiki/index.md row for {slug}"


def fix_stale_header_date(path: Path, root: Path) -> str | None:
    """Bump the header Last-updated date if History mentions a later one. Returns a fix summary or None."""
    page = parse_page(path)
    if not page["last_updated"]:
        return None
    history = page["sections"].get("History", "")
    history_dates = re.findall(r"\b(\d{4}-\d{2}-\d{2})\b", history)
    if not history_dates:
        return None
    latest = max(history_dates)
    if latest <= page["last_updated"]:
        return None
    text = page["text"]
    new_text = HEADER_RE.sub(
        lambda m: f"Area: {m.group(1)} | Status: {m.group(2).strip()} | Last updated: {latest}",
        text, count=1,
    )
    path.write_text(new_text, encoding="utf-8")
    return f"updated Last updated {page['last_updated']} -> {latest} in {path.name} (from History)"


def known_ids_in_file(root: Path, rel_path: str, area: str) -> str:
    """Return area if the referenced normalized file contains an ID for that area, else ''."""
    full = root / rel_path
    if not full.exists():
        return ""
    try:
        text = full.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""
    return area if re.search(rf"-{re.escape(area)}-\d{{3}}\b", text) else ""


def main():
    parser = argparse.ArgumentParser(description="Lint wiki/ topic pages (mechanical checks)")
    parser.add_argument("files", nargs="*", help="Topic page files to lint")
    parser.add_argument("--all", action="store_true", help="Lint all wiki/topics/*.md files")
    parser.add_argument("--fix", action="store_true",
                        help="Apply safe auto-fixes (missing index row, stale header date) before reporting")
    args = parser.parse_args()

    root = repo_root()
    paths = sorted((root / "wiki" / "topics").glob("*.md")) if args.all else [Path(f) for f in args.files]
    if not paths:
        print("No files to lint. Use --all or pass file paths.", file=sys.stderr)
        sys.exit(1)

    if args.fix:
        existing_topics = set(index_rows(root).keys())
        for path in paths:
            fixed = fix_stale_header_date(path, root)
            if fixed:
                print(f"FIXED {fixed}")
            if path.stem not in existing_topics:
                fixed = fix_missing_index_row(path, root)
                if fixed:
                    print(f"FIXED {fixed}")
                    existing_topics.add(path.stem)

    ids = known_ids(root)
    manifest = manifest_rows(root)
    existing_topics = set(index_rows(root).keys())

    all_errors, all_warnings = [], []
    for path in paths:
        errors, warnings = lint_page(path, root, ids, manifest, existing_topics)
        all_errors += errors
        all_warnings += warnings

    for warning in all_warnings:
        print(f"WARN  {warning}")
    if all_errors:
        for error in all_errors:
            print(f"ERROR {error}")
        sys.exit(1)
    print(f"{len(paths)} wiki page(s) valid ({len(all_warnings)} warning(s)).")


if __name__ == "__main__":
    main()
