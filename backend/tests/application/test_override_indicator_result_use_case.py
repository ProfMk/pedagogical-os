from uuid import uuid4
from decimal import Decimal
from datetime import datetime

from backend.application.use_cases.override_indicator_result import OverrideIndicatorResultUseCase
from backend.domain.entities.indicator_result import IndicatorResult


class FakeIndicatorResultRepository:

    def __init__(self, result: IndicatorResult | None):
        self._result = result
        self.saved = False

    def get_by_scope(self, academic_period_id, student_id, indicator_id):
        return self._result

    def save(self, result: IndicatorResult):
        self.saved = True
        self._result = result


def build_indicator_result():
    return IndicatorResult(
        id=uuid4(),
        academic_year_id=uuid4(),
        academic_period_id=uuid4(),
        student_id=uuid4(),
        indicator_id=uuid4(),
        calculated_level=Decimal("3.50"),
        final_level=Decimal("3.50"),
        override_flag=False,
        override_comment=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )


def test_override_sets_flag_when_level_changes():

    result = build_indicator_result()

    repo = FakeIndicatorResultRepository(result)

    use_case = OverrideIndicatorResultUseCase(repo)

    use_case.execute(
        academic_period_id=result.academic_period_id,
        student_id=result.student_id,
        indicator_id=result.indicator_id,
        new_final_level=Decimal("4.00"),
        comment="Teacher adjustment",
    )

    assert repo.saved is True
    assert result.final_level == Decimal("4.00")
    assert result.override_flag is True
    assert result.override_comment == "Teacher adjustment"
    assert result.calculated_level == Decimal("3.50")


def test_override_unsets_flag_when_level_equals_calculated():

    result = build_indicator_result()

    repo = FakeIndicatorResultRepository(result)

    use_case = OverrideIndicatorResultUseCase(repo)

    use_case.execute(
        academic_period_id=result.academic_period_id,
        student_id=result.student_id,
        indicator_id=result.indicator_id,
        new_final_level=Decimal("3.50"),
        comment=None,
    )

    assert repo.saved is True
    assert result.override_flag is False


def test_override_raises_if_not_found():

    repo = FakeIndicatorResultRepository(None)

    use_case = OverrideIndicatorResultUseCase(repo)

    try:
        use_case.execute(
            academic_period_id=uuid4(),
            student_id=uuid4(),
            indicator_id=uuid4(),
            new_final_level=Decimal("4.00"),
            comment=None,
        )
        assert False, "Expected ValueError"
    except ValueError:
        assert True