# Codebeamer — Re-import Checklist

Before handing generated requirements back for Codebeamer import:

- [ ] Every item is a canonical YAML block (locked schema) + SHALL text
- [ ] `commands/sys3/validate-schema.sh <file>` passes with zero errors
- [ ] IDs generated with `scripts/generate-req-id.py` (no collisions with imports)
- [ ] Status is `Draft` for new items — never pre-set `Approved`
- [ ] `source` entries reference existing upstream items (check latest CB import)
- [ ] `allocates_to` values are valid SA8620P targets within their ASIL ceiling
- [ ] Formatted via `commands/sys3/cb-export.sh` / `scripts/cb-formatter.py`
- [ ] Field names match the tracker's field IDs (`codebeamer-format.instructions.md`)
- [ ] Changed existing items are listed separately from new items in the handover note
