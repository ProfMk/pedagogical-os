# Pedagogical OS — Unified Development Roadmap
Version: 1.0  
Status: Active Governance Document  
Location: docs/governance/unified_development_roadmap.md

---

# 1. Purpose

This document defines the official unified development roadmap of Pedagogical OS.

It consolidates previous roadmap artifacts into a single deterministic development sequence aligned with:

- Pedagogical architecture
- Deterministic evaluation logic
- Layered backend architecture
- Governance rules
- Teacher operational workflows

This document becomes the single authoritative roadmap for the repository.

If any document conflicts with this roadmap, this roadmap prevails.

---

# 2. Governance Principles

## 2.1 Deterministic Development

All capabilities must be implemented in an order that preserves:

- deterministic system behavior
- pedagogical traceability
- architectural integrity
- data consistency

No feature may depend on functionality that has not yet been implemented.

---

## 2.2 Layered Architecture Compliance

All development must respect the system architecture.

Domain  
Application  
Infrastructure  
Interface  

Rules:

Domain Layer  
Pure business logic only.

Application Layer  
Use case orchestration and DTO construction.

Infrastructure Layer  
Persistence and repositories.

Interface Layer  
Controllers and serialization.

Controllers must never contain:

- business rules
- aggregation logic
- pedagogical calculations

---

## 2.3 Progressive System Stabilization

Development follows progressive stabilization.

Pedagogical Core  
→ Aggregation Engine  
→ Academic Governance  
→ Institutional Evaluation  
→ Teacher Dashboard  
→ Intervention Engine  
→ AI Pedagogical Assistance  

Each phase must reach architectural stability before the next phase begins.

---

## 2.4 Pedagogical Integrity

Protected mechanisms:

- micro-stage progression
- consolidation engine
- aggregation model
- indicator structure
- evidence model

Changes require:

- architecture review
- ADR documentation
- version increment

---

## 2.5 Multi-Tenant Safety

All queries must enforce:

- institution_id isolation
- academic_year scope
- academic_period scope

Cross-tenant access is forbidden.

---

# 3. Roadmap Structure

The roadmap is organized into seven sequential phases.

Phase 1 — Pedagogical Core Engine  
Phase 2 — Aggregation Engine  
Phase 3 — Academic Governance  
Phase 4 — Institutional Evaluation  
Phase 5 — Teacher Dashboard  
Phase 6 — Pedagogical Intervention Engine  
Phase 7 — AI Pedagogical Assistance  

Each phase contains explicit implementation points.

---

# Phase 1 — Pedagogical Core Engine

Purpose: establish the deterministic pedagogical foundation.

## 1.1 Institutional Core

Entities:

- Institution
- AcademicLevel
- AcademicGrade
- AcademicYear

Deliverables:

- multi-tenant foundation
- institutional configuration model

Status: Completed

---

## 1.2 Curriculum Hierarchy

Entities:

- Subject
- Nucleus
- Competency
- Indicator

Deliverables:

- hierarchical curriculum model
- curriculum version support

Status: Completed

---

## 1.3 Micro-Stage Structure

Entity:

IndicatorStage

Rules:

- stage_order defines progression
- normalized_level maps stage to internal level

Status: Completed

---

## 1.4 Evidence Model

Entities:

- Student
- StudentEvidence

Deliverables:

- timestamped evidence
- indicator linkage

Status: Completed

---

## 1.5 Student Indicator Progress

Entity:

StudentIndicatorProgress

Fields:

- current_stage_order
- consolidation_score
- normalized_level_internal

Status: Completed

---

## 1.6 Consolidation Engine

Rules:

Window: last 5 evidences  
Weights: [3,2,2,1,1]

Thresholds:

< 0.60 progressing  
0.60–0.79 consolidating  
≥ 0.80 consolidated

Status: Completed

---

# Phase 2 — Aggregation Engine

Purpose: transform individual progress into hierarchical evaluation.

## 2.1 Indicator Level Calculation

Formula:

IndicatorLevel =  
CurrentStageNormalized + (Consolidation * 0.3)

Status: Completed

---

## 2.2 Competency Aggregation

Formula:

CompetencyLevel = AVG(IndicatorLevel)

Status: Completed

---

## 2.3 Nucleus Aggregation

Formula:

NucleusLevel = AVG(CompetencyLevel)

Status: Completed

---

## 2.4 Aggregation Services

Responsibilities:

