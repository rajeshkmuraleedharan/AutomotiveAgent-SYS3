# Codebeamer — Tracker Workflows

Default requirement workflow assumed by the agent (adjust to the internal tracker config):

```
Draft → In Review → Approved → Implemented → Verified
              ↓
          Rejected / [RETIRED]
```

## Rules the agent must respect

- `id` is immutable once status ≥ `Approved`; changes require a new derived requirement
  (`refines:` the approved one)
- Retired requirements keep their ID with `[RETIRED]` marker — IDs are never reused
- Review findings are resolved in `In Review`, not by editing `Approved` items
- Suspect links: when an upstream `source` item changes, downstream items become suspect —
  imports that show a changed upstream item should trigger a review proposal

## Internal specifics (fill in)

- Actual state names: `[TBD]`
- Roles/permissions relevant to Rajesh: `[TBD]`
- Baseline/release tagging convention: `[TBD]`
