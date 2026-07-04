# ara::com Services — Overview

Service-oriented communication knowledge for the performance domain (QNX + Vector
MICROSAR Adaptive). Canonical definition format:
`.github/instructions/ara-com-interfaces.instructions.md`.

## Where ara::com applies — and where not

| Path | Mechanism |
|------|-----------|
| Adaptive app ↔ Adaptive app (QNX) | ara::com service, SOME/IP binding |
| Adaptive app ↔ Hexagon/Adreno | FastRPC (modelled as internal interface) |
| QNX ↔ SAIL safety island | raw protocol (SPI/mailbox) — **never ara::com** |
| Time base distribution | ara::tsync (consumes gPTP) |

## Design defaults

- Proxy/skeleton per MICROSAR Adaptive; service discovery via SOME/IP-SD
- Events for state distribution, fields for slow-changing values with notify,
  methods only where request/response semantics are required
- E2E protection (P01/P04/P05 per data layout) mandatory for ASIL ≥ A data
- Instance specifiers follow `Machine/Process/ServiceInstance` convention
- Service versioning: major = breaking, minor = compatible additions

## Internal specifics (fill in)

- SOME/IP service-ID registry location: `[TBD]`
- E2E profile guideline document: `VEC-MSR-ADAPT-E2E §[TBD]`
- Deployment machine/process naming: `[TBD]`
