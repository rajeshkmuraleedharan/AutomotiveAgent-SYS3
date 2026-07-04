# Interface Bank — Reusable Service Definitions

Validator-clean, reusable service definitions. Copy, rename, and fill `0x[TBD]` IDs
from the internal registry.

### Service: TimeBaseStatusService

| Attribute | Value |
|-----------|-------|
| ARC element | ARC-GPTP-002 (interface), provided by ARC-GPTP-001 |
| Instance specifier | `TimeSync/TimeBaseProvider/TimeBaseStatusService` |
| Service ID (SOME/IP) | 0x[TBD] |
| Instance ID | 0x[TBD] |
| Version | 1.0 |
| ASIL | B |
| E2E profile | P04 (events) |

**Events**

| Event | Type | Cycle / trigger | E2E |
|-------|------|-----------------|-----|
| `TimeBaseStatusChanged` | enum TimeBaseStatus {kSynchronized, kUncertain, kUnavailable} | on change + 100 ms heartbeat | P04 |

**Fields**

| Field | Type | Notify | Get | Set |
|-------|------|--------|-----|-----|
| `HoldoverBudgetRemaining` | uint32 (ms) | yes | yes | no |

Deployment: VLAN [TBD], PCP 6, ~64 B payload, multicast.

### Service: HealthReportService

| Attribute | Value |
|-----------|-------|
| ARC element | [per feature — supervisor components require it] |
| Instance specifier | `Platform/HealthAggregator/HealthReportService` |
| Service ID (SOME/IP) | 0x[TBD] |
| Version | 1.0 |
| ASIL | B |
| E2E profile | P01 (method payloads) |

**Methods**

| Method | In | Out | Fire&Forget |
|--------|----|----|-------------|
| `ReportHealth` | componentId: uint16, state: enum {OK, DEGRADED, FAILED}, detail: uint32 | — | yes |

Deployment: VLAN [TBD], PCP 6, unicast to aggregator; aggregator forwards a
consolidated frame to SAIL over the raw cross-domain channel (not ara::com).
