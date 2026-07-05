# gPTP TimeSync — Wiki

Area: GPTP | Status: Active (seeded from sample fixtures — replace as real imports arrive) | Last updated: 2026-07-05

## Current State

- Time accuracy: offset to grandmaster shall be ≤ 1 µs (3σ) on all synchronized ports
  during nominal operation (SYS-GPTP-001, ASIL B, allocated QNX:KryoP0 + Hardware:88Q5050).
- Holdover: system shall enter holdover within 31.25 ms after 3 consecutive missed
  Sync messages and publish `kUncertain` (SYS-GPTP-002, ASIL B, allocated QNX:KryoP0).
- Holdover strategy decided: drift-compensated (rate ratio frozen at sync loss,
  applied by `tsyncd` on QNX:KryoP0); redundant grandmaster deferred as a later
  platform option. Holdover accuracy target: ≤ 5 µs drift over 2 s at 25 °C;
  `DTC_GPTP_SYNC_LOSS` raised within 250 ms (Confluence decision page, 2026-06-18).
- Open bug: after a commanded reset of the 88Q5050, offset to GM spikes to 8 µs for
  ~2 s — a BMCA re-run transient (ADAS-101, In Progress). This is a different failure
  mode than SYS-GPTP-002 covers (missed-sync holdover), so it is **not** currently
  addressed by an existing requirement's fault model.

## Open Questions

- Does SYS-GPTP-002 (or a new requirement) need to cover the post-reset BMCA re-run
  transient surfaced by ADAS-101? (raised 2026-06-20, unresolved as of the 2026-07-04 import)
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
  `imports/normalized/confluence/2026-07-04-confluence-confluence-page.md`

## History

- 2026-07-05: page created (demo/backfill) from CB batch 2026-07-04, JIRA batch
  2026-07-04, and the Confluence holdover-decision page — filed SYS-GPTP-001,
  SYS-GPTP-002, ADAS-101 (BMCA transient bug), ADAS-105 (degradation-ladder story),
  and the holdover-strategy decision.
