from dataclasses import dataclass
from uuid import UUID

from backend.application.dto.student_indicator_progress_read_dto import (
    StudentIndicatorProgressReadDTO
)
from backend.infrastructure.repositories.student_indicator_progress_repository import (
    StudentIndicatorProgressRepository
)


@dataclass
class GetStudentIndicatorProgressUseCase:
    """
    Read-only use case.
    Returns the individual pedagogical progress of a student for a given indicator.
    """

    repository: StudentIndicatorProgressRepository

    def execute(
        self,
        student_id: UUID,
        indicator_id: UUID
    ) -> StudentIndicatorProgressReadDTO:
        """
        Executes the use case.

        Rules:
        - Read-only
        - No pedagogical decisions
        - Alert is derived ONLY from consolidation_score < 0.60
        """

        progress = self.repository.get_by_student_and_indicator(
            student_id=student_id,
            indicator_id=indicator_id
        )

        has_low_consolidation_alert = progress.consolidation_score < 0.60

        return StudentIndicatorProgressReadDTO(
            student_id=progress.student_id,
            student_name=progress.student_name,

            indicator_id=progress.indicator_id,
            indicator_description=progress.indicator_description,

            current_stage=progress.current_stage,
            total_stages=progress.total_stages,

            normalized_level_internal=progress.normalized_level_internal,
            consolidation_score=progress.consolidation_score,

            has_low_consolidation_alert=has_low_consolidation_alert
        )
