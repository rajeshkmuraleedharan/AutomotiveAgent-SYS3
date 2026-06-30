# Codebeamer ALM Rules

Rules for Codebeamer field compliance on the SYS.3 tracker.

## Mandatory Fields (all requirements)

1. `Summary` — requirement ID + title (e.g., `SYS-GPTP-001 — Time-base accuracy to grandmaster`)
2. `Description` — SHALL statement (plain text, no YAML)
3. `ASIL` — QM | A | B | C | D
4. `Verification Method` — TEST | ANALYSIS | INSPECTION | DEMONSTRATION
5. `Verification Criteria` — measurable criterion
6. `Status` — Draft | In Review | Approved | Baselined
7. `Allocated To` — SA8620P element (e.g., `QNX:KryoP0`)

## Conditional Mandatory Fields

| Condition | Required field |
|-----------|---------------|
| ASIL ≥ A | Safety Mechanism |
| ASIL ≥ B | Rationale |
| Derived from another req | Derived From (upstream trace) |
| Has downstream SWE.1 | Refined By (downstream trace) |

## Forbidden Patterns

- Do NOT enter YAML blocks in the `Description` field — YAML goes in the attribute block only
- Do NOT leave `Status = Draft` after design review sign-off
- Do NOT change `Summary` (ID) after `Approved` — raise a change request instead
- Do NOT duplicate requirements across trackers — use trace links

## Status Workflow

```
Draft → In Review → Approved → Baselined
```

- Baselining requires: ASIL, Verification Method, Verification Criteria, Allocated To, and at least one upstream trace
- Requirements in `Baselined` status require a formal change request to modify

## TODO

- [ ] Add CB tracker URL
- [ ] Add CB project ID for SYS.3 tracker
- [ ] Add CB field IDs for custom fields (ASIL, Safety Mechanism, etc.)
- [ ] Confirm CSV import column order with CB admin
