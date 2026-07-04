# JIRA import — jira-issues

| Field | Value |
| --- | --- |
| Tool | jira |
| Source export | jira-issues.csv |
| Imported | 2026-07-04 19:46 |
| Items | 5 |
| Source SHA-256 | bfac1fbcee64310f |

## ADAS-101 — gPTP offset spikes to 8 µs after switch reset

| Field | Value |
| --- | --- |
| Type | Bug |
| Status | In Progress |
| Priority | P1 |
| Assignee | rajesh |
| Reporter | skumar |
| Components | TimeSync |
| Affects versions | SW-B03 |
| Labels | gptp, timing |
| Created | 2026-06-20 10:02 |
| Updated | 2026-07-01 16:44 |
| Links | Blocks (outward): ADAS-140 |

### Observed
After a commanded reset of the 88Q5050, offset to GM spikes to 8 µs for ~2 s.

### Expected
Offset stays ≤ 1 µs (3σ) per SYS-GPTP-001.

### Notes
- Reproducible on bench B2
- `tsyncd` logs show BMCA re-run
```
[ts] offset=8123ns state=UNCERTAIN
```

## ADAS-102 — HTP orchestrator misses deadline signal under thermal throttling

| Field | Value |
| --- | --- |
| Type | Bug |
| Status | Open |
| Priority | P1 |
| Assignee | mfischer |
| Reporter | rajesh |
| Components | Perception |
| Affects versions | SW-B03 |
| Labels | htp, deadline |
| Created | 2026-06-22 08:15 |
| Updated | 2026-06-29 11:20 |
| Links | Blocks (inward): ADAS-101 |

### Observed
At Tj > 95 °C the deadline violation signal arrives 40 ms late.

### Impact
Violates SYS-HTP-001 (≤ 5 ms).

## ADAS-103 — Export SYS.3 gPTP tracker for offline review

| Field | Value |
| --- | --- |
| Type | Task |
| Status | Done |
| Priority | P3 |
| Assignee | rajesh |
| Reporter | rajesh |
| Components | TimeSync |
| Labels | codebeamer |
| Created | 2026-06-25 13:00 |
| Updated | 2026-06-26 09:30 |

Weekly Codebeamer CSV export of the gPTP requirements tracker for the offline agent workflow.

## ADAS-104 — SafeRTOS heartbeat DTC not latched after PMIC brown-out

| Field | Value |
| --- | --- |
| Type | Bug |
| Status | In Review |
| Priority | P2 |
| Assignee | akram |
| Reporter | skumar |
| Components | Safety |
| Affects versions | SW-B02 |
| Labels | sail, pmic |
| Created | 2026-06-27 15:48 |
| Updated | 2026-07-02 10:05 |
| Links | Blocks (outward): ADAS-101 |

### Observed
Brown-out on Intel PMIC rail VDD_SAIL causes heartbeat gap but DTC_SAIL_HB_LOSS is not latched.

### Suspected
Latch window (100 ms) shorter than PMIC recovery ramp (140 ms).

## ADAS-105 — Define degradation ladder for camera time-base uncertainty

| Field | Value |
| --- | --- |
| Type | Story |
| Status | Open |
| Priority | P2 |
| Assignee | rajesh |
| Reporter | pmeier |
| Components | TimeSync |
| Labels | concept, degradation |
| Created | 2026-06-30 09:12 |
| Updated | 2026-07-03 17:26 |

As a fusion consumer I need a defined degradation ladder (kSynchronized -> kUncertain -> kUnavailable) so that ADAS features shed load predictably.

#### Acceptance criteria
1. Ladder documented as operating concept
1. States mapped to ara::tsync status API
1. Reviewed by safety
