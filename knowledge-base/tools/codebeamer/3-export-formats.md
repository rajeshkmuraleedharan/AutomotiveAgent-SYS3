# Codebeamer — Export Formats

How to produce exports the importer understands (`scripts/importers/codebeamer.py`).

## Recommended: tracker CSV/Excel export

1. Open the requirements tracker → table view
2. Configure columns: Id, Name, Description, ASIL, Source, Verification,
   Verification Criteria, Rationale, References, Safety Mechanism, Allocates To,
   Status, Assigned To, Modified At, Tags
3. Export → CSV (UTF-8) or Excel → drop into `imports/inbox/`

## Word export (fallback)

Table-based Word exports work if the table's first row is the header row.
Narrative Word exports (one section per item) are NOT parsed — use CSV/Excel.

## Column mapping

Authoritative mapping: `.github/instructions/tool-export-formats.instructions.md`.
Unknown columns are dropped; extend `FIELD_MAP` to keep them.

## Sample

`imports/samples/codebeamer-requirements.csv` — synthetic 3-item export used as the
regression fixture; its normalized output must always pass `validate-requirements.py`.
