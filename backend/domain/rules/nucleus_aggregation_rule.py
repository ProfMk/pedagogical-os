# backend/app/domain/rules/nucleus_aggregation_rule.py

from domain.exceptions.domain_error import DomainError


def calculate_nucleus_level(competency_levels: list[float]) -> float:
    """
    Calculates the nucleus level as the simple arithmetic average
    of competency normalized levels (1–5).
    """

    if not competency_levels:
        raise DomainError("Cannot calculate nucleus level with no competencies")

    return sum(competency_levels) / len(competency_levels)
