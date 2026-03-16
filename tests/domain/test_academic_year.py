# backend/tests/domain/test_academic_year.py

import pytest
from datetime import date
from uuid import uuid4

from backend.domain.entities.academic_year import AcademicYear, AcademicYearStatus
from backend.domain.exceptions.academic_exceptions import AcademicYearError


def build_valid_year(status=AcademicYearStatus.DRAFT):
    return AcademicYear(
        id=uuid4(),
        institution_id=uuid4(),
        name="2026",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
        status=status,
    )


# ---------- Initialization Rules ----------

def test_academic_year_invalid_dates():
    with pytest.raises(AcademicYearError):
        AcademicYear(
            id=uuid4(),
            institution_id=uuid4(),
            name="2026",
            start_date=date(2026, 12, 31),
            end_date=date(2026, 1, 1),
            status=AcademicYearStatus.DRAFT,
        )


def test_academic_year_empty_name():
    with pytest.raises(AcademicYearError):
        AcademicYear(
            id=uuid4(),
            institution_id=uuid4(),
            name="",
            start_date=date(2026, 1, 1),
            end_date=date(2026, 12, 31),
            status=AcademicYearStatus.DRAFT,
        )


# ---------- Activation Rules ----------

def test_activate_draft_success():
    year = build_valid_year()
    year.activate(existing_active_year_exists=False)
    assert year.status == AcademicYearStatus.ACTIVE


def test_activate_fails_if_not_draft():
    year = build_valid_year(status=AcademicYearStatus.ACTIVE)
    with pytest.raises(AcademicYearError):
        year.activate(existing_active_year_exists=False)


def test_activate_fails_if_other_active_exists():
    year = build_valid_year()
    with pytest.raises(AcademicYearError):
        year.activate(existing_active_year_exists=True)


# ---------- Closing Rules ----------

def test_close_active_success():
    year = build_valid_year(status=AcademicYearStatus.ACTIVE)
    year.close(open_periods_exist=False)
    assert year.status == AcademicYearStatus.CLOSED


def test_close_fails_if_not_active():
    year = build_valid_year(status=AcademicYearStatus.DRAFT)
    with pytest.raises(AcademicYearError):
        year.close(open_periods_exist=False)


def test_close_fails_if_open_periods_exist():
    year = build_valid_year(status=AcademicYearStatus.ACTIVE)
    with pytest.raises(AcademicYearError):
        year.close(open_periods_exist=True)
