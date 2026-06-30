# Skill — Codebeamer ALM Integration

Skill for Codebeamer field mapping and import format for the SYS.3 tracker.

## Field Mapping

| YAML field | Codebeamer field | Notes |
|------------|-----------------|-------|
| `id` | Summary | Include title: `SYS-GPTP-001 — Title` |
| `level` | Requirement Type | Always `SYS.3` |
| `asil` | ASIL | QM \| A \| B \| C \| D |
| `source` | Upstream Trace | Tracker ref or free text |
| `verification` | Verification Method | TEST \| ANALYSIS \| INSPECTION |
| `verification_criteria` | Verification Criteria | Text area |
| `rationale` | Rationale | Text area |
| `references` | References | Multi-line text |
| `safety_mechanism` | Safety Mechanism | Text area |
| `allocates_to` | Allocated To | SA8620P element list |
| `tags` | Tags | Multi-select |
| requirement text | Description | Plain text (no YAML) |

## Status Lifecycle

```
Draft → In Review → Approved → Baselined
```

## Import Method

1. `python scripts/cb-formatter.py <file.md> --output cb-import.csv`
2. Codebeamer > Tracker > Import > CSV
3. Map columns to CB fields (see `docs/codebeamer-import-guide.md`)

## TODO

- [ ] Add CB project URL and tracker ID
- [ ] Confirm CSV column order with CB administrator
- [ ] Add REST API endpoint for programmatic import
