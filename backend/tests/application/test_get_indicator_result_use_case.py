from uuid import uuid4
from decimal import Decimal
from datetime import datetime

from backend.application.use_cases.get_indicator_result import (
    GetIndicatorResultUseCase
)
from backend.application.use_cases.override_indicator_result import (
    OverrideIndicatorResultUseCase
)
from backend.domain.entities.indicator_result import IndicatorResult


class FakeRepository:
    """
    In-memory fake repository used for Application layer tests.
    """

    def __init__(self, result: IndicatorResult | None):
        self._result = result

    def get_by_scope(self, academic_period_id, student_id, indicator_id):
        if self._result is None:
            return None

        if (
            self._result.academic_period_id == academic_period_id
            and self._result.student_id == student_id
            and self._result.indicator_id == indicator_id
        ):
            return self._result

        return None

    def save(self, result: IndicatorResult):
        self._result = result


def build_result():
    return IndicatorResult(
        id=uuid4(),
        academic_year_id=uuid4(),
        academic_period_id=uuid4(),
        student_id=uuid4(),
        indicator_id=uuid4(),
        calculated_level=Decimal("3.40"),
        final_level=Decimal("3.40"),
        override_flag=False,
        override_comment=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


def test_returns_indicator_result_dto():

    result = build_result()

    use_case = GetIndicatorResultUseCase(
        repository=FakeRepository(result)
    )

    dto = use_case.execute(
        academic_period_id=result.academic_period_id,
        student_id=result.student_id,
        indicator_id=result.indicator_id,
    )

    assert dto.calculated_level == Decimal("3.40")
    assert dto.final_level == Decimal("3.40")
    assert dto.override_flag is False
    assert dto.override_comment is None


def test_raises_if_not_found():

    use_case = GetIndicatorResultUseCase(
        repository=FakeRepository(None)
    )

    try:
        use_case.execute(uuid4(), uuid4(), uuid4())
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_full_override_and_read_flow():

    result = build_result()

    repo = FakeRepository(result)

    override_use_case = OverrideIndicatorResultUseCase(repo)
    read_use_case = GetIndicatorResultUseCase(repo)

    # Step 1: Apply override
    override_use_case.execute(
        academic_period_id=result.academic_period_id,
        student_id=result.student_id,
        indicator_id=result.indicator_id,
        new_final_level=Decimal("4.50"),
        comment="Manual teacher override",
    )

    # Step 2: Read result
    dto = read_use_case.execute(
        academic_period_id=result.academic_period_id,
        student_id=result.student_id,
        indicator_id=result.indicator_id,
    )

    assert dto.calculated_level == Decimal("3.40")
    assert dto.final_level == Decimal("4.50")
    assert dto.override_flag is True
    assert dto.override_comment == "Manual teacher override"