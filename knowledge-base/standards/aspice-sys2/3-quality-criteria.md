# ASPICE SYS.2 — Quality Criteria

Review checklist for SYS.2 items (applied by @requirements-reviewer in addition to
the generic scorecard).

## Item-level criteria

- [ ] Solution-free: no component names, allocation targets, protocols, or vendor
      parts unless the stakeholder genuinely constrains them
- [ ] Stated at the system boundary (actors: driver, environment, other vehicles,
      backend — not internal elements)
- [ ] Atomic, single SHALL, quantified with units (language rules unchanged)
- [ ] `source:` reaches STK-* / CON-* / standard — never only another SYS item
- [ ] Verifiable at system or vehicle level; criteria carry units and conditions
- [ ] ASIL assigned from the hazard analysis (or QM with rationale)

## Set-level criteria

- [ ] Coverage: every stakeholder requirement in scope is refined or explicitly deferred
- [ ] No contradictions within the set (esp. timing budgets vs. feature expectations)
- [ ] Categorization tags present and consistent
- [ ] Downstream: every item is refined by ≥ 1 SYS.3 item or marked "direct-verify"

## Typical SYS.2 findings on this project

- Solution bias imported from platform knowledge ("on the SAIL", "via ara::com")
- Vehicle-level timing copied unchanged into SYS.3 without re-budgeting
- Safety requirements without a hazard/safety-goal source
- Stakeholder wishes ("comfortable", "quickly") passed through unquantified
