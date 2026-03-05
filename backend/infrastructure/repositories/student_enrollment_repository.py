from uuid import UUID
from sqlalchemy.orm import Session

from backend.application.ports.student_enrollment_repository import (
    StudentEnrollmentRepository,
)
from backend.infrastructure.orm.student_enrollment_orm import StudentEnrollmentORM


class StudentEnrollmentRepositoryORM(StudentEnrollmentRepository):

    def __init__(self, session: Session):
        self._session = session

    def get_active_students(
        self,
        academic_year_id: UUID,
    ):

        rows = (
            self._session.query(StudentEnrollmentORM.student_id)
            .filter(
                StudentEnrollmentORM.academic_year_id == academic_year_id,
                StudentEnrollmentORM.is_active == True,
            )
            .all()
        )

        return [row.student_id for row in rows]