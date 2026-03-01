# Pedagogical OS – Project Guardrails
Version: 1.0
Status: Active
Scope: Global (applies to entire repository)

---

## 1. Purpose

This document defines the non-negotiable architectural, pedagogical, and governance constraints of Pedagogical OS.

Its purpose is to:

- Prevent architectural drift.
- Protect pedagogical core logic.
- Ensure deterministic behavior.
- Maintain clean layered separation.
- Preserve long-term system integrity.
- Guarantee traceability of decisions.

This document overrides informal chat agreements or temporary implementation shortcuts.

If a conflict exists between implementation and this document, this document prevails.

---

## 2. Non-Negotiable Architectural & Pedagogical Principles

The following rules are mandatory and cannot be bypassed without a formal versioned decision record (ADR).

### 2.1 Strict Layered Architecture

The system MUST follow strict separation of concerns:

- **Domain Layer**
  - Pure business logic only.
  - No external dependencies.
  - No database access.
  - No framework imports.
  - Deterministic behavior only.

- **Application Layer**
  - Orchestration of use cases.
  - DTO composition.
  - No business rule definitions.
  - No persistence logic.

- **Infrastructure Layer**
  - ORM mappings.
  - Database access.
  - External service integrations.
  - No business rules.

- **Interface Layer**
  - REST endpoints.
  - Input validation.
  - Output serialization.
  - No pedagogical logic.
  - No aggregation logic.
  - No progression rules.

Violation of layer boundaries is considered a structural error.

---

### 2.2 Irreversible Stage Progression

Micro-stage progression is strictly irreversible.

- A student can only move forward.
- Retrogression is forbidden.
- No manual override can reduce stage.
- No automatic recalculation can reduce stage.

Any modification to this rule requires:
- Major version increment.
- Explicit pedagogical justification.
- Formal ADR.

---

### 2.3 Deterministic Consolidation Engine

The consolidation engine must:

- Use only defined evidence windows.
- Apply fixed weighted logic.
- Produce deterministic results.
- Be fully testable.
- Have 100% decision branch coverage.

No probabilistic or AI-based adjustment is allowed before Month 6.

---

### 2.4 Aggregation Must Be Explainable

Indicator → Competency → Nucleus aggregation:

- Must use transparent mathematical operations.
- Must be reproducible.
- Must be traceable to underlying data.
- Must never hide intermediate values.

---

### 2.5 Override Restrictions

- No override functionality before Month 4.
- Override must preserve:
  - calculated_level
  - final_level
  - override_flag
  - audit trace
- Override can never modify raw evidence.

---

### 2.6 AI Restrictions

- No AI-generated decisions before Month 6.
- AI may not alter:
  - consolidation
  - progression
  - aggregation logic
- AI may only suggest, never decide.

---

### 2.7 Testing Is Mandatory

- All business rules must have unit tests.
- All progression rules must have branch coverage.
- Interface tests must not access real databases.
- No merge without passing tests.
---

## 3. Scope Control & Roadmap Authority

Pedagogical OS follows a strictly versioned and roadmap-driven development model.

### 3.1 Single Source of Truth

The official technical roadmap document is the single source of truth for:

- Scope definition
- Feature inclusion
- Feature exclusion
- Delivery sequencing
- Success criteria

If any informal discussion, prototype, or chat-based decision conflicts with the roadmap document, the roadmap prevails.

---

### 3.2 Month-Based Development Boundaries

Each development cycle is constrained by its roadmap month.

It is strictly forbidden to:

- Implement features belonging to future months.
- Anticipate structural requirements of future months.
- Introduce "future-ready" abstractions.
- Add preparatory database fields.
- Add override mechanisms before Month 4.
- Add AI components before Month 6.

All development must remain inside the explicitly defined scope of the current roadmap month.

---

### 3.3 Operational Points

Operational subdivision of roadmap months:

- Exists only to reduce cognitive load.
- Does not expand scope.
- Does not redefine deliverables.
- Does not introduce new features.

Operational points are organizational tools, not scope modifiers.

---

### 3.4 Scope Violation Protocol

If a request exceeds the current roadmap scope:

- Development must stop immediately.
- The scope conflict must be explicitly stated.
- A decision must be documented.
- No silent implementation is allowed.

Scope discipline is mandatory for system stability.

---

## 4. Data Integrity & Multi-Tenant Safety

Pedagogical OS is a multi-tenant B2B platform.

Data isolation and institutional separation are mandatory.

### 4.1 Tenant Isolation

- All domain entities must include `institution_id`.
- Cross-tenant data access is strictly forbidden.
- No query may return data without tenant filtering.
- Repository implementations must enforce tenant boundaries.

Violation of tenant isolation is considered a critical security breach.

