# JIRA import — jira-issues-followup

| Field | Value |
| --- | --- |
| Tool | jira |
| Source export | jira-issues-followup.csv |
| Imported | 2026-07-05 22:46 |
| Items | 2 |
| Source SHA-256 | ac46a3fca3b1e31a |

## ADAS-101 — gPTP offset spikes to 8 µs after switch reset

| Field | Value |
| --- | --- |
| Type | Bug |
| Status | Resolved |
| Priority | P1 |
| Assignee | rajesh |
| Reporter | skumar |
| Components | TimeSync |
| Affects versions | SW-B03 |
| Labels | gptp |
| Created | 2026-06-20 10:02 |
| Updated | 2026-07-08 11:30 |
| Links | Blocks (outward): ADAS-140 |

### Resolution
Added a 500 ms BMCA settle/grace period after any commanded 88Q5050 reset before offset is evaluated against the 1 µs (3σ) threshold; suppresses the transient without masking a genuine sync loss (still bounded by the existing 250 ms DTC_GPTP_SYNC_LOSS path if sync doesn't recover within the grace window).

### Verification
Bench-reproduced on B2 with the fault-injection switch, 50 repetitions, 0 false negatives on genuine sync loss.

## ADAS-106 — DTC snapshot not attached when DTC_SAIL_HB_LOSS is reported to the diagnostic tester

| Field | Value |
| --- | --- |
| Type | Bug |
| Status | Open |
| Priority | P2 |
| Assignee | akram |
| Reporter | rajesh |
| Components | Diagnostics |
| Affects versions | SW-B03 |
| Labels | uds |
| Created | 2026-07-06 09:15 |
| Updated | 2026-07-07 14:02 |

### Observed
When DTC_SAIL_HB_LOSS is set, the UDS ReadDTCInformation response omits the freeze-frame snapshot (should include PMIC rail voltage + heartbeat gap duration per the diagnostic concept).

### Impact
Field technicians cannot see the PMIC brown-out context that triggered the DTC without also pulling raw SafeRTOS logs.
