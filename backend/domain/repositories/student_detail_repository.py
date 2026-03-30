from abc import ABC, abstractmethod
from typing import List
from uuid import UUID


class StudentDetailRepository(ABC):
    @abstractmethod
    def get_student_detail(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        student_id: UUID,
    ) -> List[dict]:
        pass
