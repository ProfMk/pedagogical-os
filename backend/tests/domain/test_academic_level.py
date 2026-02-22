# backend/tests/domain/test_academic_level.py

import pytest
from uuid import uuid4

from backend.domain.entities.academic_level import AcademicLevel
from backend.domain.exceptions.academic_exceptions import AcademicLevelError


def test_academic_level_success():
    level = AcademicLevel(
        id=uuid4(),
        institution_id=uuid4(),
        name="Primaria 3",
        order_index=2,
        education_stage="primaria"
    )

    assert level.name == "Primaria 3"
    assert level.order_index == 2
    assert level.education_stage == "primaria"


def test_academic_level_empty_name():
    with pytest.raises(AcademicLevelError):
        AcademicLevel(
            id=uuid4(),
            institution_id=uuid4(),
            name="",
            order_index=1
        )


def test_academic_level_whitespace_name():
    with pytest.raises(AcademicLevelError):
        AcademicLevel(
            id=uuid4(),
            institution_id=uuid4(),
            name="   ",
            order_index=1
        )


def test_academic_level_negative_order_index():
    with pytest.raises(AcademicLevelError):
        AcademicLevel(
            id=uuid4(),
            institution_id=uuid4(),
            name="Primaria 1",
            order_index=-1
        )