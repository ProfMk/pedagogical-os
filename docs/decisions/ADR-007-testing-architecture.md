# ADR-007 — Structured Testing Architecture

Status: Accepted  
Date: 2026-03-07

## Context

Pedagogical OS contains complex deterministic pedagogical engines including:

- stage progression
- consolidation engine
- aggregation logic
- report card calculation

Testing these engines requires both fast feedback and realistic datasets.

Without structured testing architecture, tests risk:

- duplication
- inconsistent datasets
- slow execution
- unreliable simulation scenarios.

## Decision

The project adopts a three-layer testing architecture:

tests/unit  
tests/integration  
tests/simulation  

Pedagogical datasets must be generated through standardized builders.

Large simulation datasets are provided through SQL seeds.

## Consequences

Benefits:

- deterministic pedagogical testing
- fast unit tests
- realistic system validation
- reproducible datasets

Risks:

- additional governance overhead
- need for maintenance of builders and seeds.

This architecture becomes mandatory for all future tests.