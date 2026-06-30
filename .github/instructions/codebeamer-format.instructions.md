---
name: Codebeamer Format
description: "Use when: formatting requirements for Codebeamer import, mapping YAML fields to CB fields, or validating CB field completeness"
applyTo: ["**/requirements/**", "**/*codebeamer*", "**/*CB*"]
---

# Codebeamer ALM — SYS.3 Field Mapping

## YAML → Codebeamer Field Mapping

| YAML field | Codebeamer field | Type | Required |
|------------|-----------------|------|----------|
| `id` | Summary / Requirement ID | Text | Yes |
| `level` | Requirement Type | List | Yes |
| `asil` | ASIL | List (QM/A/B/C/D) | Yes |
| `source` | Upstream Trace | Tracker reference | Yes |
| `verification` | Verification Method | List | Yes |
| `verification_criteria` | Verification Criteria | Text area | Yes |
| `rationale` | Rationale | Text area | Recommended |
| `references` | References | Text (multi-line) | Recommended |
| `safety_mechanism` | Safety Mechanism | Text area | Required (ASIL≥A) |
| `refines` | Derived From | Tracker reference | If applicable |
| `allocates_to` | Allocated To (HW/SW) | Text | Yes (ASIL≥B) |
| `tags` | Tags / Labels | Multi-select | Optional |
| requirement text | Description | Rich text | Yes |

## Codebeamer Import Format

TODO: Add actual CB project field IDs and CSV/import template when project is set up.

```
# Placeholder — replace with actual Codebeamer project import format
# Format: CSV or REST API POST to /api/v3/trackers/{trackerId}/items
```

## Mandatory Fields (Codebeamer SYS.3 tracker)

1. Summary (= requirement ID + title)
2. Description (= requirement SHALL statement)
3. ASIL
4. Verification Method
5. Verification Criteria
6. Status (`Draft` | `In Review` | `Approved` | `Baselined`)
7. Allocated To

## Status Workflow

```
Draft → In Review → Approved → Baselined
```

Requirements must reach `Approved` before SWE.1 decomposition begins.

## Notes

- TODO: Add CB tracker ID for SYS.3 requirements
- TODO: Add CB project URL
- TODO: Confirm CSV import field order with CB administrator
