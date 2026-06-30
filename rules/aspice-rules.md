# ASPICE SYS.3 Rules

ASPICE v3.1 compliance rules for the SYS.3 System Architectural Design process.

## SYS.3 Work Products

| Work Product | ID | Required content |
|-------------|----|-----------------|
| System Architectural Design | WP-SYS3-001 | System structure, interfaces, allocated requirements |
| System Architectural Design Evaluation | WP-SYS3-002 | Review record, traceability, consistency check |
| Allocated Requirements | WP-SYS3-003 | Bidirectional trace: SYS.1 ↔ SYS.3 ↔ SWE.1 |

## Requirement Quality Criteria (ASPICE SYS.3.BP2)

| Criterion | Description |
|-----------|-------------|
| Complete | All SYS.1 stakeholder requirements are addressed |
| Consistent | No conflicting requirements in the same baseline |
| Verifiable | Each requirement has measurable verification criteria |
| Unambiguous | Only one valid interpretation |
| Atomic | One testable behaviour per requirement |
| Traceable | Bidirectional trace to upstream and downstream |
| Feasible | Implementable with SA8620P platform constraints |

## Traceability Rules

- Every SYS.3 requirement must trace UP to at least one SYS.1 or stakeholder requirement
- Every SYS.3 requirement must trace DOWN to at least one SWE.1 requirement (before SWE.1 baseline)
- Trace gaps must be documented as open items with owner and due date

## Change Management Rules

- Requirements in `Approved` or `Baselined` status require a change request (CR) to modify
- CR must assess: safety impact, ASIL change, downstream SWE.1 impact
- Changed requirements must be re-reviewed before re-approval

## Review Checklist (before Approved)

- [ ] Atomic (one SHALL)
- [ ] Unambiguous (no weak verbs)
- [ ] Quantified verification criteria with units
- [ ] ASIL assigned and justified
- [ ] Safety mechanism specified (ASIL ≥ A)
- [ ] allocates_to valid SA8620P target
- [ ] Upstream trace to stakeholder requirement or standard
- [ ] Codebeamer mandatory fields complete
- [ ] Reviewed by SYS.3 lead and safety manager (ASIL ≥ B)