- deterministic aggregation
- application layer orchestration

Status: Completed

---

# Phase 3 — Academic Governance

Purpose: control evaluation periods.

## 3.1 Academic Period Model

Entity:

AcademicPeriod

Fields:

- start_date
- end_date
- is_closed

Status: Completed

---

## 3.2 Close Academic Period

Use case:

CloseAcademicPeriod

Effects:

- freeze updates
- block overrides
- snapshot results

Status: Completed

---

## 3.3 Reopen Academic Period

Use case:

ReopenAcademicPeriod

Requirements:

- mandatory reason
- audit record

Status: Completed

---

## 3.4 Academic Period Event Audit

Entity:

AcademicPeriodEvent

Event types:

- PERIOD_CLOSED
- PERIOD_REOPENED

Status: Completed

---

# Phase 4 — Institutional Evaluation

Purpose: produce institutional evaluation outputs with traceability.

## 4.1 Indicator Result Snapshot

Entity:

IndicatorResult

Fields:

calculated_level  
final_level  
override_flag  
override_comment  

Status: Completed

---

## 4.2 Teacher Override Mechanism

Constraints:

- raw evidence cannot change
- stage progression cannot regress

Status: Completed

---

## 4.3 Override Audit Trail

Entity:

IndicatorResultOverride

Records:

- previous value
- new value
- override comment
- responsible user

Status: Completed

---

# Phase 5 — Teacher Dashboard

Purpose: provide teachers with operational visibility of progress.

## 5.1 Frontend Modular Architecture

Structure:

Page  
↓  
Hook  
↓  
API  
↓  
Backend  

Status: Completed

---

## 5.2 Student Indicator Dashboard

Teachers view:

Group  
→ Student  
→ Indicator  
→ Current Stage  
→ Consolidation  
→ Normalized Level  

Status: Completed

---

## 5.3 Teacher Dashboard Data Access Layer

Responsibilities:

- HTTP abstraction
- DTO contract enforcement
- UI isolation

Status: Completed

---

## 5.4 Teacher Dashboard Backend Endpoint

Endpoint:

GET /teacher/dashboard

Responsibilities:

- return aggregated dataset
- enforce tenant isolation

Aggregation must occur in:

Application Layer

Status: Completed

---

## 5.5 Dashboard Aggregation Engine

Hierarchy:

Group  
→ Students  
→ Indicators  

DTO:

TeacherDashboardResponse

Status: Completed

---

## 5.6 Period State Visualization

Dashboard must display:

- active academic period
- period status
- timeline context

Status: Completed

---

## 5.7 Override Confirmation Flow

Teacher override interface must show:

- calculated level
- final level
- override confirmation

Status: Pending

---

# Phase 6 — Pedagogical Intervention Engine

Purpose: convert evaluation signals into pedagogical action.

## 6.1 Low Consolidation Trigger

Condition:

consolidation < 0.60

Status: Pending

---

## 6.2 Group Gap Detection

Condition:

> 30% students below threshold

Status: Pending

---

## 6.3 Activity Repository

Activities indexed by:

- indicator
- micro-stage
- difficulty
- cognitive focus

Status: Pending

---

## 6.4 Intervention Recommendations

Types:

- group intervention
- individual intervention

Status: Pending

---

## 6.5 Dashboard Intervention Integration

Dashboard must display:

- alerts
- recommended activities
- intervention suggestions

Status: Pending

---

# Phase 7 — AI Pedagogical Assistance

Purpose: assist teachers with activity generation.

## 7.1 AI Activity Generation Endpoint

Generates activities aligned with:

- indicator
- micro-stage
- consolidation state

Status: Pending

---

## 7.2 AI Prompt Structure

AI input:

- indicator description
- stage definition
- pedagogical framework

Status: Pending

---

## 7.3 AI Activity Log

Entity:

AIActivityLog

Records:

- generated activities
- teacher usage
- context parameters

Status: Pending

---

# 4. Current Development Position

Current system position:

Phase 5 — Teacher Dashboard  
Point 5.4 — Teacher Dashboard Backend Endpoint

---

# 5. Scope Control

Development must follow roadmap order.

Forbidden:

- implementing Phase 6 before Phase 5 stability
- introducing AI before Phase 7
- anticipating future abstractions

---

# 6. Modification Protocol

Changes require:

1. architecture review  
2. ADR documentation  
3. version increment  

No informal modifications are allowed.

---

# End of Document