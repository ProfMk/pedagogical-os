# backend/tests/domain/rules/test_indicator_level_rule.py

from domain.rules.indicator_level_rule import calculate_indicator_level


def test_last_stage_with_full_consolidation_returns_five():
    """
    Given:
        - an indicator with 6 micro-stages
        - the student is in the last micro-stage
        - consolidation is full (1.0)
    Then:
        - the normalized level must be exactly 5.0
    """

    result = calculate_indicator_level(
        stage_index=6,
        total_stages=6,
        consolidation=1.0,
    )

    assert result == 5.0

def test_intermediate_consolidation_does_not_reach_stage_max():
    """
    Given:
        - an indicator with 7 micro-stages
        - the student is in stage 3
        - consolidation is intermediate (0.5)
    Then:
        - the normalized level is inside the stage range
        - but strictly lower than the stage maximum
    """

    total_stages = 7
    stage_index = 3
    consolidation = 0.5

    result = calculate_indicator_level(
        stage_index=stage_index,
        total_stages=total_stages,
        consolidation=consolidation,
    )

    stage_span = 4 / total_stages
    stage_min = 1 + (stage_index - 1) * stage_span
    stage_max = stage_min + stage_span

    assert stage_min < result < stage_max

import pytest

from domain.exceptions.domain_error import DomainError


def test_consolidation_out_of_range_raises_domain_error():
    """
    Given:
        - consolidation outside [0, 1]
    Then:
        - a DomainError must be raised
    """

    with pytest.raises(DomainError):
        calculate_indicator_level(
            stage_index=3,
            total_stages=7,
            consolidation=1.2,
        )

def test_invalid_stage_index_raises_domain_error():
    """
    Given:
        - stage_index outside valid range
    Then:
        - a DomainError must be raised
    """

    with pytest.raises(DomainError):
        calculate_indicator_level(
            stage_index=0,   # invalid
            total_stages=5,
            consolidation=0.5,
        )

    with pytest.raises(DomainError):
        calculate_indicator_level(
            stage_index=6,   # invalid
            total_stages=5,
            consolidation=0.5,
        )

def test_normalized_level_out_of_global_range_raises_domain_error():
    """
    Given:
        - a calculation that would push the result outside [1, 5]
    Then:
        - a DomainError must be raised
    """

    # This should never happen with correct inputs,
    # but we protect the boundary explicitly.
    with pytest.raises(DomainError):
        calculate_indicator_level(
            stage_index=1,
            total_stages=1,
            consolidation=1.5,  # invalid consolidation, forces overflow
        )

