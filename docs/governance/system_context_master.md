# Pedagogical OS – System Context Master
Version: 1.4
Status: Active
Scope: Operational LLM Context (Authoritative)

---

## 1. Project Identity

Pedagogical OS is a multi-tenant B2B SaaS platform designed for private schools in Latin America.

Primary Objective:

To provide a structured, transparent, evidence-based pedagogical system that:

- Aligns curriculum execution with evaluation criteria.
- Tracks competency development progressively.
- Reduces subjective grading.
- Generates actionable pedagogical insights.
- Preserves teacher autonomy with full traceability.

The system is deterministic by design.

Pedagogical integrity always prevails over technical convenience.

---

## 2. Architectural Model (Strictly Enforced)

The system follows a strict four-layer architecture.

### 2.1 Domain Layer

- Pure business logic only.
- No framework imports.
- No database access.
- No FastAPI.
- No SQLAlchemy.
- Deterministic behavior only.
- Contains:
  - Stage progression rules
  - Consolidation engine
  - Aggregation logic
  - Core pedagogical rules

Domain must remain completely framework-independent.

---

### 2.2 Application Layer

- Use case orchestration.
- DTO composition.
- Coordinates domain and infrastructure.
- No business rule definitions.
- DTOs implemented using Python dataclasses.
- No ORM models returned.

---

### 2.3 Infrastructure Layer

- SQLAlchemy ORM models.
- Repository implementations.
- Database access.
- Migrations.
- No pedagogical logic allowed.

---

### 2.4 Interface Layer

- FastAPI endpoints.
- Input validation.
- Explicit JSON serialization.
- Snake_case → camelCase mapping.
- No business logic.
- Controllers must remain thin.

Violation of layer boundaries is a structural error.

---

## 3. Project Structure (Locked)

The backend structure is fixed and part of the architectural contract.

backend/
  app/
  application/
    dto/
    use_cases/
    ports/
  domain/
    entities/
    rules/
    services/
    value_objects/
    exceptions/
  infrastructure/
    orm/
    repositories/
    migrations/
    db/
  interface/
    api/
    schemas/
  tests/
    domain/
    application/
    interface/
    integration/

docs/
  architecture/
  governance/
  decisions/
  pedagogy/
  roadmap/

Rules:

- No new top-level folders allowed.
- No merging of architectural layers.
- No alternative paradigms.
- Any structural change requires ADR approval.

---

## 4. Technology Stack (Locked)

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pytest

No microservices.
No CQRS.
No distributed architecture.
No stack change without ADR.

The system must remain simple and production-ready.

---

## 5. Core Pedagogical Constraints

### 5.1 Stage Progression

- Irreversible.
- No retrogression allowed.
- No override may reduce stage.
- Deterministic and fully test-covered.

---

### 5.2 Consolidation Engine

- Deterministic.
- No AI influence.
- No probabilistic logic.
- Fully testable.

Consolidation must produce identical results for identical inputs.

---

### 5.3 Aggregation Hierarchy

Indicator → Competency → Nucleus

- Transparent calculations.
- Reproducible logic.
- Traceable intermediate values.
- No hidden weighting.

---

## 6. Roadmap Discipline

Development is strictly roadmap-driven.

Forbidden:

- Implementing features from future months.
- Preparing abstractions “just in case”.
- Modifying locked months.
- Override before Month 4.
- AI before Month 6.

Operational points exist only to reduce cognitive load.
They do not expand scope.

---

## 7. Database Reality

Existing core tables:

- institution
- subject
- nucleus
- competency
- indicator
- indicator_stage
- student
- student_evidence
- student_indicator_progress

Constraints:

- UUID primary keys.
- Explicit foreign keys.
- Unique (student_id, indicator_id).
- Referential integrity enforced.
- Multi-tenant isolation mandatory.

No override/result table exists before Month 4.

New tables must not break existing constraints.

---

## 8. Multi-Tenant Safety

- All data must be institution-scoped.
- No cross-tenant queries allowed.
- Tenant filtering must be enforced at repository level.
- Data leakage is considered a critical error.

---

## 9. Testing Policy (Mandatory)

### 9.1 Domain

- All business rules must have unit tests.
- Stage progression requires full branch coverage.
- Consolidation boundaries must be tested.

---

### 9.2 Interface

- No real database access in interface tests.
- Dependency overrides required.
- HTTP contract must be verified explicitly.

---

### 9.3 Regression Control

