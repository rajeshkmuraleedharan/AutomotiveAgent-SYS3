# ADAS Platform — Static Structure

Reference static decomposition (adjust AREA scope per feature; keep diagrams ≤ 12 elements).

## Reference view: TimeSync subsystem

```mermaid
graph TD
  subgraph QNX["QNX 8.0 (ASIL-B)"]
    GM["ARC-GPTP-001<br>TimeBase Provider [B]"]
    ST["ARC-GPTP-002<br>TimeBase Status Service [B]"]
  end
  subgraph HW["Network HW"]
    SW["ARC-GPTP-004<br>TSN Switch Config [–]"]
  end
  subgraph SAIL["SAIL (ASIL-D)"]
    MON["ARC-GPTP-003<br>Sync Health Monitor [D→B decomp]"]
  end
  GM -->|"TimeBaseStatusService (ara::com)"| ST
  GM -->|"PTP HW timestamps"| SW
  GM -.->|"heartbeat (raw SPI)"| MON
```

Caption: static decomposition, concern = trustworthy platform time base,
addresses SYS-GPTP-001/002.

## Structural rules of thumb

- One component = one ASIL + one allocation target; split mixed elements
- Supervision components live on SAIL; supervised producers on QNX
- HW configuration (switch schedules, PHY setup) is modelled as elements too —
  they carry requirements and need verification
- Cross-domain edges are always raw-protocol interface elements, drawn dashed

## Where the real content goes

As features are worked, their static views land here (or in feature-specific
`*.architecture.md` files) after passing `commands/arch/validate-arch.sh`.
