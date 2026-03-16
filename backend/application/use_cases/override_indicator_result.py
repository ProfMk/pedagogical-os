from uuid import UUID
from decimal import Decimal

from backend.application.ports.indicator_result_repository import IndicatorResultRepository


class OverrideIndicatorResultUseCase:

    def __init__(self, repository: IndicatorResultRepository):
        self._repository = repository

    def execute(
        self,
        academic_period_id: UUID,
        student_id: UUID,
        indicator_id: UUID,
        new_final_level: Decimal,
        comment: str | None,
    ) -> None:

        result = self._repository.get_by_scope(
            academic_period_id=academic_period_id,
            student_id=student_id,
            indicator_id=indicator_id,
        )

        if result is None:
            raise ValueError("IndicatorResult not found for given scope.")

        result.apply_override(
            new_final_level=new_final_level,
            comment=comment,
        )

        self._repository.save(result)
