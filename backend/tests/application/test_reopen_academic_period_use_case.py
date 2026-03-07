from datetime import date, datetime
from uuid import uuid4

import pytest

from backend.application.use_cases.reopen_academic_period import ReopenAcademicPeriodUseCase
from backend.domain.entities.academic_period import AcademicPeriod
from backend.domain.exceptions.academic_exceptions import AcademicPeriodError
from backend.domain.value_objects.academic_period_event_type import AcademicPeriodEventType


class FakeAcademicPeriodRepository:

    def __init__(self, period):
        self.period = period
        self.saved_period = None

    def get_by_id(self, academic_period_id):
        if self.period is None:
            return None
        if self.period.id != academic_period_id:
            return None
        return self.period

    def save(self, period):
        self.saved_period = period


class FakeAcademicPeriodEventRepository:

    def __init__(self):
        self.saved_event = None

    def save(self, event):
        self.saved_event = event


def build_period(is_closed=True):
    return AcademicPeriod(
        id=uuid4(),
        academic_year_id=uuid4(),
        name="Q1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        is_closed=is_closed,
    )


def execute_use_case(use_case, period_id, reason="Audit reason"):
    return use_case.execute(
        academic_period_id=period_id,
        reason=reason,
        performed_by_user_id=uuid4(),
        event_id=uuid4(),
        created_at=datetime(2026, 1, 1, 0, 0, 0),
    )


def test_reopen_closed_period_success():
    period = build_period(is_closed=True)
    period_repo = FakeAcademicPeriodRepository(period)
    event_repo = FakeAcademicPeriodEventRepository()

    use_case = ReopenAcademicPeriodUseCase(period_repo, event_repo)

    updated_period = execute_use_case(use_case, period.id)

    assert updated_period.is_closed is False
    assert period_repo.saved_period is period


def test_reopen_open_period_raises_error():
    period = build_period(is_closed=False)
    period_repo = FakeAcademicPeriodRepository(period)
    event_repo = FakeAcademicPeriodEventRepository()

    use_case = ReopenAcademicPeriodUseCase(period_repo, event_repo)

    with pytest.raises(AcademicPeriodError):
        execute_use_case(use_case, period.id)


def test_reopen_without_reason_raises_error():
    period = build_period(is_closed=True)
    period_repo = FakeAcademicPeriodRepository(period)
    event_repo = FakeAcademicPeriodEventRepository()

    use_case = ReopenAcademicPeriodUseCase(period_repo, event_repo)

    with pytest.raises(AcademicPeriodError):
        execute_use_case(use_case, period.id, reason="   ")


def test_audit_event_created():
    period = build_period(is_closed=True)
    period_repo = FakeAcademicPeriodRepository(period)
    event_repo = FakeAcademicPeriodEventRepository()

    use_case = ReopenAcademicPeriodUseCase(period_repo, event_repo)

    execute_use_case(use_case, period.id)

    assert event_repo.saved_event is not None
    assert event_repo.saved_event.academic_period_id == period.id
    assert event_repo.saved_event.event_type == AcademicPeriodEventType.PERIOD_REOPENED
