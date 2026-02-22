# ADR-001 – Strict Layered Architecture Enforcement

Status: Accepted  
Date: <YYYY-MM-DD>

---

## Context

Pedagogical OS is a B2B SaaS platform with:

- Pedagogical core logic (stage progression, consolidation, aggregation)
- Multi-tenant constraints
- Deterministic behavior requirements
- Long-term institutional stability goals

Without strict separation of responsibilities, the system risks:

- Business logic leaking into controllers
- Hidden side effects
- Testing fragility
- Architectural drift
- Increased coupling between layers

The project also uses AI assistance for development, which increases the risk of uncontrolled structural changes.

---

## Decision

The system will enforce a strict four-layer architecture:

1. Domain Layer  
   - Pure business rules  
   - No framework imports  
   - No database access  
   - Deterministic logic only  

2. Application Layer  
   - Use case orchestration  
   - DTO construction  
   - No business rule definitions  

3. Infrastructure Layer  
   - ORM mappings  
   - Database access  
   - External integrations  
   - No pedagogical logic  

4. Interface Layer  
   - REST endpoints  
   - Serialization  
   - Input validation  
   - No business logic  

Any violation of these boundaries is considered a structural error.

---

## Consequences

Positive:

- High testability
- Predictable behavior
- Clear separation of responsibilities
- Long-term maintainability
- Protection against overengineering

Negative:

- Slight increase in boilerplate code
- Explicit mapping required between layers

This tradeoff is accepted in favor of stability.