---

### 4.2 Referential Integrity

- All foreign keys must be explicitly defined.
- No orphaned progress records are allowed.
- No deletion of historical evidence is permitted without audit trace.
- Stage progression must remain consistent with indicator definitions.

---

### 4.3 Deterministic Reproducibility

Given the same input data, the system must always produce the same:

- Consolidation result
- Stage progression
- Aggregation values

No hidden randomness is allowed in core logic.

---

## 5. Curriculum Versioning Governance

Curriculum structures are versioned and immutable once active.

### 5.1 Indicator & Stage Versioning

- Indicators must include `version_number`.
- Micro-stages cannot be modified retroactively.
- Structural curriculum changes require:
  - New version creation
  - Migration strategy
  - Formal documentation

---

### 5.2 Backward Compatibility

Active student progress records must:

- Remain attached to the curriculum version they started with.
- Never be silently remapped to new stage definitions.
- Preserve historical traceability.

---

## 6. Security by Design

Security is mandatory at architectural level.

### 6.1 No Business Logic in Controllers

Controllers must never:

- Perform consolidation calculations
- Apply progression rules
- Modify pedagogical states
- Aggregate hierarchical levels

All logic must be inside Domain or Application layers.

---

### 6.2 Input Validation

- All external input must be validated.
- UUIDs must be validated.
- No raw database exceptions must leak to API responses.
- Error messages must not expose internal schema details.

---

### 6.3 Read-Only Enforcement

Until explicitly authorized by roadmap month:

- Dashboards are read-only.
- No write operations are permitted.
- No state mutation is allowed through interface endpoints.

---

## 7. Testing Policy Enforcement

Testing is not optional.

### 7.1 Business Rule Testing

- All Domain rules must have unit tests.
- All stage progression paths must be covered.
- Consolidation thresholds must be tested at boundaries.

---

### 7.2 Interface Testing

- Interface tests must not access real databases.
- All database dependencies must be overridden.
- HTTP contract must be verified explicitly.

---

### 7.3 Regression Control

- Every bug fix must include a regression test.
- No merge is allowed if tests fail.
- Test coverage must increase or remain stable.

---

## 8. Documentation & Version Control

Documentation is mandatory and versioned.

### 8.1 No Silent Changes

- Any structural change requires documentation.
- Architectural modifications require ADR.
- Pedagogical core modifications require major version increment.

---

### 8.2 Versioning Rules

- Minor change → increment minor version.
- Structural change → increment major version.
- Pedagogical core change → increment major version and require justification.

---

## 9. LLM Usage & AI Interaction Policy

LLMs may assist development but cannot redefine system architecture.

### 9.1 LLM Restrictions

LLMs must not:

- Redesign core domain logic.
- Introduce new architectural paradigms.
- Bypass roadmap sequencing.
- Remove guardrails.

---

### 9.2 LLM Scope Enforcement

When using AI assistance:

- Always specify roadmap month.
- Always specify operational point.
- Always confirm change type.
- Always verify alignment with this document.

This document overrides LLM-generated suggestions.

---

## 10. Stability Over Optimization

The system prioritizes:

- Determinism over cleverness.
- Clarity over abstraction.
- Stability over feature expansion.
- Traceability over speed.

Overengineering is prohibited.

Premature optimization is prohibited.

Architectural consistency is mandatory.


## Versioning Policy for Pedagogical Core

Any change affecting:

- Stage progression rules
- Consolidation formula
- Micro-stage structure
- Aggregation hierarchy
- Indicator level calculation

Requires:

1. MAJOR version increment
2. New tag
3. Updated technical documentation
4. Regression tests
5. Explicit justification
---

## Roadmap Point Closure Rule

A roadmap point is not considered closed until:

- Code is committed
- Documentation is updated
- Roadmap status file is updated
- Tests are green
- Changes are pushed to GitHub

No local-only completion is valid.

# End of Document – Version 1.0

---

# ADDENDUM — GOVERNANCE EXPANSION (Version 2.0)

The following sections expand the governance model without altering
any prior rule defined in Version 1.0.

All previously defined constraints remain fully active.

---

## 11. Dual Environment Development Governance

Pedagogical OS formally adopts a dual-environment development model.

This model is binding and enforceable.

### 11.1 Strategic Design Environment

The Strategic Design Environment is responsible for:

- Architectural decisions
- Domain modeling
- Risk evaluation
- Roadmap compliance validation
- Specification drafting
- Pedagogical core protection
- Post-implementation validation

This environment acts as:

Architectural Authority.

It must not delegate undefined or open-ended instructions.

---

### 11.2 Mechanical Implementation Environment (CODEX)

The Mechanical Implementation Environment (e.g., CODEX or AI code generators):

