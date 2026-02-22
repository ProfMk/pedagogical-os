import pytest

from domain.exceptions.domain_error import DomainError
from domain.rules.indicator_internal_level_rule import (
    calculate_indicator_internal_level,
)


def test_should_return_base_level_when_consolidation_is_zero():
    result = calculate_indicator_internal_level(
        stage_base_level=3.0,
        consolidation_score=0.0,
        consolidation_weight=0.3,
    )
    assert result == 3.0


def test_should_apply_maximum_weight_when_consolidation_is_one():
    result = calculate_indicator_internal_level(
        stage_base_level=2.0,
        consolidation_score=1.0,
        consolidation_weight=0.3,
    )
    assert result == 2.3


def test_should_increase_level_monotonically():
    low = calculate_indicator_internal_level(3.0, 0.2, 0.3)
    high = calculate_indicator_internal_level(3.0, 0.8, 0.3)
    assert high > low


def test_should_fail_if_weight_exceeds_maximum():
    with pytest.raises(DomainError):
        calculate_indicator_internal_level(
            stage_base_level=3.0,
            consolidation_score=0.5,
            consolidation_weight=0.31,
        )


def test_should_fail_if_stage_base_level_is_invalid():
    with pytest.raises(DomainError):
        calculate_indicator_internal_level(
            stage_base_level=6.0,
            consolidation_score=0.5,
            consolidation_weight=0.3,
        )


def test_should_fail_if_consolidation_score_is_invalid():
    with pytest.raises(DomainError):
        calculate_indicator_internal_level(
            stage_base_level=3.0,
            consolidation_score=1.5,
            consolidation_weight=0.3,
        )
