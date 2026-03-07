from uuid import UUID

from fastapi import APIRouter, Depends

from backend.application.use_cases.get_indicator_result import (
    GetIndicatorResultUseCase,
)

from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.indicator_result_repository_orm import (
    IndicatorResultRepositoryORM,
)

router = APIRouter()


def get_use_case(session=Depends(get_session)):
    repository = IndicatorResultRepositoryORM(session)
    return GetIndicatorResultUseCase(repository)


@router.get("/indicator-result")
def get_indicator_result(
    student_id: UUID,
    indicator_id: UUID,
    academic_period_id: UUID,
    use_case: GetIndicatorResultUseCase = Depends(get_use_case),
):

    result = use_case.execute(
        student_id=student_id,
        indicator_id=indicator_id,
        academic_period_id=academic_period_id,
    )

    return result