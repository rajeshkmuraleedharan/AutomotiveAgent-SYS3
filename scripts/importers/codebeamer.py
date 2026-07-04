"""
Codebeamer export importer: CSV / XLSX / DOCX(table) -> normalized markdown.

Requirement items are emitted as canonical SYS.3 schema YAML blocks so that
scripts/validate-requirements.py runs directly on the normalized output.
Codebeamer bookkeeping fields (tracker, status, assignee, item id, dates) go
into a `cb_meta:` sub-map inside the block — the validator ignores extra keys,
and the locked schema fields stay clean.

Column headers differ per tracker configuration. FIELD_MAP below matches the
common export headers tolerantly (case/space-insensitive). Extend FIELD_MAP if
your tracker uses different labels; the mapping documentation lives in
.github/instructions/tool-export-formats.instructions.md.
"""

import csv
import re
from pathlib import Path

from . import common

# normalized header -> canonical schema field (None = keep in cb_meta)
FIELD_MAP = {
    "id": "cb_item_id",
    "itemid": "cb_item_id",
    "requirementid": "req_id",
    "reqid": "req_id",
    "name": "title",
    "summary": "title",
    "title": "title",
    "description": "text",
    "requirementtext": "text",
    "level": "level",
    "asil": "asil",
    "asillevel": "asil",
    "criticality": "asil",
    "source": "source",
    "upstreamtrace": "source",
    "tracesfrom": "source",
    "verification": "verification",
    "verificationmethod": "verification",
    "verificationcriteria": "verification_criteria",
    "acceptancecriteria": "verification_criteria",
    "rationale": "rationale",
    "references": "references",
    "referencedocuments": "references",
    "safetymechanism": "safety_mechanism",
    "refines": "refines",
    "parentrequirement": "refines",
    "allocatesto": "allocates_to",
    "allocation": "allocates_to",
    "tags": "tags",
    "labels": "tags",
    # cb_meta bookkeeping
    "tracker": "cb_tracker",
    "status": "cb_status",
    "assignedto": "cb_assignee",
    "assignee": "cb_assignee",
    "modifiedat": "cb_modified",
    "modified": "cb_modified",
    "submittedat": "cb_created",
    "createdat": "cb_created",
}

LIST_FIELDS = {"source", "references", "refines", "allocates_to", "tags"}
MULTILINE_FIELDS = {"verification_criteria", "rationale", "safety_mechanism"}
SYS_ID = re.compile(r"\bSYS-[A-Z]+-\d{3}\b")

# canonical emission order for the YAML attribute block
BLOCK_ORDER = [
    "id", "level", "asil", "source", "verification", "verification_criteria",
    "rationale", "references", "safety_mechanism", "refines", "allocates_to", "tags",
]


def _split_list(value: str) -> list[str]:
    return [p.strip() for p in re.split(r"[;\n]+", value) if p.strip()]


def _rows_from_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def _rows_from_xlsx(path: Path) -> list[dict]:
    import openpyxl  # pip install openpyxl

    ws = openpyxl.load_workbook(path, read_only=True, data_only=True).active
    rows_iter = ws.iter_rows(values_only=True)
    headers = [str(h) if h is not None else "" for h in next(rows_iter)]
    return [
        {h: ("" if c is None else str(c)) for h, c in zip(headers, row)}
        for row in rows_iter
        if any(c is not None and str(c).strip() for c in row)
    ]


def _rows_from_docx(path: Path) -> list[dict]:
    import docx  # pip install python-docx

    rows: list[dict] = []
    for table in docx.Document(str(path)).tables:
        if not table.rows:
            continue
        headers = [cell.text.strip() for cell in table.rows[0].cells]
        for row in table.rows[1:]:
            values = [cell.text.strip() for cell in row.cells]
            if any(values):
                rows.append(dict(zip(headers, values)))
    return rows


def _map_row(raw: dict) -> dict:
    item: dict = {"cb_meta": {}}
    for header, value in raw.items():
        if value is None or not str(value).strip():
            continue
        value = str(value).strip()
        field = FIELD_MAP.get(common.norm_key(header or ""))
        if field is None:
            continue
        if field.startswith("cb_") and field != "cb_meta":
            item["cb_meta"][field.removeprefix("cb_")] = value
        elif field in LIST_FIELDS:
            item[field] = _split_list(value)
        else:
            item[field] = value
    return item


def _requirement_id(item: dict) -> str:
    for candidate in (item.get("req_id", ""), item.get("title", ""), item.get("text", "")):
        match = SYS_ID.search(candidate)
        if match:
            return match.group(0)
    return f"CB-{item['cb_meta'].get('item_id', item['cb_meta'].get('tracker', 'ITEM'))}"


def _yaml_block(item: dict, req_id: str) -> str:
    lines = ["---"]
    values = dict(item)
    values["id"] = req_id
    values.setdefault("level", "SYS.3")
    for key in BLOCK_ORDER:
        value = values.get(key)
        if not value:
            continue
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines += [f"  - {v}" for v in value]
        elif key in MULTILINE_FIELDS or "\n" in str(value):
            lines.append(f"{key}: |")
            lines += [f"  {line}" for line in str(value).splitlines()]
        else:
            lines.append(f"{key}: {value}")
    meta = item.get("cb_meta") or {}
    if meta:
        lines.append("cb_meta:")
        lines += [f"  {k}: {v}" for k, v in sorted(meta.items())]
    lines.append("---")
    return "\n".join(lines)


def import_file(path: Path) -> tuple[Path, str, int]:
    """Parse a Codebeamer export; return (output path, rendered markdown, item count)."""
    suffix = path.suffix.lower()
    if suffix == ".csv":
        raw_rows = _rows_from_csv(path)
    elif suffix == ".xlsx":
        raw_rows = _rows_from_xlsx(path)
    elif suffix == ".docx":
        raw_rows = _rows_from_docx(path)
    else:
        raise ValueError(f"Unsupported Codebeamer export format: {path.name}")

    items = [m for m in (_map_row(r) for r in raw_rows) if m.get("title") or m.get("text")]

    sections = []
    for item in items:
        req_id = _requirement_id(item)
        title = SYS_ID.sub("", item.get("title", "")).strip(" —-–:")
        text = item.get("text", "").strip()
        body = f"**{req_id} — {title}**\n\n{text}" if title else text
        sections.append(f"{_yaml_block(item, req_id)}\n\n{body}\n")

    out_path = common.output_path("codebeamer", path.name)
    header = common.file_header(f"Codebeamer import — {path.stem}", "codebeamer", path, len(items))
    text = header + "\n" + "\n".join(sections)
    return out_path, text, len(items)
