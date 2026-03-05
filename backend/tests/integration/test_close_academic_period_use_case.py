from backend.application.use_cases.close_academic_period import CloseAcademicPeriodUseCase

from backend.infrastructure.repositories.indicator_result_repository_orm import (
    IndicatorResultRepositoryORM,
)
from backend.infrastructure.repositories.student_enrollment_repository import (
    StudentEnrollmentRepositoryORM,
)
from backend.infrastructure.repositories.report_card_repository_orm import (
    ReportCardRepositoryORM,
)
from backend.infrastructure.repositories.academic_period_repository_orm import (
    AcademicPeriodRepositoryORM,
)


def test_close_academic_period_generates_report_card(
    academic_context,
    test_db_session,
):

    context = academic_context

    period = context["academic_period"]

    indicator_repo = IndicatorResultRepositoryORM(test_db_session)
    enrollment_repo = StudentEnrollmentRepositoryORM(test_db_session)
    report_repo = ReportCardRepositoryORM(test_db_session)
    period_repo = AcademicPeriodRepositoryORM(test_db_session)

    use_case = CloseAcademicPeriodUseCase(
        period_repo,
        indicator_repo,
        enrollment_repo,
        report_repo,
    )

    use_case.execute(period.id)

    updated_period = period_repo.get_by_id(period.id)

    assert updated_period.is_closed is True