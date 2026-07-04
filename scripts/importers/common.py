"""
Shared helpers for the offline export importers (Codebeamer / JIRA / Confluence).

Normalized output convention:
- One markdown file per processed export: imports/normalized/{tool}/{YYYY-MM-DD}-{tool}-{slug}.md
- Files start with an H1 + a metadata table — NOT YAML frontmatter, so that
  scripts/validate-requirements.py --all only ever sees canonical requirement
  YAML blocks (emitted by the Codebeamer importer) and nothing else.
- Every run appends a row to imports/normalized/manifest.md
"""

import hashlib
import re
from datetime import date, datetime
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def normalized_dir(tool: str) -> Path:
    d = repo_root() / "imports" / "normalized" / tool
    d.mkdir(parents=True, exist_ok=True)
    return d


def archive_dir() -> Path:
    d = repo_root() / "imports" / "archive"
    d.mkdir(parents=True, exist_ok=True)
    return d


def slugify(text: str, max_len: int = 48) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or "export"


def output_path(tool: str, source_name: str) -> Path:
    stamp = date.today().isoformat()
    return normalized_dir(tool) / f"{stamp}-{tool}-{slugify(Path(source_name).stem)}.md"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    def clean(cell: object) -> str:
        return str(cell if cell is not None else "").replace("|", "\\|").replace("\n", " ").strip()

    lines = [
        "| " + " | ".join(clean(h) for h in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines += ["| " + " | ".join(clean(c) for c in row) + " |" for row in rows]
    return "\n".join(lines)


def file_header(title: str, tool: str, source: Path, item_count: int) -> str:
    meta = md_table(
        ["Field", "Value"],
        [
            ["Tool", tool],
            ["Source export", source.name],
            ["Imported", datetime.now().strftime("%Y-%m-%d %H:%M")],
            ["Items", str(item_count)],
            ["Source SHA-256", sha256(source)[:16]],
        ],
    )
    return f"# {title}\n\n{meta}\n"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_manifest(tool: str, source: Path, out_file: Path, item_count: int) -> None:
    manifest = repo_root() / "imports" / "normalized" / "manifest.md"
    if not manifest.exists():
        manifest.write_text(
            "# Import Manifest\n\n"
            "One row per processed export. Raw files live in `imports/archive/` (gitignored).\n\n"
            "| Imported | Tool | Source export | Items | Normalized file | Source SHA-256 |\n"
            "| --- | --- | --- | --- | --- | --- |\n",
            encoding="utf-8",
        )
    row = (
        f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} | {tool} | {source.name} "
        f"| {item_count} | `{out_file.relative_to(repo_root())}` | `{sha256(source)[:16]}` |\n"
    )
    with manifest.open("a", encoding="utf-8") as f:
        f.write(row)


def norm_key(header: str) -> str:
    """Normalize a column header for tolerant matching: 'Issue key' -> 'issuekey'."""
    return re.sub(r"[^a-z0-9]", "", header.lower())
