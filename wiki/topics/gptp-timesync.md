# gPTP TimeSync — Wiki

Area: GPTP | Status: Active | Last updated: 2026-07-05

## Current State

- Time accuracy: offset to grandmaster shall be ≤ 1 µs (3σ) on all synchronized ports
  during nominal operation (SYS-GPTP-001, ASIL B, allocated QNX:KryoP0 + Hardware:88Q5050).
- Holdover: system shall enter holdover within 31.25 ms after 3 consecutive missed
  Sync messages and publish `kUncertain` (SYS-GPTP-002, ASIL B, allocated QNX:KryoP0).
- Holdover strategy decided: drift-compensated (rate ratio frozen at sync loss,
  applied by `tsyncd` on QNX:KryoP0); redundant grandmaster deferred as a later
  platform option. Holdover accuracy target: ≤ 5 µs drift over 2 s at 25 °C;
  `DTC_GPTP_SYNC_LOSS` raised within 250 ms (Confluence decision page, 2026-06-18).
- Resolved bug: after a commanded reset of the 88Q5050, offset to GM previously spiked
  to 8 µs for ~2 s — a BMCA re-run transient (ADAS-101, Resolved). Fix: a 500 ms
  BMCA settle/grace period after any commanded reset before offset is evaluated
  against the 1 µs (3σ) threshold; a genuine sync loss is still caught by the
  existing 250 ms `DTC_GPTP_SYNC_LOSS` path if sync doesn't recover within the grace
  window. Bench-verified: 50 repetitions, 0 false negatives on genuine sync loss.
  This closes the gap in SYS-GPTP-002's fault model that this page previously
  flagged as an Open Question — no new requirement was needed, since the fix is a
  design change (grace period) rather than a change to the requirement itself.

## Open Questions

- ADAS-105: a degradation ladder (`kSynchronized` → `kUncertain` → `kUnavailable`) for
  camera time-base uncertainty was requested as a Story (Component: TimeSync) with no
  owning SYS-* requirement or CON-* concept yet — candidate for `/concept-feature`.
  (raised 2026-06-30, unresolved)

## Decisions

- Holdover strategy (drift-compensated, over free-running oscillator and redundant-GM
  options) is recorded in the Confluence decision page (2026-06-18) but has not yet
  been promoted to a `project-context/decisions/` ADR — consider `/record-learning`.

## Cross-References

- Requirements: SYS-GPTP-001, SYS-GPTP-002
- JIRA: ADAS-101, ADAS-105
- Source imports: `imports/normalized/codebeamer/2026-07-04-codebeamer-codebeamer-requirements.md`,
  `imports/normalized/jira/2026-07-04-jira-jira-issues.md`,
  `imports/normalized/confluence/2026-07-04-confluence-confluence-page.md`,
  `imports/normalized/jira/2026-07-05-jira-jira-issues-followup.md`

## History

- 2026-07-05: page created (demo/backfill) from CB batch 2026-07-04, JIRA batch
  2026-07-04, and the Confluence holdover-decision page — filed SYS-GPTP-001,
  SYS-GPTP-002, ADAS-101 (BMCA transient bug), ADAS-105 (degradation-ladder story),
  and the holdover-strategy decision.
- 2026-07-05: ADAS-101 resolved (JIRA batch 2026-07-05, jira-issues-followup) — BMCA
  settle/grace-period fix; removed from Open Questions, folded resolution into
  Current State. Status label changed from "(demo)" to "Active" now that a real
  incremental update has been folded in.
