# Skill — SYS.3 Requirements Authoring

Skill for writing ASPICE SYS.3 system requirements on the SA8620P ADAS platform.

## Scope

- Three topics: gPTP TimeSync | HTP Orchestration | Technical Safety Concept
- Output: Codebeamer YAML attribute blocks + SHALL statements
- Standard: ASPICE v3.1 SYS.3

## Core Capability

Given a feature area and context, produce:
1. 6–12 SYS.3 requirements with full YAML attribute blocks
2. Measurable verification criteria for each
3. Safety mechanisms for ASIL ≥ A requirements
4. Vendor citations from the registry

## ID Convention

| Topic | Prefix | Example |
|-------|--------|---------|
| gPTP TimeSync | `SYS-GPTP` | `SYS-GPTP-003` |
| HTP Orchestration | `SYS-HTP` | `SYS-HTP-007` |
| Tech Safety Concept | `SYS-TSC` | `SYS-TSC-002` |
| Tech Safety Req | `SYS-TSR` | `SYS-TSR-011` |

## Quality Checklist

Before outputting a requirement:
- [ ] One SHALL per requirement
- [ ] No "should", "may", "appropriate", "reasonable"
- [ ] Quantified constraint with units
- [ ] Measurable verification criteria
- [ ] safety_mechanism present (ASIL ≥ A)
- [ ] allocates_to valid SA8620P target
- [ ] At least one vendor reference
