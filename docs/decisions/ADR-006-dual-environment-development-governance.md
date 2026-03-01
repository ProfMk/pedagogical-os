# ADR-006 — Dual Environment Development Governance (CODEX Integration)

Status: Accepted  
Date: 2026-03-01  
Decision Type: Structural Governance Decision  
Supersedes: None  
Related ADRs: ADR-001, ADR-003, ADR-005  

---

## Context

Pedagogical OS has evolved into a deterministic, multi-tenant B2B SaaS platform
with strict architectural layering, protected pedagogical core logic, and
migration safety constraints.

Development velocity requirements increased as the system matured.

The project owner works as a solo developer and uses AI-assisted tools
for implementation (e.g., CODEX).

Unrestricted AI-assisted development introduces risks:

- Architectural drift
- Layer contamination
- Implicit modification of pedagogical core logic
- Migration inconsistencies
- Determinism violations
- Silent rule reinterpretation

Given the critical nature of:

- Stage progression irreversibility
- Consolidation engine determinism
- Curriculum versioning integrity
- Multi-tenant isolation
- ORM metadata unification

A formal governance model was required to integrate AI-assisted coding
without compromising structural safety.

---

## Decision

Pedagogical OS adopts a Dual Environment Development Governance Model.

Development is formally separated into two environments:

### 1. Strategic Design Environment

This chat environment is responsible for:

- Architectural decisions
- Domain modeling
- Risk analysis
- Specification definition
- Version control management
- Pedagogical core protection
- Post-implementation validation

This environment acts as:

Architect + Governance Authority.

It does NOT generate unrestricted implementation code.

---

### 2. Mechanical Implementation Environment (CODEX)

CODEX is restricted to:

- Executing closed, deterministic specifications
- Generating boilerplate structures
- Implementing predefined DTOs
- Writing repository implementations
- Generating migrations under strict constraints
- Writing tests with explicitly defined behavior

CODEX is explicitly forbidden from:

- Making architectural decisions
- Modifying protected pedagogical logic
- Refactoring across layers without instruction
- Introducing structural changes not defined in specification
- Reinterpreting open-ended instructions

---

## Mandatory Four-Phase Workflow

All roadmap points must follow:

### Phase 1 — Architectural Definition
- Objective clarification
- Layer impact definition
- Database impact analysis
- Risk assessment
- Test definition
- Pedagogical core validation

### Phase 2 — CODEX SAFE SPEC BLOCK (if implementation required)
- Deterministic closed instruction block
- Explicit file paths
- Explicit forbidden files
- Explicit constraints
- Explicit required test names
- Core logic protection statements

### Phase 3 — External Implementation
- Implementation in CODEX
- Commit to develop branch only
- No direct commit to main

### Phase 4 — Architectural Validation
- Layer verification
- Determinism verification
- Migration safety verification
- Multi-tenant safety verification
- Test coverage verification
- Commit message formalization
- Version increment declaration

No roadmap point may bypass phases.

---

## Consequences

### Positive

- AI acceleration without architectural corruption
- Preserved deterministic behavior
- Protection of pedagogical engine integrity
- Reduced regression risk
- Enforced layer discipline
- Improved scalability for future team expansion

### Trade-offs

- Slightly slower initial design phase
- More formal workflow
- Additional validation step required

---

## Enforcement

- One roadmap point per chat.
- No cross-point development.
- No implementation without specification.
- No modification of protected core without explicit approval and major version increment.
- No merge without validation.

Violation of this ADR constitutes a structural governance breach.

---

## Version Impact

This ADR updates the Master Governance Protocol to v3.0.

It does not modify:

- Stage progression logic
- Consolidation engine logic
- Aggregation rules
- Curriculum versioning semantics
- ORM metadata rules

This is a governance-level structural enhancement only.

---

End of ADR-006.