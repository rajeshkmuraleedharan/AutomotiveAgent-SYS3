# Internal Docs — Seeded Project Knowledge

Drop **sanitized** internal reference material here (architecture notes, review
protocols, platform docs) that the agent should treat as project background.
Prefer markdown; for tool exports use the `imports/` pipeline instead.

## Sanitization rule (before anything lands here)

- No customer or OEM program names
- No unreleased part numbers beyond those already in `vendor-references.instructions.md`
- No personal data beyond internal short names
- No license-restricted vendor documentation excerpts — cite `VENDOR-DOC §section` instead

Files here are read as background context; they never override the locked schema,
`rules/`, or `conventions.md`.
