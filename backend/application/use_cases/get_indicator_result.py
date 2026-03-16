from uuid import UUID

from backend.application.dto.indicator_result_read_dto import (
    IndicatorResultReadDTO
)
from backend.application.ports.indicator_result_repository import (
    IndicatorResultRepository
)


class GetIndicatorResultUseCase:

    def __init__(self, repository: IndicatorResultRepository):
        self._repository = repository

    def execute(
        self,
        academic_period_id: UUID,
        student_id: UUID,
        indicator_id: UUID,
    ) -> IndicatorResultReadDTO:

        result = self._repository.get_by_scope(
            academic_period_id=academic_period_id,
            student_id=student_id,
            indicator_id=indicator_id,
        )

        if result is None:
            raise ValueError("IndicatorResult not found.")

        return IndicatorResultReadDTO(
            academic_year_id=result.academic_year_id,
            academic_period_id=result.academic_period_id,
            student_id=result.student_id,
            indicator_id=result.indicator_id,
            calculated_level=result.calculated_level,
            final_level=result.final_level,
            override_flag=result.override_flag,
            override_comment=result.override_comment,
        )