Is permitted only to:

- Execute closed deterministic specifications
- Generate boilerplate structures
- Implement predefined DTOs
- Write repository implementations under instruction
- Produce tests explicitly defined

Is strictly forbidden from:

- Making architectural decisions
- Altering protected pedagogical logic
- Refactoring across layers
- Introducing new abstractions
- Modifying roadmap sequencing
- Interpreting ambiguous goals

Any violation is classified as structural governance breach.

---

## 12. CODEX SAFE SPECIFICATION PROTOCOL

All AI-assisted implementation must follow a closed instruction format.

A CODEX SAFE SPEC BLOCK must include:

- Exact objective
- Exact file paths to create
- Exact file paths to modify
- Explicit forbidden files
- Explicit constraints
- Required test names
- Explicit pedagogical core protection statement

Specifications must be deterministic and non-ambiguous.

Open-ended instructions are prohibited.

---

## 13. Mandatory Four-Phase Workflow Enforcement

Every roadmap point must follow this sequence:

Phase 1 — Architectural Definition  
Phase 2 — CODEX Safe Specification (if implementation required)  
Phase 3 — Controlled Implementation (develop branch only)  
Phase 4 — Architectural Validation and Governance Approval  

Skipping any phase is prohibited.

No roadmap point is considered complete unless all phases are executed.

---

## 14. AI-Assisted Development Safeguards

AI tools may assist implementation but must not:

- Redefine system architecture
- Modify domain logic autonomously
- Introduce structural patterns not defined
- Remove guardrails
- Circumvent roadmap sequencing

All AI-generated output must be validated
against this document before integration.

Human governance prevails over AI convenience.

---

## 15. Architectural Breach Escalation Framework

An architectural breach includes:

- Layer contamination
- Unauthorized modification of core logic
- Determinism violation
- Multi-tenant safety violation
- Roadmap scope violation
- Migration without structural validation
- CODEX acting beyond specification

Breach protocol:

1. Immediate halt of development
2. Formal breach documentation
3. Root cause analysis
4. Mandatory correction
5. Regression testing
6. Governance confirmation before continuation

No breach may be silently tolerated.

---

## 16. Deterministic Implementation Requirements

All implementation must satisfy:

- Reproducibility
- Explicit dependency declaration
- No hidden coupling
- No silent behavioral change
- No convenience shortcuts

Code clarity overrides abstraction density.

Implicit magic is forbidden.

---

---

## 17. Database Dump Structural Authority (NEW – CRITICAL)

The PostgreSQL structural dump is the authoritative representation
of the live relational structure.

It overrides:

- Assumptions
- ORM interpretations
- Migration memory
- AI suggestions
- Developer recollection

Before performing ANY of the following:

- Creating a new migration
- Modifying an existing table
- Adding or modifying a column
- Creating or reusing ENUM types
- Defining or altering foreign keys
- Changing UNIQUE constraints
- Modifying ON DELETE behavior
- Referencing table or column names
- Generating constraints in Alembic

The current database dump MUST be reviewed.

Verification must include:

- Exact table names
- Exact column names
- Exact constraint names
- Exact ENUM definitions
- Existing UNIQUE constraints
- Existing FK names
- Existing ON DELETE rules
- Current alembic_version

Assumptions are prohibited.

Recreating an existing ENUM without verification is prohibited.

Changing constraint names without verification is prohibited.

Modifying ON DELETE behavior without validation is prohibited.

Any migration created without dump verification constitutes a structural governance breach.

---

## 18. Governance-Level Version Reinforcement

Any modification affecting:

- Pedagogical core
- Consolidation engine
- Stage progression
- Aggregation logic
- Curriculum versioning
- Dual-environment governance rules
- Guardrail enforcement mechanisms

Requires:

1. Major version increment
2. Updated documentation
3. Regression tests
4. Git tag
5. Push confirmation to remote repository

Governance integrity overrides development velocity.

---

---

## 19. Mandatory Clean Rebuild Migration Validation (CRITICAL)

Structural migrations must be validated not only incrementally,
but also through full schema reconstruction.

Before approving any structural migration:

1. Execute incremental upgrade in the active development database.
2. Create a separate clean database instance.
3. Execute `alembic upgrade head` from empty state.
4. Confirm full schema reconstruction completes without errors.
5. Confirm no ENUM duplication.
6. Confirm no foreign key resolution errors.
7. Confirm no missing dependency between revisions.
8. Confirm metadata integrity.

Primary development and production databases must never be destroyed.

Clean rebuild validation must occur in an isolated temporary database.

Failure of clean rebuild blocks migration approval.

Approval without clean rebuild validation constitutes structural governance breach.

---

# End of Document – Version 2.0

