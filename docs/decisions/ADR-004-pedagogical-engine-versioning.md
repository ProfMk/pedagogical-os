# ADR-004 — Pedagogical Engine Versioning Strategy

## Status
Accepted

## Context

Pedagogical OS is a B2B institutional SaaS where the pedagogical engine
(consolidation rules, stage promotion logic, aggregation formulas)
defines academic evaluation semantics.

Future modifications to these rules must not reinterpret historical data.

## Decision

The pedagogical engine will be versioned independently from the application version.

A future database table will store:

- version_string
- consolidation parameters
- promotion thresholds
- aggregation rules metadata

Each student_indicator_progress record will reference the engine version used
for its calculation.

This guarantees:

- Historical traceability
- Institutional auditability
- Controlled evolution of pedagogical logic
- Safe recalculation strategies

## Consequences

- Engine logic becomes explicit and governed
- Major pedagogical changes require new engine version
- Future migrations must preserve historical coherence