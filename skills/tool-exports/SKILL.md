# Skill — Offline Tool Exports (Codebeamer / JIRA / Confluence)

Skill for working with manual exports from the internal ALM/collaboration tools.
There is **no API access** — all tool state enters the repo as files.

## Workflow

1. Rajesh drops raw exports into `imports/inbox/` (Word/Excel/CSV/HTML)
2. Run `commands/import/normalize-exports.sh` (or `/import-normalize`)
3. Agent reads ONLY `imports/normalized/{tool}/*.md` — never raw binary exports
4. Raw files are moved to `imports/archive/` (gitignored); `imports/normalized/manifest.md` logs every run

## Export formats per tool

| Tool | How to export | Formats | Detection |
|------|---------------|---------|-----------|
| Codebeamer | Tracker → Export → Excel/CSV/Word | `.csv` `.xlsx` `.docx` (tables) | header has `Id`/`Tracker`, no `Issue key` |
| JIRA | Issue search → Export → CSV (all fields) | `.csv` `.xlsx` | header has `Issue key` |
| Confluence | Page → ••• → Export → Word or HTML | `.docx` `.html` | by extension |

PDF is not supported — re-export as Word or HTML.

## Normalized output

- Codebeamer requirement items → **canonical SYS.3 YAML blocks** (locked schema), so
  `scripts/validate-requirements.py` runs directly on imports; tool bookkeeping
  (tracker, status, assignee, item id) lives in the `cb_meta:` sub-map
- JIRA issues → `## KEY — Summary` sections with metadata table + description
  (wiki markup converted to markdown); no YAML blocks
- Confluence pages → one markdown file per page

## Tool workflow awareness (for re-importable output)

- **Codebeamer**: requirement IDs are immutable after `Approved`; never invent CB item
  ids; when drafting updates for re-import, keep the tracker's status vocabulary
  (`Draft → In Review → Approved`) and produce YAML via `scripts/cb-formatter.py` /
  `commands/sys3/cb-export.sh`
- **JIRA**: reference issues by key (`ADAS-NNN`); respect the lifecycle
  `Open → In Progress → In Review → Done`; proposed new tickets get `NEW-` placeholder
  keys and a summary ≤ 90 chars
- **Confluence**: proposed pages are drafted as markdown with an H1 title matching the
  intended page title, so they can be pasted into the editor

## Rules

- See `rules/import-rules.md`
- Field mapping reference: `.github/instructions/tool-export-formats.instructions.md`
- If a Codebeamer export column is not recognized, extend `FIELD_MAP` in
  `scripts/importers/codebeamer.py` AND document it in the instructions file
