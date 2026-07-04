"""
JIRA export importer: CSV / XLSX -> normalized markdown.

Handles the standard JIRA "Export -> CSV (all fields)" layout, including its
repeated-column quirk (multiple `Labels`, `Comment`, and issue-link columns
share the same header — values are collected into lists, not overwritten).
JIRA wiki markup in descriptions is converted to basic markdown.

Output: one markdown file per export, one `## KEY — Summary` section per issue
with a metadata table and the converted description. No YAML blocks are
emitted, so validate-requirements.py never trips over JIRA content.
"""

import csv
import re
from pathlib import Path

from . import common

META_COLUMNS = [
    ("issuetype", "Type"),
    ("status", "Status"),
    ("priority", "Priority"),
    ("assignee", "Assignee"),
    ("reporter", "Reporter"),
    ("components", "Components"),
    ("affectsversions", "Affects versions"),
    ("fixversions", "Fix versions"),
    ("labels", "Labels"),
    ("created", "Created"),
    ("updated", "Updated"),
]

LINK_HEADER = re.compile(r"(inward|outward) issue link \((.+)\)", re.I)


def _read_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            headers = next(reader)
            return headers, [row for row in reader if any(cell.strip() for cell in row)]
    if path.suffix.lower() == ".xlsx":
        import openpyxl  # pip install openpyxl

        ws = openpyxl.load_workbook(path, read_only=True, data_only=True).active
        rows_iter = ws.iter_rows(values_only=True)
        headers = [str(h) if h is not None else "" for h in next(rows_iter)]
        rows = [
            ["" if c is None else str(c) for c in row]
            for row in rows_iter
            if any(c is not None and str(c).strip() for c in row)
        ]
        return headers, rows
    raise ValueError(f"Unsupported JIRA export format: {path.name}")


def _collect(headers: list[str], row: list[str]) -> dict[str, list[str]]:
    """Group values by header, preserving repeated columns as lists."""
    issue: dict[str, list[str]] = {}
    for header, value in zip(headers, row):
        value = value.strip()
        if not value:
            continue
        issue.setdefault(header.strip(), []).append(value)
    return issue


def wiki_to_md(text: str) -> str:
    """Convert the most common JIRA wiki markup constructs to markdown."""
    text = re.sub(r"^h([1-6])\.\s*", lambda m: "#" * int(m.group(1)) + " ", text, flags=re.M)
    text = re.sub(r"\{code(?::[^}]*)?\}", "```", text)
    text = re.sub(r"\{noformat\}", "```", text)
    text = re.sub(r"\{\{(.+?)\}\}", r"`\1`", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"**\1**", text)  # *bold* -> **bold**
    text = re.sub(r"^\#\s+", "1. ", text, flags=re.M)  # numbered list
    text = re.sub(r"^\*\*\s+", "  - ", text, flags=re.M)  # nested bullet
    text = re.sub(r"^\*\s+", "- ", text, flags=re.M)  # bullet
    text = re.sub(r"\[([^|\]]+)\|([^\]]+)\]", r"[\1](\2)", text)  # [text|url]
    return text


def _first(issue: dict[str, list[str]], name: str) -> str:
    for header, values in issue.items():
        if common.norm_key(header) == name:
            return values[0]
    return ""


def _all(issue: dict[str, list[str]], name: str) -> list[str]:
    collected: list[str] = []
    for header, values in issue.items():
        if common.norm_key(header) == name:
            collected.extend(values)
    return collected


def _links(issue: dict[str, list[str]]) -> list[str]:
    links = []
    for header, values in issue.items():
        match = LINK_HEADER.match(header.strip())
        if match:
            direction, kind = match.groups()
            links += [f"{kind} ({direction.lower()}): {v}" for v in values]
    return links


def _issue_section(issue: dict[str, list[str]]) -> str:
    key = _first(issue, "issuekey") or "UNKNOWN"
    summary = _first(issue, "summary")
    rows = []
    for norm_name, label in META_COLUMNS:
        values = _all(issue, norm_name)
        if values:
            rows.append([label, ", ".join(dict.fromkeys(values))])
    links = _links(issue)
    if links:
        rows.append(["Links", "; ".join(links)])
    table = common.md_table(["Field", "Value"], rows)

    description = _first(issue, "description")
    if description:
        md = wiki_to_md(description)
        # demote description headings below the per-issue `## KEY` level
        md = re.sub(r"^(#{1,5}) ", r"#\1 ", md, flags=re.M)
        body = f"\n\n{md}"
    else:
        body = ""
    return f"## {key} — {summary}\n\n{table}{body}\n"


def import_file(path: Path) -> tuple[Path, str, int]:
    """Parse a JIRA export; return (output path, rendered markdown, issue count)."""
    headers, rows = _read_rows(path)
    issues = [_collect(headers, row) for row in rows]
    issues = [i for i in issues if _first(i, "issuekey")]

    sections = [_issue_section(issue) for issue in issues]
    out_path = common.output_path("jira", path.name)
    header = common.file_header(f"JIRA import — {path.stem}", "jira", path, len(issues))
    return out_path, header + "\n" + "\n".join(sections), len(issues)
