from abc import ABC, abstractmethod
from typing import List
from uuid import UUID


class StudentIndicatorProgressReaderPort(ABC):

    @abstractmethod
    def get_student_indicator_progress(
        self,
        student_id: UUID,
        academic_year_id: UUID
    ) -> List[dict]:
        """
        Returns consolidated indicator progress for a student.
        """
        pass