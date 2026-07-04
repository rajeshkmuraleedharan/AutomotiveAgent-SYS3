# Import Rules

Rules for the offline export workflow (`imports/`).

## Directory Contract

| Directory | Who writes | Committed | Rule |
|-----------|-----------|-----------|------|
| `imports/inbox/` | Rajesh (raw exports) | never (gitignored) | write-only drop zone |
| `imports/normalized/` | normalizer script only | yes, if sanitized | the ONLY import content the agent reads |
| `imports/archive/` | normalizer script only | never (gitignored) | raw files are archived, not deleted |
| `imports/samples/` | maintained fixtures | yes | synthetic data only |

## Processing Rules

- Raw exports are never read directly by the agent — always via `scripts/normalize-imports.py`
- Every processed file gets a manifest row (`imports/normalized/manifest.md`) with source hash
- Detection failures are fixed with `--tool`, not by hand-editing raw exports
- Normalized files are regenerated, never hand-edited — corrections go into the
  importer (`FIELD_MAP`) or the source tracker

## Sanitization Rules (before committing `imports/normalized/`)

- No customer or OEM program names
- No unreleased part numbers beyond those already in `vendor-references.instructions.md`
- No personal data beyond internal short names already used in the repo
- When in doubt: keep the normalized file local (don't commit) — the workflow works either way

## Content Rules

- Codebeamer requirement imports must carry canonical YAML blocks; validation gaps are
  reported as tracker findings, never silently "fixed" during import
- Requirement IDs from imports are authoritative — the agent never renumbers imported IDs
