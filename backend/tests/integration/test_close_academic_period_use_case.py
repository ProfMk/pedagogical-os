from datetime import date
from uuid import uuid4

from backend.application.use_cases.close_academic_period import CloseAcademicPeriodUseCase
from backend.domain.entities.academic_period import AcademicPeriod
from backend.infrastructure.repositories.academic_period_event_repository_orm import (
    AcademicPeriodEventRepositoryORM,
)

from backend.tests.integration.test_reopen_academic_period_use_case import (
    InMemoryAcademicPeriodRepository,
    InMemorySession,
)


class FakeIndicatorResultRepository:
    def get_all_by_period(self, academic_period_id):
        return []


class FakeEnrollmentRepository:
    def get_active_students(self, academic_year_id):
        return []


class FakeReportCardRepository:
    def save_nucleus_results(self, results):
        pass

    def save_subject_results(self, results):
        pass


def test_close_academic_period_creates_event():

    period = AcademicPeriod(
        id=uuid4(),
        academic_year_id=uuid4(),
        name="Q1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        is_closed=False,
    )

    period_repo = InMemoryAcademicPeriodRepository(period)

    session = InMemorySession()

    event_repo = AcademicPeriodEventRepositoryORM(session)

    indicator_repo = FakeIndicatorResultRepository()
    enrollment_repo = FakeEnrollmentRepository()
    report_repo = FakeReportCardRepository()

    use_case = CloseAcademicPeriodUseCase(
        period_repo,
        indicator_repo,
        enrollment_repo,
        report_repo,
        event_repo,
    )

    use_case.execute(
        academic_period_id=period.id,
        performed_by_user_id=uuid4(),
    )

    assert period.is_closed is True
    assert len(session.items) == 1
    assert session.items[0].event_type == "PERIOD_CLOSED"