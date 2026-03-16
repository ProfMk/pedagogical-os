from uuid import UUID

from backend.application.ports.indicator_group_progress_reader_port import (
    IndicatorGroupProgressReaderPort
)


class GetIndicatorGroupProgressUseCase:

    def __init__(self, repository: IndicatorGroupProgressReaderPort):
        self.repository = repository

    def execute(
        self,
        group_id: str,
        indicator_id: UUID,
        indicator_name: str,
        total_stages: int
    ):

        student_progress = self.repository.get_by_group_and_indicator(
            group_id=group_id,
            indicator_id=indicator_id
        )

        total_students = len(student_progress)

        if total_students == 0:
            return {
                "indicator_id": indicator_id,
                "indicator_name": indicator_name,
                "total_students": 0,
                "average_level": 0,
                "completion_rate": 0,
            }

        stage_sum = sum(p.current_stage_order for p in student_progress)
        consolidation_sum = sum(p.consolidation_score for p in student_progress)

        stage_avg = stage_sum / total_students
        consolidation_avg = consolidation_sum / total_students

        return type("IndicatorGroupProgressResult", (), {
            "stageAverage": stage_avg,
            "consolidationAverage": consolidation_avg,
            "totalStages": total_stages
        })()
