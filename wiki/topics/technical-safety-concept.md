# Technical Safety Concept — Wiki

Area: TSC | Status: Active | Last updated: 2026-07-05

## Current State

- Open bug: the SafeRTOS heartbeat DTC (`DTC_SAIL_HB_LOSS`) is not latched after an
  Intel PMIC brown-out on rail `VDD_SAIL` — suspected cause: the latch window
  (100 ms) is shorter than the PMIC recovery ramp (140 ms) (ADAS-104, In Review).

## Open Questions

- Should the DTC latch window be widened to exceed the 140 ms PMIC recovery ramp, or
  should the recovery ramp itself be bounded tighter? No SYS-TSC/TSR requirement
  currently governs this case — candidate for a new requirement once resolved.
  (raised 2026-06-27, unresolved)
- Related: the same brown-out event also surfaced a diagnostics gap (freeze-frame
  snapshot missing from the UDS DTC report) — see `wiki/topics/diagnostics.md`
  (ADAS-106). Resolving the latch-window question first may inform what the
  snapshot needs to capture.

## Decisions

- No ADRs filed for this topic yet.

## Cross-References

- JIRA: ADAS-104, ADAS-106
- Source imports: `imports/normalized/jira/2026-07-04-jira-jira-issues.md`,
  `imports/normalized/jira/2026-07-05-jira-jira-issues-followup.md`

## History

- 2026-07-05: page created (demo/backfill) from JIRA batch 2026-07-04 — filed
  ADAS-104 (SafeRTOS DTC latch bug) as an open safety question. No Codebeamer or
  Confluence content available yet for this topic in the sample fixtures.
- 2026-07-05: cross-referenced the new `diagnostics.md` topic (ADAS-106, JIRA batch
  2026-07-05) — same brown-out event, different open question.
