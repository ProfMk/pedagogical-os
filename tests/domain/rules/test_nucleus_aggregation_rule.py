# backend/tests/domain/rules/test_nucleus_aggregation_rule.py

from domain.rules.nucleus_aggregation_rule import calculate_nucleus_level


def test_nucleus_level_is_simple_average_of_competencies():
    """
    Given:
        - a nucleus with multiple competencies
        - each competency already normalized (1–5)
    Then:
        - the nucleus level is the simple arithmetic average
    """

    competency_levels = [2.5, 3.5, 4.0]

    result = calculate_nucleus_level(competency_levels)

    assert result == 3.3333333333333335

def test_nucleus_aggregation_is_order_independent():
    """
    Given:
        - the same competency levels in different order
    Then:
        - the nucleus level must be the same
    """

    levels_a = [2.5, 3.5, 4.0]
    levels_b = [4.0, 2.5, 3.5]

    result_a = calculate_nucleus_level(levels_a)
    result_b = calculate_nucleus_level(levels_b)

    assert result_a == result_b

import pytest
from domain.exceptions.domain_error import DomainError


def test_nucleus_aggregation_with_empty_list_raises_domain_error():
    """
    Given:
        - an empty list of competency levels
    Then:
        - a DomainError must be raised
    """

    with pytest.raises(DomainError):
        calculate_nucleus_level([])
