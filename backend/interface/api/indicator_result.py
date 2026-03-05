from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.indicator_result_repository import (
    IndicatorResultRepositoryORM,
)

from backend.application.use_cases.override_indicator_result import (
    OverrideIndicatorResultUseCase,
)
from backend.application.use_cases.get_indicator_result import (
    GetIndicatorResultUseCase,
)

from backend.interface.schemas.indicator_result import (
    IndicatorResultOverrideRequest,
    IndicatorResultResponse,
)

router = APIRouter(prefix="/indicator-results", tags=["Indicator Results"])


@router.patch("/override", response_model=IndicatorResultResponse)
def override_indicator_result(
    payload: IndicatorResultOverrideRequest,
    db: Session = Depends(get_session),
):

    repository = IndicatorResultRepositoryORM(db)

    override_use_case = OverrideIndicatorResultUseCase(repository)
    get_use_case = GetIndicatorResultUseCase(repository)

    try:
        override_use_case.execute(
            academic_year_id=payload.academic_year_id,
            student_id=payload.student_id,
            indicator_id=payload.indicator_id,
            new_final_level=payload.new_final_level,
            override_comment=payload.override_comment,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    result = get_use_case.execute(
        academic_year_id=payload.academic_year_id,
        student_id=payload.student_id,
        indicator_id=payload.indicator_id,
    )

    return result