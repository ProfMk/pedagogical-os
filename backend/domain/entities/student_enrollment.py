# backend/domain/entities/student_enrollment.py

from dataclasses import dataclass
from uuid import UUID

from backend.domain.exceptions.academic_exceptions import StudentEnrollmentError


@dataclass
class StudentEnrollment:
    id: UUID
    student_id: UUID
    academic_year_id: UUID
    academic_level_id: UUID

    def __post_init__(self):
        if not self.student_id:
            raise StudentEnrollmentError("student_id is required")

        if not self.academic_year_id:
            raise StudentEnrollmentError("academic_year_id is required")

        if not self.academic_level_id:
            raise StudentEnrollmentError("academic_level_id is required")
