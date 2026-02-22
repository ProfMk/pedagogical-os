# backend/tests/domain/rules/test_competency_aggregation_rule.py

from domain.rules.competency_aggregation_rule import calculate_competency_level


def test_competency_level_is_simple_average_of_indicators():
    """
    Given:
        - a competency with multiple indicators
        - each indicator already normalized (1–5)
    Then:
        - the competency level is the simple arithmetic average
    """

    indicator_levels = [2.0, 3.0, 4.0]

    result = calculate_competency_level(indicator_levels)

    assert result == 3.0

def test_competency_aggregation_is_order_independent():
    """
    Given:
        - the same indicator levels in different order
    Then:
        - the competency level must be the same
    """

    levels_a = [2.0, 3.0, 4.0]
    levels_b = [4.0, 2.0, 3.0]

    result_a = calculate_competency_level(levels_a)
    result_b = calculate_competency_level(levels_b)

    assert result_a == result_b


import pytest
from domain.exceptions.domain_error import DomainError


def test_competency_aggregation_with_empty_list_raises_domain_error():
    """
    Given:
        - an empty list of indicator levels
    Then:
        - a DomainError must be raised
    """

    with pytest.raises(DomainError):
        calculate_competency_level([])

