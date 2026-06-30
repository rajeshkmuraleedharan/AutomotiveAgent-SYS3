---
name: Vendor References Registry
description: "Use when: adding references to requirements, citing vendor safety manuals, or checking available document short-IDs"
applyTo: ["**"]
---

# Vendor Document Registry — SA8620P Platform

Use these short-IDs in `references:` YAML fields. Format: `SHORT-ID §section`.

## Qualcomm SA8620P

| Short-ID | Document | Notes |
|----------|----------|-------|
| `QC-SA8620P-SM` | Qualcomm SA8620P Safety Manual | PBIST/CBIST coverage, SPFM/LFM data |
| `QC-SA8620P-TRM` | SA8620P Technical Reference Manual | Register maps, clocking, power |
| `QC-SA8620P-HRM` | SA8620P Hardware Reference Manual | Pin descriptions, interfaces |
| `QC-HEXAGON-SM` | Hexagon DSP Safety Manual | HTP safety isolation, SMMU |

## QNX 8.0

| Short-ID | Document |
|----------|----------|
| `QNX8-SM` | QNX 8.0 Safety Manual |
| `QNX8-AA-REF` | QNX 8.0 Adaptive AUTOSAR Reference |

## SafeRTOS

| Short-ID | Document |
|----------|----------|
| `SRTOS-SM` | SafeRTOS Safety Manual |
| `SRTOS-USR` | SafeRTOS User Guide |

## Vector MICROSAR Adaptive

| Short-ID | Document |
|----------|----------|
| `VEC-MSR-ADAPT-COM` | ara::com Technical Reference |
| `VEC-MSR-ADAPT-EXEC` | ara::exec Technical Reference |
| `VEC-MSR-ADAPT-PHM` | ara::phm Technical Reference |
| `VEC-MSR-ADAPT-TSYNC` | ara::tsync Technical Reference |
| `VEC-MSR-ADAPT-DIAG` | ara::diag Technical Reference |
| `VEC-MSR-ADAPT-PER` | ara::per Technical Reference |
| `VEC-MSR-ADAPT-LOG` | ara::log Technical Reference |
| `VEC-DAVINCI-CFG-ADAPT` | DaVinci Configurator Adaptive Guide |

## Marvell Ethernet

| Short-ID | Document |
|----------|----------|
| `MRVL-88Q5050-DS` | Marvell 88Q5050 TSN Switch Datasheet |
| `MRVL-88Q22xx-DS` | Marvell 88Q22xx PHY Datasheet |
| `MRVL-TSN-SM` | Marvell TSN Safety Manual |

## Intel PMIC

| Short-ID | Document |
|----------|----------|
| `INTEL-PMIC-DS` | Intel PMIC Datasheet |
| `INTEL-PMIC-SM` | Intel PMIC Safety Manual |

## Open Items (TBD)

- [ ] Confirm Vector MICROSAR Adaptive release: R22-11 or R23-11
- [ ] Confirm Marvell switch exact part: 88Q5050 (placeholder)
- [ ] Confirm Marvell PHY exact part: 88Q22xx (placeholder)
- [ ] Confirm Intel PMIC part number
- [ ] Add vendor doc storage path (network drive / SharePoint)
- [ ] Confirm gPTP grandmaster placement (SA8620P or dedicated GM unit)
