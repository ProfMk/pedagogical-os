from uuid import UUID
from decimal import Decimal

from backend.application.ports.indicator_result_repository import IndicatorResultRepository
from backend.application.ports.academic_period_repository import AcademicPeriodRepository
from backend.domain.exceptions.academic_exceptions import AcademicPeriodError


class OverrideIndicatorResultUseCase:

    def __init__(
        self,
        repository: IndicatorResultRepository,
        academic_period_repository: AcademicPeriodRepository,
    ):
        self._repository = repository
        self._academic_period_repository = academic_period_repository

    def execute(
        self,
        academic_period_id: UUID,
        student_id: UUID,
        indicator_id: UUID,
        new_final_level: Decimal,
        comment: str | None,
    ) -> None:

        academic_period = self._academic_period_repository.get_by_id(academic_period_id)

        if academic_period is None:
            raise AcademicPeriodError("Academic period not found")

        if academic_period.is_closed:
            raise AcademicPeriodError("Cannot override: academic period is closed")

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
