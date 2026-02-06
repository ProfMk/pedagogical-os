# Pedagogical OS – Technical Roadmap



## Month 1 – Data Model \& Consolidation Engine

1.1 Core database schema

1.2 Indicator \& stage modeling

1.3 Student evidence ingestion

1.4 Consolidation engine logic

1.5 Stage progression rules

1.6 Unit testing framework


## Month 2–3 – Aggregation & Teacher Dashboard

### Objective
Provide clear, hierarchical, and pedagogically meaningful visualization of student progress,
built on top of the deterministic core implemented in Month 1.

---

### 2.1 Indicator aggregation
- Aggregate progress at Indicator level
- Use current stage and consolidation score
- Deterministic calculation only (no override)

---

### 2.2 Competency aggregation
- Aggregate Indicators belonging to the same Competency
- Use average of Indicator internal levels
- No institutional conversion yet

---

### 2.3 Nucleus aggregation
- Aggregate Competencies belonging to the same Nucleus
- Hierarchical and deterministic
- Read-only aggregation logic

---

### 2.4 Internal level normalization
- Calculate normalized internal level (1–5)
- Based on:
  - micro-stage index
  - consolidation impact
- Internal use only (not yet institutional grading)

---

### 2.5 Preliminary institutional level conversion (no override)
- Convert internal normalized level to institutional scale
- Use institution-configured mapping
- Override is NOT allowed in this phase
- Conversion is informational only

---

### 2.6 Basic pedagogical alerts
- Detect low consolidation cases
- Trigger when consolidation < 0.60
- Alerts are informational (no interventions yet)

---

### 2.7 Teacher dashboard base structure
- Hierarchical visualization:
  - Indicator → Competency → Nucleus
- Minimum required elements:
  - Current stage (X of Y)
  - Consolidation bar
  - Visual alert indicators
- No advanced UX or AI features




## Month 4 – Override \& Institutional Mapping

4.1 Calculated vs final level

4.2 Override tracking

4.3 Institutional level mapping



## Month 5 – Basic Intervention Engine

5.1 Trigger system

5.2 Activity bank structure

5.3 Recommendation engine



## Month 6 – AI Integration

6.1 AI activity generation

6.2 Pedagogical framework injection

6.3 Usage tracking



## Month 7 – Stabilization \& Pilot

7.1 Integration testing

7.2 Performance optimization

7.3 Pilot feedback iteration



