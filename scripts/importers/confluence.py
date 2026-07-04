"""
Confluence export importer: HTML / DOCX -> normalized markdown.

Confluence pages are exported via "..." menu -> Export -> "Export to HTML" or
"Export to Word". PDF export is NOT supported — re-export as HTML or Word.

HTML is converted with a small stdlib html.parser subclass (headings, lists,
tables, code blocks, links, emphasis). DOCX is converted with python-docx,
preserving the paragraph/table order of the document body.
"""

import re
from html.parser import HTMLParser
from pathlib import Path

from . import common


class _HtmlToMd(HTMLParser):
    SKIP = {"script", "style", "head"}
    HEADINGS = {f"h{i}": "#" * i for i in range(1, 7)}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.list_stack: list[str] = []  # "ul" | "ol"
        self.in_cell = False
        self.in_pre = False
        self.skip_depth = 0
        self.row: list[str] = []
        self.table_rows: list[list[str]] = []
        self.href = ""

    def _emit(self, text: str) -> None:
        if self.in_cell:
            self.row[-1] += text
        else:
            self.out.append(text)

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip_depth += 1
            return
        if tag in self.HEADINGS:
            self._emit(f"\n\n{self.HEADINGS[tag]} ")
        elif tag == "p":
            self._emit("\n\n")
        elif tag == "br":
            self._emit("\n")
        elif tag in ("ul", "ol"):
            self.list_stack.append(tag)
        elif tag == "li":
            indent = "  " * (len(self.list_stack) - 1)
            marker = "1." if self.list_stack and self.list_stack[-1] == "ol" else "-"
            self._emit(f"\n{indent}{marker} ")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code" and not self.in_pre:
            self._emit("`")
        elif tag == "pre":
            self.in_pre = True
            self._emit("\n\n```\n")
        elif tag == "a":
            self.href = dict(attrs).get("href", "")
            self._emit("[")
        elif tag == "table":
            self.table_rows = []
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.row.append("")
            self.in_cell = True

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag in self.HEADINGS:
            self._emit("\n")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            self._emit("\n")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code" and not self.in_pre:
            self._emit("`")
        elif tag == "pre":
            self.in_pre = False
            self._emit("\n```\n")
        elif tag == "a":
            self._emit(f"]({self.href})" if self.href else "]")
            self.href = ""
        elif tag in ("td", "th"):
            self.in_cell = False
        elif tag == "tr" and self.row:
            self.table_rows.append(self.row)
        elif tag == "table" and self.table_rows:
            headers, *rows = self.table_rows
            self.out.append("\n\n" + common.md_table(headers, rows) + "\n")

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.in_pre:
            self._emit(data)
        else:
            self._emit(re.sub(r"\s+", " ", data))

    def markdown(self) -> str:
        text = "".join(self.out)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def _from_html(path: Path) -> str:
    parser = _HtmlToMd()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser.markdown()


def _from_docx(path: Path) -> str:
    import docx  # pip install python-docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph

    document = docx.Document(str(path))
    lines: list[str] = []
    for element in document.element.body:
        if element.tag.endswith("}p"):
            para = Paragraph(element, document)
            text = para.text.strip()
            if not text:
                continue
            style = (para.style.name or "") if para.style else ""
            match = re.match(r"Heading (\d)", style)
            if match:
                lines.append(f"\n{'#' * int(match.group(1))} {text}\n")
            elif "List Number" in style:
                lines.append(f"1. {text}")
            elif "List" in style:
                lines.append(f"- {text}")
            else:
                lines.append(f"{text}\n")
        elif element.tag.endswith("}tbl"):
            table = Table(element, document)
            cells = [[c.text.strip() for c in row.cells] for row in table.rows]
            if cells:
                headers, *rows = cells
                lines.append("\n" + common.md_table(headers, rows) + "\n")
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def import_file(path: Path) -> tuple[Path, str, int]:
    """Parse a Confluence export; return (output path, rendered markdown, page count)."""
    suffix = path.suffix.lower()
    if suffix in (".html", ".htm"):
        body = _from_html(path)
    elif suffix == ".docx":
        body = _from_docx(path)
    elif suffix == ".pdf":
        raise ValueError("PDF export not supported — re-export the page as HTML or Word")
    else:
        raise ValueError(f"Unsupported Confluence export format: {path.name}")

    out_path = common.output_path("confluence", path.name)
    header = common.file_header(f"Confluence import — {path.stem}", "confluence", path, 1)
    return out_path, f"{header}\n{body}\n", 1
