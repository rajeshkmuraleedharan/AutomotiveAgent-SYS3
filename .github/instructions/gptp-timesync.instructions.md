---
name: gPTP TimeSync — SA8620P
description: "Use when: writing SYS.3 requirements for gPTP, specifying timing accuracy, holdover, grandmaster selection, or Marvell TSN integration on SA8620P"
applyTo: ["**/gptp**", "**/timesync**", "**/tsync**", "**/*SYS-GPTP*"]
---

# gPTP TimeSync — SA8620P Platform

## Topic Scope (SYS.3)

gPTP synchronization requirements covering:
- Time accuracy to grandmaster (≤ 1 µs, 3σ)
- Holdover behaviour on sync loss
- Grandmaster selection / Best Master Clock Algorithm (BMCA)
- Marvell 88Q5050 hardware timestamping integration
- ara::tsync end-station configuration
- Status publication to consumers (sensor fusion EKF)

## SA8620P Architecture

```
[gPTP Grandmaster] ← IEEE 802.1AS-2020
        │ 100BASE-T1 / 1000BASE-T1
        ▼
Marvell 88Q5050 TSN Switch
        │ hardware timestamping (ns precision)
        ▼
Marvell 88Q22xx PHY
        │
SA8620P Ethernet MAC
        │
ara::tsync (Vector MICROSAR Adaptive, QNX Kryo P0)
        │
[Sensor Fusion EKF] ← time-base consumer (ASIL-B)
```

## Key Parameters

| Parameter | Value | Source |
|-----------|-------|--------|
| Sync accuracy target | ≤ 1 µs (3σ) | SYS-GPTP-003 |
| Sync interval | 125 ms (default) | IEEE 802.1AS-2020 §11.5 |
| Holdover threshold | ≥ 3 missed sync events | SYS-GPTP-TBD |
| Status on loss | kUncertain | ara::tsync |
| ASIL | B | allocated to QNX:KryoP0 |

## Requirement Areas

See `knowledge-base/features/gptp-timesync/` for deep reference and requirements bank.

1. Time accuracy — grandmaster offset ≤ 1 µs (3σ)
2. Holdover — kUncertain status after 3 missed syncs, EKF degraded mode
3. BMCA — grandmaster priority configuration, tie-breaking
4. Startup — gPTP synchronized before ADAS FunctionGroup starts
5. Monitoring — ara::phm / DTC_GPTP_SYNC_LOSS
6. Temperature — accuracy maintained at –40 °C to +85 °C

## Safety

- ASIL-B: gPTP time-base provider (ara::tsync on QNX:KryoP0)
- Safety mechanism: holdover monitor → kUncertain → EKF widens association gate
- DTC: `DTC_GPTP_SYNC_LOSS`, `DTC_GPTP_UNCERTAIN`
- Vendor refs: `MRVL-88Q5050-DS §4.2`, `VEC-MSR-ADAPT-TSYNC §2.3`
