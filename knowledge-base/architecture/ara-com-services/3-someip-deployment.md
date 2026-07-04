# ara::com — SOME/IP Deployment on the TSN Network

Deployment knowledge for services crossing the Marvell 88Q5050 TSN switch.

## Per-service deployment notes (mandatory in every definition)

| Item | Why |
|------|-----|
| VLAN + PCP priority (802.1Q) | TSN scheduling class on the 88Q5050 |
| Cycle time / trigger | bandwidth + latency budget |
| Payload size estimate | switch queue dimensioning |
| Multicast vs unicast | SD configuration |

## Priority scheme (defaults — confirm against internal network spec `[TBD]`)

| Traffic | PCP |
|---------|-----|
| gPTP (802.1AS) | 7 (highest, per switch config) |
| Safety/health events | 6 |
| Control (SOME/IP methods) | 5 |
| Sensor/fusion data streams | 4 |
| Diagnostics, logging | 1–0 |

## Rules

- gPTP frames never share a queue with bulk data — switch schedule guarantees this
  (MRVL-88Q5050-DS §[TBD])
- SOME/IP-SD offer/find cycles kept out of the safety-relevant traffic classes
- Bandwidth estimates roll up per link; > 70 % utilization on any TSN class is a finding
- Service IDs / instance IDs from the internal registry only (`0x[TBD]` until assigned)
