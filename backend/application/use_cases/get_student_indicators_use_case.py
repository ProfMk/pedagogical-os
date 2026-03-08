from typing import List
from uuid import UUID

from backend.application.dtos.student_indicator_dto import StudentIndicatorDTO
from backend.infrastructure.repositories.indicator_repository import IndicatorRepository


class GetStudentIndicatorsUseCase:

    def __init__(self, repository: IndicatorRepository):
        self.repository = repository

    def execute(
        self,
        student_id: UUID
    ) -> List[StudentIndicatorDTO]:
        return self.repository.get_indicators_for_student(student_id)
