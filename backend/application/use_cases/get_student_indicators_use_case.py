from typing import List
from uuid import UUID

from backend.application.dto.student_indicator_dto import StudentIndicatorDTO
from backend.application.ports.indicator_repository_port import IndicatorRepositoryPort

class GetStudentIndicatorsUseCase:

    def __init__(self, repository: IndicatorRepositoryPort):
        self.repository = repository

    def execute(
        self,
        student_id: UUID
    ) -> List[StudentIndicatorDTO]:
        return self.repository.get_indicators_for_student(student_id)
