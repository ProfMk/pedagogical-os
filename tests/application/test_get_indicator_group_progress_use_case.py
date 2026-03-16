from uuid import uuid4

import pytest

from backend.application.use_cases.get_indicator_group_progress import (
    GetIndicatorGroupProgressUseCase
)
from backend.domain.entities.student_indicator_progress import (
    StudentIndicatorProgress
)


class FakeStudentIndicatorProgressRepository:
    def get_by_group_and_indicator(self, group_id, indicator_id):
        return [
            StudentIndicatorProgress(
                student_id=uuid4(),
                indicator_id=indicator_id,
                current_stage_order=3,
                consolidation_score=0.80,
            ),
            StudentIndicatorProgress(
                student_id=uuid4(),
                indicator_id=indicator_id,
                current_stage_order=3,
                consolidation_score=0.82,
            ),
            StudentIndicatorProgress(
                student_id=uuid4(),
                indicator_id=indicator_id,
                current_stage_order=2,
                consolidation_score=0.50,
            ),
            StudentIndicatorProgress(
                student_id=uuid4(),
                indicator_id=indicator_id,
                current_stage_order=4,
                consolidation_score=0.85,
            ),
        ]


def test_group_indicator_progress_is_aggregated_correctly():
    indicator_id = uuid4()
    group_id = "1A"

    repository = FakeStudentIndicatorProgressRepository()
    use_case = GetIndicatorGroupProgressUseCase(repository)

    result = use_case.execute(
        group_id=group_id,
        indicator_id=indicator_id,
        indicator_name="Comprende fracciones equivalentes",
        total_stages=5,
    )

    expected_stage_avg = (3 + 3 + 2 + 4) / 4
    expected_consolidation_avg = (0.80 + 0.82 + 0.50 + 0.85) / 4

    assert result.stageAverage == expected_stage_avg
    assert result.consolidationAverage == expected_consolidation_avg
    assert result.totalStages == 5
