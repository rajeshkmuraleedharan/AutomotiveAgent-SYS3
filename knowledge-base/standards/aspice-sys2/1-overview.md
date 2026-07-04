# ASPICE SYS.2 — System Requirements Analysis — Overview

SYS.2 transforms stakeholder requirements into a consistent, analyzed set of system
requirements. On this project: stakeholder input arrives as STK-* items, JIRA
stories, and Agreed concepts (CON-*); output is canonical YAML blocks with
`level: SYS.2` in Codebeamer.

## Process outcomes (ASPICE v3.1)

1. System requirements defined (from stakeholder requirements)
2. Categorized (functional / non-functional / safety / regulatory)
3. Analyzed for correctness, technical feasibility, and verifiability
4. Impact on the operating environment evaluated
5. Prioritized for implementation
6. Consistency + bidirectional traceability with stakeholder requirements
7. Communicated and agreed

## Position in this repo's chain

```
STK-* / CON-* concepts → SYS.2 (this) → SYS.3 requirements + ARC architecture
```

- SYS.2 answers WHAT the system must do at its boundary — solution-free
- SYS.3 quantifies HOW per platform element; ARC elements realize SYS.3
- Usage rules: `.github/instructions/sys2-requirements.instructions.md`
