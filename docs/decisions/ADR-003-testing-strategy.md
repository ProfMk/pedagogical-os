# ADR-003 – DTO Serialization Strategy (Dataclass + Explicit Interface Mapping)

Status: Accepted  
Date: <YYYY-MM-DD>

---

## Context

The system uses:

- Python 3.11+
- FastAPI
- SQLAlchemy
- Strict layered architecture

Application layer DTOs were initially designed using Python dataclasses.

FastAPI supports Pydantic models for response serialization, but introducing Pydantic into the Application layer would:

- Couple core logic to framework specifics
- Reduce architectural purity
- Increase dependency footprint in business logic

---

## Decision

DTOs in the Application layer will use Python dataclasses.

The Interface layer will:

- Explicitly map DTO fields to JSON responses
- Perform snake_case → camelCase transformation when necessary
- Avoid leaking ORM models directly

No ORM models will be returned from API endpoints.

No Pydantic models will be used inside the Domain or Application layers.

---

## Consequences

Positive:

- Clear separation between core logic and framework
- Improved testability of Application layer
- Reduced hidden serialization behavior
- Explicit API contracts

Negative:

- Manual mapping required in Interface layer
- Slight increase in boilerplate code

This tradeoff favors architectural integrity over convenience.