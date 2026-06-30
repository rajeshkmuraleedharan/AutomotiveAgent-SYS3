# Codebeamer Import Guide

How to import generated SYS.3 requirements into Codebeamer ALM.

## Prerequisites

- Codebeamer account with write access to the SYS.3 tracker
- Project URL: TODO
- SYS.3 tracker ID: TODO

## Method 1 — Manual Entry (Draft requirements)

1. Open the SYS.3 tracker in Codebeamer
2. Click `New Item`
3. Copy-paste from the generated YAML + text:
   - `id` → Summary field (prefix with title)
   - Requirement text → Description
   - `asil` → ASIL field
   - `verification` → Verification Method
   - `verification_criteria` → Verification Criteria
   - `safety_mechanism` → Safety Mechanism
   - `allocates_to` → Allocated To
4. Set Status to `Draft`
5. Add upstream trace in `Upstream Trace` field

## Method 2 — CSV Import (batch)

Use `scripts/cb-formatter.py` to convert YAML blocks to Codebeamer CSV format:

```bash
python scripts/cb-formatter.py requirements/gptp-reqs.md --output cb-import.csv
# Then import via Codebeamer > Tracker > Import > CSV
```

TODO: Add CB CSV column order when project is configured.

## Method 3 — REST API

```bash
# TODO: Add CB REST API endpoint when project is configured
# curl -X POST https://[CB-URL]/api/v3/trackers/[TRACKER-ID]/items \
#   -H "Authorization: Bearer [TOKEN]" \
#   -d @payload.json
```

## Status After Import

- All imported requirements start at `Draft`
- Move to `In Review` after self-review with `/req-review`
- `Approved` after design review sign-off
- `Baselined` after baseline cut — no changes without CR

## TODO

- [ ] Add Codebeamer project URL
- [ ] Add SYS.3 tracker ID
- [ ] Confirm CSV import column order
- [ ] Add REST API endpoint
- [ ] Add Bearer token handling (secrets manager reference)
