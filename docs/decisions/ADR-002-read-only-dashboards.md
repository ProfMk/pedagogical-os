# ADR-002 – Read-Only Dashboard Policy Before Override Phase

Status: Accepted  
Date: <YYYY-MM-DD>

---

## Context

During Months 2–3, the roadmap defines:

- Aggregation engine
- Normalized level calculation
- Dashboard visualization
- Basic alerts

Override functionality is explicitly scheduled for Month 4.

Allowing mutation or teacher override earlier would:

- Blur pedagogical traceability
- Complicate validation
- Break roadmap sequencing
- Introduce premature state mutation logic

---

## Decision

All dashboards implemented before Month 4 must be strictly read-only.

This includes:

- No write endpoints
- No state mutation
- No override capability
- No recalculation triggered from interface

Dashboards may expose:

- Aggregated values
- Consolidation scores
- Alert flags
- Normalized levels

But must never alter stored data.

---

## Consequences

Positive:

- Safe incremental development
- Deterministic validation
- Clear milestone separation
- Reduced complexity during aggregation phase

Negative:

- Teachers cannot override until Month 4
- Some functionality temporarily limited

This limitation is intentional and roadmap-aligned.