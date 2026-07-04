# Confluence — Export Formats

How to produce exports the importer understands (`scripts/importers/confluence.py`).

## Export procedure

- Single page: ••• menu → Export → **Export to Word** (`.docx`) or **Export to HTML**
- HTML preserves structure best (tables, code blocks); Word is fine for text pages
- **PDF is rejected** by the importer — re-export as Word or HTML

## What survives conversion

| Element | HTML | DOCX |
|---------|------|------|
| Headings h1–h6 | ✓ | ✓ (Heading styles) |
| Bullet / numbered lists | ✓ (nested) | ✓ (flat) |
| Tables | ✓ | ✓ |
| Code blocks | ✓ | — (plain text) |
| Links | ✓ (`[text](url)`) | text only |
| Images, macros, attachments | dropped | dropped |

## Samples

- `imports/samples/confluence-page.html` — decision page fixture
- `imports/samples/confluence-htp-notes.docx` — Word export fixture
