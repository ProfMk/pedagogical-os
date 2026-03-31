import uuid
from decimal import Decimal
from datetime import datetime

from backend.domain.entities.indicator_result import IndicatorResult
from backend.infrastructure.repositories.indicator_result_repository_orm import (
    IndicatorResultRepositoryORM,
)
from backend.application.use_cases.override_indicator_result import (
    OverrideIndicatorResultUseCase,
)
from backend.infrastructure.repositories.academic_period_repository_orm import (
    AcademicPeriodRepositoryORM,
)
from backend.infrastructure.orm.academic_period_orm import AcademicPeriodORM


def test_override_indicator_result_by_period(test_db_session):

    repository = IndicatorResultRepositoryORM(test_db_session)
    academic_period_repository = AcademicPeriodRepositoryORM(test_db_session)

    academic_year_id = uuid.uuid4()
    academic_period_id = uuid.uuid4()
    student_id = uuid.uuid4()
    indicator_id = uuid.uuid4()

    academic_period = AcademicPeriodORM(
        id=academic_period_id,
        academic_year_id=academic_year_id,
        code="P1",
        name="Period 1",
        sequence=1,
        weight=Decimal("0.50"),
        is_closed=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    academic_period_repository.save(academic_period)

    # Create initial result
    result = IndicatorResult(
        id=uuid.uuid4(),
        academic_year_id=academic_year_id,
        academic_period_id=academic_period_id,
        student_id=student_id,
        indicator_id=indicator_id,
        calculated_level=Decimal("3.50"),
        final_level=Decimal("3.50"),
        override_flag=False,
        override_comment=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    # Save initial state
    repository.save(result)

    # Execute override
    use_case = OverrideIndicatorResultUseCase(repository, academic_period_repository)

    use_case.execute(
        academic_period_id=academic_period_id,
        student_id=student_id,
        indicator_id=indicator_id,
        new_final_level=Decimal("4.00"),
        comment="Teacher adjustment",
    )

    # Retrieve updated result
    updated = repository.get_by_scope(
        academic_period_id=academic_period_id,
        student_id=student_id,
        indicator_id=indicator_id,
    )

    assert updated is not None
    assert updated.final_level == Decimal("4.00")
    assert updated.override_flag is True
    assert updated.override_comment == "Teacher adjustment"
    assert updated.calculated_level == Decimal("3.50")
