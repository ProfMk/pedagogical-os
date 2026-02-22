from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dataclasses import asdict


from backend.application.use_cases.get_indicator_group_progress import (
    GetIndicatorGroupProgressUseCase
)
from backend.application.use_cases.get_student_indicator_progress import (
    GetStudentIndicatorProgressUseCase
)
from backend.infrastructure.repositories.student_indicator_progress_repository_orm import (
    StudentIndicatorProgressRepositoryORM
)
from backend.infrastructure.orm.session import get_session
from backend.infrastructure.orm.indicator_orm import IndicatorORM


router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/indicator/{indicator_id}/group/{group_id}")
def get_indicator_group_progress(
    indicator_id: UUID,
    group_id: str,
    session: Session = Depends(get_session),
):
    """
    Returns aggregated group progress for a single indicator.
    Read-only endpoint.
    """

    indicator = session.get(IndicatorORM, indicator_id)
    if indicator is None:
        raise HTTPException(
            status_code=404,
            detail="Indicator not found"
        )

    repository = StudentIndicatorProgressRepositoryORM(session)
    use_case = GetIndicatorGroupProgressUseCase(repository)

    try:
        result = use_case.execute(
            group_id=group_id,
            indicator_id=indicator_id,
            indicator_name=indicator.description,
            total_stages=indicator.total_stages,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )

    return result.dict()

@router.get("/indicator/{indicator_id}/student/{student_id}")
def get_indicator_student_progress(
    indicator_id: UUID,
    student_id: UUID,
    session: Session = Depends(get_session),
):
    """
    Returns individual student progress for a single indicator.
    Read-only endpoint.
    """

    # 1. Validate indicator exists
    indicator = session.get(IndicatorORM, indicator_id)
    if indicator is None:
        raise HTTPException(
            status_code=404,
            detail="Indicator not found"
        )

    # 2. Build repository and use case
    repository = StudentIndicatorProgressRepositoryORM(session)
    use_case = GetStudentIndicatorProgressUseCase(repository)

    # 3. Execute use case
    try:
        result = use_case.execute(
            student_id=student_id,
            indicator_id=indicator_id,
            indicator_name=indicator.description,
            total_stages=indicator.total_stages,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc)
        )

    # 4. Return DTO as dict
    return {
    "studentName": result.student_name,
    "indicatorId": result.indicator_id,
    "indicatorDescription": result.indicator_description,

    "currentStage": result.current_stage,
    "totalStages": result.total_stages,

    "normalizedLevelInternal": result.normalized_level_internal,
    "consolidationScore": result.consolidation_score,

    "hasLowConsolidationAlert": result.has_low_consolidation_alert,
} 
