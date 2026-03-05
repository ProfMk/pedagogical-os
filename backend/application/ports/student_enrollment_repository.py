from uuid import UUID
from typing import List


class StudentEnrollmentRepository:

    def get_active_students(
        self,
        academic_year_id: UUID,
    ) -> List[UUID]:
        raise NotImplementedError