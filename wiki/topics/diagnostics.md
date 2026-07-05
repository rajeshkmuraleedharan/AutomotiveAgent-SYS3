# Diagnostics — Wiki

Area: DIAG | Status: Active | Last updated: 2026-07-05

## Current State

- Open bug: when `DTC_SAIL_HB_LOSS` is set, the UDS `ReadDTCInformation` response
  omits the freeze-frame snapshot (should include PMIC rail voltage + heartbeat gap
  duration per the diagnostic concept) — field technicians can't see the PMIC
  brown-out context without also pulling raw SafeRTOS logs (ADAS-106, Open).

## Open Questions

- Should the freeze-frame snapshot format for `DTC_SAIL_HB_LOSS` be specified as a
  new requirement (linking to the existing PMIC brown-out latch-window question on
  `wiki/topics/technical-safety-concept.md`, ADAS-104), or is this purely a
  diagnostics/UDS implementation gap with no new SYS-* requirement needed? (raised
  2026-07-06, unresolved)

## Decisions

- No ADRs filed for this topic yet.

## Cross-References

- JIRA: ADAS-106
- Source imports: `imports/normalized/jira/2026-07-05-jira-jira-issues-followup.md`

## History

- 2026-07-05: page created — this topic didn't exist before; JIRA Component
  "Diagnostics" (ADAS-106) had no matching AREA/topic, so a new page was created per
  `rules/wiki-rules.md`'s granularity rule (new topic on first reference, never
  pre-emptively). Cross-referenced against the related PMIC/SAIL bug already on
  `technical-safety-concept.md` (ADAS-104) since both concern the same brown-out event.
