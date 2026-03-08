from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.application.dtos.student_indicator_dto import StudentIndicatorDTO


class IndicatorRepositoryPort(ABC):

    @abstractmethod
    def get_indicators_for_student(
        self,
        student_id: UUID
    ) -> List[StudentIndicatorDTO]:
        pass