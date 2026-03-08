from uuid import UUID

from fastapi import APIRouter, Depends

from backend.application.use_cases.get_student_indicator_progress import (
    GetStudentIndicatorProgressUseCase,
)

from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.student_indicator_progress_repository_orm import (
    StudentIndicatorProgressRepositoryORM,
)

router = APIRouter()


def get_use_case(session=Depends(get_session)):
    repository = StudentIndicatorProgressRepositoryORM(session)
    return GetStudentIndicatorProgressUseCase(repository)


@router.get("/dashboard/indicator/{indicator_id}/student/{student_id}")
def get_student_indicator_dashboard(
    indicator_id: UUID,
    student_id: UUID,
    use_case: GetStudentIndicatorProgressUseCase = Depends(get_use_case),
):

    dto = use_case.execute(
        student_id=student_id,
        indicator_id=indicator_id,
    )

    return {
        "studentId": str(dto.student_id),
        "studentName": dto.student_name,
        "indicatorId": str(dto.indicator_id),
        "indicatorDescription": dto.indicator_description,
        "currentStage": dto.current_stage,
        "totalStages": dto.total_stages,
        "normalizedLevelInternal": dto.normalized_level_internal,
        "consolidationScore": dto.consolidation_score,
        "hasLowConsolidationAlert": dto.has_low_consolidation_alert,
    }

@router.get("/dashboard")
def get_dashboard_summary():
    """
    Temporary dashboard summary endpoint.

    This endpoint will later be connected to a proper
    DashboardSummaryUseCase.

    For now it allows the frontend architecture to run
    without breaking.
    """

    return {
        "subjectGroups": [],
        "students": [],
        "alerts": [],
        "progressSummary": {}
    }