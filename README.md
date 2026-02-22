# \# Pedagogical OS

# 

# Pedagogical OS is a B2B multi-tenant SaaS platform designed to standardize curriculum execution, competency tracking, and evidence-based evaluation for private schools in Latin America.

# 

# \## Core Principles

# 

# \- Irreversible stage progression

# \- Weighted consolidation engine

# \- Hierarchical aggregation (Indicator → Competency → Nucleus)

# \- Institutional level mapping

# \- Teacher override with traceability

# \- Intervention engine

# \- AI aligned to pedagogical framework

# \- Secure-by-design architecture

# 

# \## Development Governance

# 

# \- Versioned technical documentation

# \- Structured roadmap execution

# \- Clean architecture

# \- English-only technical codebase

# \- UUID primary keys

# \- RESTful APIs

# \- Test-driven components

# 

# \## Repository Structure

# docs/

# backend/

# frontend/

database/

## Development Closure Protocol

Every roadmap point must follow this mandatory closure procedure:

1. Update documentation in `/docs`
2. Update `docs/roadmap/roadmap_status.md`
3. Ensure all tests pass
4. Commit using structured message:
   type(scope): roadmap-point-description
5. Push to `develop`
6. If milestone-level change → create version tag

Example:

git commit -m "feat(month-4-override): finalize indicator result persistence"
git push

===

# \## Roadmap

# 

# See ROADMAP.md

