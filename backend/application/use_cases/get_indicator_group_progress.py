from uuid import UUID

from backend.application.dto.indicator_group_progress_dto import (
    IndicatorGroupProgressDTO
)
from backend.infrastructure.repositories.student_indicator_progress_repository_orm import (
    StudentIndicatorProgressRepositoryORM
)


class GetIndicatorGroupProgressUseCase:
    """
    Application use case that computes aggregated group progress
    for a single indicator.

    This use case:
    - reads individual progress states
    - computes simple averages
    - performs NO pedagogical decisions
    """

    def __init__(
        self,
        repository: StudentIndicatorProgressRepositoryORM,
    ):
        self.repository = repository

    def execute(
        self,
        group_id: str,
        indicator_id: UUID,
        indicator_name: str,
        total_stages: int,
    ) -> IndicatorGroupProgressDTO:
        progresses = self.repository.get_by_group_and_indicator(
            group_id=group_id,
            indicator_id=indicator_id,
        )

        if not progresses:
            raise ValueError(
                "No StudentIndicatorProgress found for given group and indicator"
            )

        stage_avg = (
            sum(p.current_stage_order for p in progresses) / len(progresses)
        )

        consolidation_avg = (
            sum(p.consolidation_score for p in progresses) / len(progresses)
        )

        return IndicatorGroupProgressDTO(
            indicatorId=indicator_id,
            indicatorName=indicator_name,
            stageAverage=stage_avg,
            totalStages=total_stages,
            consolidationAverage=consolidation_avg,
        )
