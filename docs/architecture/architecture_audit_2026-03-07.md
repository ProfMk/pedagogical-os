# Architecture Audit Report (Layered + DDD)

Date: 2026-03-07
Scope: `backend/` and architecture-related tests.
Method: static dependency/import review + architecture test execution.

## Confirmed corrected violations

1. **Domain layer remains framework-free**
   - No SQLAlchemy/FastAPI/infrastructure imports were found in `backend/domain`.
2. **ORM model classes are isolated under infrastructure ORM package**
   - ORM entities are defined in `backend/infrastructure/orm/*_orm.py`.
3. **Several infrastructure repositories explicitly implement application ports**
   - `IndicatorResultRepositoryORM`, `ReportCardRepositoryORM`, `StudentEnrollmentRepositoryORM`, and `AcademicPeriodEventRepositoryORM` inherit from corresponding application port interfaces.
4. **Use cases that mutate/read indicator results are port-driven and DB-agnostic**
   - `GetIndicatorResultUseCase` and `OverrideIndicatorResultUseCase` depend on `IndicatorResultRepository` port and never open sessions directly.
5. **Test layering is mostly aligned by intent**
   - Application tests use fake repositories.
   - Integration tests use SQLAlchemy session/ORM + infrastructure repositories.

## Remaining architecture violations

### V1 — Interface controllers still use ORM + DB session directly
- **Rule(s) violated**: Interface must not use ORM directly; controllers should delegate to use cases.
- **Files**:
  - `backend/interface/api/dashboard.py`
  - `backend/interface/api/indicator_result.py`
- **Details**:
  - Controllers import SQLAlchemy `Session`, infrastructure session provider, infrastructure repositories, and ORM models directly.
  - Dashboard endpoints execute `session.get(IndicatorORM, ...)` and instantiate ORM repositories in controller scope.

### V2 — Application layer imports infrastructure repositories
- **Rule(s) violated**: Application must depend only on ports; must not import infrastructure.
- **Files**:
  - `backend/application/use_cases/get_student_indicator_progress.py`
  - `backend/application/use_cases/get_indicator_group_progress.py`
- **Details**:
  - Use cases import concrete infrastructure repository classes instead of application port interfaces.

### V3 — Not all infrastructure repositories explicitly implement application ports
- **Rule(s) violated**: Infrastructure repositories should implement application ports.
- **Files**:
  - `backend/infrastructure/repositories/academic_period_repository_orm.py`
  - `backend/infrastructure/repositories/student_indicator_progress_repository.py`
  - `backend/infrastructure/repositories/student_indicator_progress_repository_orm.py`
- **Details**:
  - Repositories are concrete classes without explicit inheritance from application port contracts.
  - Missing corresponding ports for student indicator progress read paths in `backend/application/ports/`.

### V4 — Interface test layer mirrors interface architecture issue
- **Rule(s) violated**: Tests should not introduce architecture violations.
- **Files**:
  - `backend/tests/interface/test_dashboard_api.py`
  - `backend/tests/interface/test_dashboard_student_indicator_progress.py`
- **Details**:
  - Interface tests couple directly to infrastructure session and ORM model types due to controller design.

## Architecture cleanliness status

**MAJOR VIOLATIONS**

Rationale: direct layer boundary breaks remain in core paths (interface ↔ infrastructure and application ↔ infrastructure), which violates the architecture dependency direction.

## Recommended corrections

1. Introduce application ports for student progress read scenarios:
   - `StudentIndicatorProgressReaderPort`
   - `IndicatorGroupProgressReaderPort` (or one combined read port)
2. Refactor use cases to depend on these ports, never on infrastructure classes.
3. Move session handling + repository wiring out of controllers into composition/root dependency providers.
4. Refactor controllers to only:
   - parse request
   - call use case
   - map response/error
5. Add/align port for academic period repository and make `AcademicPeriodRepositoryORM` explicitly implement it.
6. Add architecture tests to enforce forbidden imports:
   - `backend/interface/**` must not import `backend.infrastructure.orm.*` or SQLAlchemy session types.
   - `backend/application/**` must not import `backend.infrastructure.*`.
7. Update interface tests to inject fakes at use-case boundary rather than coupling to ORM/session behavior.

## Validation checks executed

- `PYTHONPATH=/workspace/pedagogical-os pytest backend/tests/architecture -q`
- static import scans with `rg` over domain/application/interface/tests paths.
