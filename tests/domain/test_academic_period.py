# backend/tests/domain/test_academic_period.py

import pytest
from datetime import date, datetime
from uuid import uuid4

from backend.domain.entities.academic_period import AcademicPeriod
from backend.domain.exceptions.academic_exceptions import AcademicPeriodError


def build_valid_period():
    return AcademicPeriod(
        id=uuid4(),
        academic_year_id=uuid4(),
        name="Periodo 1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
    )


# ---------- Initialization Rules ----------

def test_period_invalid_date_range():
    with pytest.raises(AcademicPeriodError):
        AcademicPeriod(
            id=uuid4(),
            academic_year_id=uuid4(),
            name="Periodo 1",
            start_date=date(2026, 4, 1),
            end_date=date(2026, 3, 31),
        )


def test_period_empty_name():
    with pytest.raises(AcademicPeriodError):
        AcademicPeriod(
            id=uuid4(),
            academic_year_id=uuid4(),
            name="",
            start_date=date(2026, 1, 1),
            end_date=date(2026, 3, 31),
        )


# ---------- Year Boundary Validation ----------

def test_period_outside_year_start():
    period = build_valid_period()
    with pytest.raises(AcademicPeriodError):
        period.validate_within_year(
            year_start=date(2026, 2, 1),
            year_end=date(2026, 12, 31),
        )


def test_period_outside_year_end():
    period = build_valid_period()
    with pytest.raises(AcademicPeriodError):
        period.validate_within_year(
            year_start=date(2026, 1, 1),
            year_end=date(2026, 2, 28),
        )


def test_period_within_year_success():
    period = build_valid_period()
    period.validate_within_year(
        year_start=date(2026, 1, 1),
        year_end=date(2026, 12, 31),
    )


# ---------- Closing Rules ----------

def test_close_period_success():
    period = build_valid_period()
    snapshot_time = datetime.utcnow()
    period.close(snapshot_time)
    assert period.is_closed is True
    assert period.snapshot_generated_at == snapshot_time


def test_close_period_twice_fails():
    period = build_valid_period()
    period.close(datetime.utcnow())

    with pytest.raises(AcademicPeriodError):
        period.close(datetime.utcnow())


def test_close_requires_snapshot_time():
    period = build_valid_period()
    with pytest.raises(AcademicPeriodError):
        period.close(None)
