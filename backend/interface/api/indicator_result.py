from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.infrastructure.orm.session import get_session
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM

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

    result = (
        db.query(IndicatorResultORM)
        .filter(
            IndicatorResultORM.academic_year_id == payload.academic_year_id,
            IndicatorResultORM.student_id == payload.student_id,
            IndicatorResultORM.indicator_id == payload.indicator_id,
        )
        .first()
    )

    if not result:
        raise HTTPException(status_code=404, detail="Indicator result not found")

    result.final_level = payload.new_final_level
    result.override_flag = True
    result.override_comment = payload.override_comment

    db.commit()
    db.refresh(result)

    return result