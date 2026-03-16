# backend/tests/domain/test_student_enrollment.py

import pytest
from uuid import uuid4

from backend.domain.entities.student_enrollment import StudentEnrollment
from backend.domain.exceptions.academic_exceptions import StudentEnrollmentError


def test_student_enrollment_success():
    enrollment = StudentEnrollment(
        id=uuid4(),
        student_id=uuid4(),
        academic_year_id=uuid4(),
        academic_level_id=uuid4(),
    )

    assert enrollment.student_id is not None
    assert enrollment.academic_year_id is not None
    assert enrollment.academic_level_id is not None


def test_student_enrollment_missing_student_id():
    with pytest.raises(StudentEnrollmentError):
        StudentEnrollment(
            id=uuid4(),
            student_id=None,
            academic_year_id=uuid4(),
            academic_level_id=uuid4(),
        )


def test_student_enrollment_missing_academic_year_id():
    with pytest.raises(StudentEnrollmentError):
        StudentEnrollment(
            id=uuid4(),
            student_id=uuid4(),
            academic_year_id=None,
            academic_level_id=uuid4(),
        )


def test_student_enrollment_missing_academic_level_id():
    with pytest.raises(StudentEnrollmentError):
        StudentEnrollment(
            id=uuid4(),
            student_id=uuid4(),
            academic_year_id=uuid4(),
            academic_level_id=None,
        )
