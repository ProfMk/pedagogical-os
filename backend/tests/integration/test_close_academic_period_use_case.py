from uuid import uuid4

from backend.application.use_cases.reopen_academic_period import (
    ReopenAcademicPeriodUseCase,
)

from backend.infrastructure.repositories.academic_period_repository_orm import (
    AcademicPeriodRepositoryORM,
)

from backend.infrastructure.repositories.academic_period_event_repository_orm import (
    AcademicPeriodEventRepositoryORM,
)

from backend.infrastructure.orm.institutional_user_orm import InstitutionalUserORM


def test_reopen_academic_period_creates_event(
    academic_context,
    test_db_session,
):

    context = academic_context
    period = context["academic_period"]

    # cerrar periodo
    period.is_closed = True
    test_db_session.commit()

    # ---------------------------------------------------------
    # crear usuario institucional válido
    # ---------------------------------------------------------

    user = InstitutionalUserORM(
        id=uuid4(),
        email="integration@test.com",
        role="ADMIN",
    )

    test_db_session.add(user)
    test_db_session.commit()

    # ---------------------------------------------------------
    # repositorios
    # ---------------------------------------------------------

    period_repo = AcademicPeriodRepositoryORM(test_db_session)

    event_repo = AcademicPeriodEventRepositoryORM(test_db_session)

    use_case = ReopenAcademicPeriodUseCase(
        period_repo,
        event_repo,
    )

    # ---------------------------------------------------------
    # ejecutar caso de uso
    # ---------------------------------------------------------

    use_case.execute(
        period.id,
        "Integration test reopen",
        user.id,
    )

    # ---------------------------------------------------------
    # verificar
    # ---------------------------------------------------------

    updated_period = period_repo.get_by_id(period.id)

    assert updated_period.is_closed is False