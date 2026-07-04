# ASPICE SYS.2 — Work Products

| Work product | In this repo |
|--------------|--------------|
| System requirements specification | Canonical YAML blocks, `level: SYS.2`, in Codebeamer (offline via `imports/`) |
| Categorization | `tags:` (functional, safety, nonfunctional, regulatory) |
| Analysis results (feasibility, verifiability) | `rationale:` + `verification_criteria:` fields |
| Traceability records | `source:` (upstream STK-*/CON-*) + SYS.3 items citing SYS.2 IDs (downstream) |
| Communication/agreement record | CB status workflow (`Draft → In Review → Approved`) |

## Verification at SYS.2 level

- `verification:` commonly DEMONSTRATION or TEST at vehicle/system level
- Criteria still quantified with units — "system level" is not an excuse for vagueness
- ANALYSIS acceptable for regulatory/constraint items with the cited document

## Interfaces to other processes

- **SYS.1** stakeholder requirements: every SYS.2 item traces to ≥ 1 STK-*/CON-* source
- **SYS.3**: refinement — SYS.3 `source:` lists SYS.2 IDs; orphan SYS.3 items are findings
- **SUP.10** change management: SYS.2 changes propagate suspect links downstream (CB)
