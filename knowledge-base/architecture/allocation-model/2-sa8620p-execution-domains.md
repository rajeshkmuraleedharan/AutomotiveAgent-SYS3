# SA8620P Execution Domains

| Target | What runs there | Scheduling | ASIL ceiling | Typical use |
|--------|-----------------|------------|--------------|-------------|
| `QNX:KryoP0` / `QNX:KryoP1` | latency-critical Adaptive apps | QNX SCHED_FIFO | B | time base, fusion front-end |
| `QNX:KryoE<n>` | Adaptive service apps | ara::exec managed | B | supervisors, aggregators, managers |
| `QNX:Hexagon` | NN inference (SNPE/QNN DLCs) | FastRPC sessions | QM | perception models |
| `QNX:Adreno` | GPU compute/visualization | QNX | QM | pre/post-processing |
| `SAIL:SafeRTOS` | safety supervision, safe-state control | SafeRTOS static schedule | D | health monitor, watchdogs, degradation enforcement |
| `Hardware:88Q5050` | TSN switch config/schedules | — | — | gPTP transparent clock, traffic classes |
| `Hardware:88Q22xx` | PHY config | — | — | link diagnostics |
| `Hardware:PMIC` | power sequencing, brown-out behaviour | — | — | rail supervision requirements |

## Domain boundaries

- QNX ↔ SAIL: raw protocol (SPI/mailbox heartbeat + consolidated health frame)
- CPU ↔ Hexagon/Adreno: FastRPC; the calling ASIL-B side owns deadline supervision
- Everything ↔ network: through the 88Q5050 TSN classes (see ara-com-services/3)

## Placement heuristics

- Monitor on SAIL, producer on QNX; enforcement of safe state always reachable from SAIL
- Split "compute" (QM accelerator) from "supervise" (ASIL target) — bank example ARC-HTP-001
- PMIC/power requirements allocate to `Hardware:PMIC` + a SAIL supervision element pair
