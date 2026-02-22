# ADR-005 – ORM Governance and Metadata Integrity

Status: Accepted  
Date: 2026-02-20  
Decision Type: Structural Architecture Hardening  

---

## Context

During Month 4 development, integration testing against real PostgreSQL revealed structural inconsistencies in ORM configuration.

Observed issues:

- Multiple import paths for the same ORM module.
- Mixed relative and absolute imports.
- Duplicate SQLAlchemy metadata trees.
- Foreign key resolution failures.
- Duplicate table registration errors.

These problems were invisible under mocked or in-memory tests.

They only surfaced during real integration testing.

This exposed a structural governance gap in ORM management.

---

## Problem

SQLAlchemy relies on a single shared declarative Base and a single metadata tree.

If:

- Multiple Base instances exist
- Modules are imported under different namespaces
- Relative and absolute imports are mixed

Then:

- Tables are registered multiple times
- Foreign keys cannot resolve
- Integration tests fail unpredictably
- Debugging becomes extremely complex

This is unacceptable for a deterministic B2B SaaS system.

---

## Decision

The system enforces:

1. A single declarative Base instance.
2. Absolute import policy rooted at `backend.`
3. Prohibition of relative Base imports.
4. Mandatory real PostgreSQL integration testing for persistence.
5. Architectural enforcement through automated tests.

---

## Rules Enforced

- Base must exist only in:
  backend.infrastructure.orm.base

- All ORM models must import:
  from backend.infrastructure.orm.base import Base

- Forbidden:
  - from .base import Base
  - from infrastructure.orm.base import Base
  - Mixed module roots

- All imports must start from:
  backend.

---

## Consequences

Positive:

- Stable foreign key resolution
- Deterministic metadata behavior
- Predictable integration tests
- Reduced debugging time
- Multi-developer safety

Trade-offs:

- Slightly stricter import discipline
- Enforcement tests required

The benefits outweigh the constraints.

---

## Enforcement

- System Context Master v1.4 updated.
- Automated structural tests implemented.
- Future ORM code must pass structural validation.

---

## Rationale

Pedagogical OS is deterministic by design.

Metadata fragmentation violates determinism at infrastructure level.

Structural integrity is mandatory in a multi-tenant B2B environment.

---

End of ADR-005