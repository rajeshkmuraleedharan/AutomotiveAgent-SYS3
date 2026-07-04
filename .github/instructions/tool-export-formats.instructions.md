---
name: Tool Export Formats
description: "Use when: processing, reading, or generating content for Codebeamer, JIRA, or Confluence offline exports"
applyTo: ["imports/**", "scripts/importers/**", "scripts/normalize-imports.py"]
---

# Offline Tool Export Formats — Field Mapping Reference

Single source of truth for how export columns map to normalized markdown.
The executable copy of the Codebeamer map is `FIELD_MAP` in `scripts/importers/codebeamer.py` —
keep both in sync.

## Codebeamer (CSV / XLSX / DOCX tables)

Headers are matched case/space-insensitively.

| Export column | Normalized field | Notes |
|---------------|------------------|-------|
| `Id` / `Item ID` | `cb_meta.item_id` | CB-internal, never a requirement ID |
| `Requirement ID` / `Req ID` | canonical `id` | falls back to `SYS-…` pattern found in Name/Description |
| `Name` / `Summary` / `Title` | requirement title | emitted as `**{id} — {title}**` |
| `Description` / `Requirement Text` | requirement text | the SHALL statement |
| `Level` | `level` | defaults to `SYS.3` |
| `ASIL` / `Criticality` | `asil` | QM / A / B / C / D |
| `Source` / `Upstream Trace` / `Traces From` | `source` list | split on `;` or newline |
| `Verification` / `Verification Method` | `verification` | TEST / ANALYSIS / INSPECTION / DEMONSTRATION |
| `Verification Criteria` / `Acceptance Criteria` | `verification_criteria` | literal block |
| `Rationale` | `rationale` | literal block |
| `References` / `Reference Documents` | `references` list | split on `;` |
| `Safety Mechanism` | `safety_mechanism` | literal block |
| `Refines` / `Parent Requirement` | `refines` list | |
| `Allocates To` / `Allocation` | `allocates_to` list | must be valid SA8620P targets |
| `Tags` / `Labels` | `tags` list | |
| `Tracker`, `Status`, `Assigned To`, `Modified At`, `Submitted At` | `cb_meta.*` | bookkeeping only |

Unmapped columns are dropped (by design — extend `FIELD_MAP` to keep one).

## JIRA (CSV "all fields" / XLSX)

- `Issue key`, `Issue Type`, `Summary`, `Status`, `Priority`, `Assignee`, `Reporter`,
  `Components`, `Affects versions`, `Fix versions`, `Labels`, `Created`, `Updated`,
  `Description` → per-issue metadata table + body
- Repeated columns (`Labels`, link columns) are collected, not overwritten
- `Inward/Outward issue link (TYPE)` → `Links` row: `TYPE (direction): KEY`
- Description wiki markup converted: `h2.`→`##` (then demoted one level), `*bold*`,
  `{{monospace}}`, `{code}`/`{noformat}`→fenced blocks, `*`/`#` lists, `[text|url]`

## Confluence (HTML / DOCX)

- One markdown file per page; headings, lists, tables, code blocks, links preserved
- PDF exports are rejected — re-export as Word or HTML

## Generation rules (return trip)

- Requirements meant for Codebeamer re-import: canonical YAML blocks; format with
  `scripts/cb-formatter.py`; status values from the tracker workflow only
- Proposed JIRA tickets: `NEW-` key placeholder, summary ≤ 90 chars, wiki-markup body
- Proposed Confluence pages: markdown with H1 = page title
