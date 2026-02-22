# backend/app/domain/rules/competency_aggregation_rule.py

from domain.exceptions.domain_error import DomainError


def calculate_competency_level(indicator_levels: list[float]) -> float:
    """
    Calculates the competency level as the simple arithmetic average
    of indicator normalized levels (1–5).
    """

    if not indicator_levels:
        raise DomainError("Cannot calculate competency level with no indicators")

    return sum(indicator_levels) / len(indicator_levels)