- Every bug fix requires regression test.
- No merge with failing tests.
- Deterministic test behavior required.

---

## 10. Serialization Policy

- DTOs use Python dataclasses.
- Explicit JSON mapping in Interface layer.
- ORM models never returned directly.
- No framework coupling inside Domain.
- CamelCase for API responses.

---

## 11. Override Philosophy (Month 4+)

Override must:

- Preserve calculated_level.
- Store final_level separately.
- Include override_flag.
- Include override_comment.
- Never modify raw evidence.
- Never modify consolidation.
- Never modify progression.

Teacher autonomy must remain auditable.

---

## 12. AI Restrictions

AI may not:

- Modify consolidation.
- Modify progression.
- Modify aggregation.
- Decide final evaluation.

AI may only suggest (Month 6+).

---

## 13. Chat Segmentation Policy (Mandatory)

Each operational point of a roadmap month must be developed in a separate chat session.

Rules:

- One chat = One operational point.
- No cross-point development.
- No anticipation of future points.
- No retroactive modification of previous points.
- Each chat must begin with:
  - Month
  - Operational point
  - Status
  - Change type
- Each chat must propose a formal title before development.

This segmentation ensures traceability and cognitive control.

---

## 14. Development Protocol

For every new chat:

1. Confirm roadmap month.
2. Confirm operational point.
3. Confirm status.
4. Confirm change type.
5. Propose formal chat title.
6. Work strictly inside scope.
7. Provide full file paths and full code.
8. Explain step-by-step.
9. Stop immediately if scope violation is detected.

This document overrides informal chat agreements.

---

---

## 15. ORM Governance & Import Consistency (Critical Structural Rules)

The following rules are mandatory and derived from real integration testing validation.

These rules prevent metadata fragmentation, foreign key resolution errors, duplicate table registration, and structural instability.

Architectural consistency overrides convenience.

---

### 15.1 Single Declarative Base Rule (Non-Negotiable)

There must be exactly one SQLAlchemy declarative Base instance in the entire system.

The only allowed location:

backend.infrastructure.orm.base

All ORM models must import Base using absolute import:

from backend.infrastructure.orm.base import Base

Forbidden:

- Relative imports of Base (e.g. `from .base import Base`)
- Alternative Base definitions
- Multiple `declarative_base()` calls
- Multiple metadata trees

Multiple Base instances will break:

- Foreign key resolution
- Metadata integrity
- Cross-table mapping
- Integration test stability

Violation of this rule is considered a structural error.

---

### 15.2 Absolute Import Policy (Mandatory)

All imports inside backend must start from the root module:

backend.

Example:

from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM

Forbidden:

- `from infrastructure.`
- Mixed import roots
- Relative imports across architectural layers
- Inconsistent module prefixes

Python treats different import paths as different modules in memory.

Mixed imports cause:

- Duplicate metadata registration
- Duplicate table definitions
- Foreign key resolution failures
- Hard-to-debug runtime errors

All modules must share the same import root.

---

### 15.3 Metadata Integrity Rule

All ORM models must belong to the same Base.metadata tree.

No ORM model may be registered under a different module namespace.

Before debugging foreign key errors, verify:

- Single Base instance
- Single metadata tree
- No mixed import paths
- No duplicated module registration

Foreign key resolution errors often indicate metadata fragmentation, not database failure.

---

### 15.4 Mandatory Real Integration Testing for Persistence

Mock-based testing is insufficient to validate ORM structure.

Every repository implementation must include at least one real PostgreSQL integration test.

Integration tests must validate:

- Real insert
- Real foreign key resolution
- Real UNIQUE constraint behavior
- Real commit cycle
- Real deletion cleanup

In-memory or mocked databases may hide structural errors.

Integration testing against PostgreSQL is mandatory for persistence validation.

---

### 15.5 Structural Validation Checklist (Before Writing ORM Code)

Before implementing any new ORM model or repository, confirm:

- Base is imported from backend.infrastructure.orm.base
- No relative Base imports exist
- No mixed module roots are used
- All repository imports use absolute backend paths
- An integration test will be added
- No duplicate table names exist in metadata

Failure to validate these items is considered architectural negligence.

---

### 15.6 Enforcement Philosophy

These rules guarantee:

- Deterministic metadata behavior
- Stable foreign key resolution
- Predictable integration test execution
- Long-term maintainability
- Safe multi-developer collaboration

Structural discipline is mandatory in PEDAGOGICAL-OS.

---
# End of Document – System Context Master v1.3