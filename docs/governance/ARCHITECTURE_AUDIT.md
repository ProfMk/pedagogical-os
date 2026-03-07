# Pedagogical OS – Architecture Audit Rules

The system enforces strict layered architecture.

Layers:

Domain
Application
Infrastructure
Interface

## Layer Rules

Domain layer must not import:

- SQLAlchemy
- ORM models
- infrastructure modules
- FastAPI
- database sessions

Application layer must not import:

- SQLAlchemy
- ORM models
- database sessions

Infrastructure layer may import:

- SQLAlchemy
- ORM
- repositories

Interface layer must not:

- execute queries
- contain business logic
- import ORM models directly

## Forbidden Imports

Domain → infrastructure
Domain → sqlalchemy
Domain → fastapi

Application → sqlalchemy
Application → ORM

Interface → ORM queries

## Purpose

These rules guarantee:

- deterministic domain logic
- strict separation of layers
- long-term maintainability