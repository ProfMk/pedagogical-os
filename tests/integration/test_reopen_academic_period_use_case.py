from datetime import date, datetime
from uuid import uuid4

from backend.application.use_cases.reopen_academic_period import ReopenAcademicPeriodUseCase
from backend.domain.entities.academic_period import AcademicPeriod
from backend.infrastructure.repositories.academic_period_event_repository_orm import (
    AcademicPeriodEventRepositoryORM,
)


class InMemorySession:

    def __init__(self):
        self.items = []
        self.committed = False

    def add(self, item):
        self.items.append(item)

    def commit(self):
        self.committed = True


class InMemoryAcademicPeriodRepository:

    def __init__(self, period):
        self.period = period

    def get_by_id(self, academic_period_id):
        if self.period.id == academic_period_id:
            return self.period
        return None

    def save(self, period):
        self.period = period


def test_reopen_academic_period_use_case_integration_flow():
    period = AcademicPeriod(
        id=uuid4(),
        academic_year_id=uuid4(),
        name="Q1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        is_closed=True,
    )

    period_repo = InMemoryAcademicPeriodRepository(period)
    session = InMemorySession()
    event_repo = AcademicPeriodEventRepositoryORM(session)

    use_case = ReopenAcademicPeriodUseCase(period_repo, event_repo)

    use_case.execute(
        academic_period_id=period.id,
        reason="Correction approved by governance",
        performed_by_user_id=uuid4(),
        event_id=uuid4(),
        created_at=datetime(2026, 3, 1, 12, 0, 0),
    )

    assert period_repo.period.is_closed is False
    assert len(session.items) == 1
    assert session.items[0].academic_period_id == period.id
