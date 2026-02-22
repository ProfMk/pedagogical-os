# backend/app/domain/rules/indicator_level_rule.py

from domain.exceptions.domain_error import DomainError


def calculate_indicator_level(
    *,
    stage_index: int,
    total_stages: int,
    consolidation: float,
) -> float:
    """
    Calculates the normalized indicator level (1–5) based on:
    - current micro-stage
    - total number of micro-stages
    - consolidation score (0–1)

    Pure domain rule.
    """

    if total_stages < 1:
        raise DomainError("Total stages must be at least 1")

    if stage_index < 1 or stage_index > total_stages:
        raise DomainError("Stage index is out of valid range")

    if consolidation < 0 or consolidation > 1:
        raise DomainError("Consolidation must be between 0 and 1")

    stage_span = 4 / total_stages
    stage_min = 1 + (stage_index - 1) * stage_span

    normalized_level = stage_min + (consolidation * stage_span)

    # Final guardrail: absolute range [1, 5]
    if normalized_level < 1 or normalized_level > 5:
        raise DomainError("Normalized level must be between 1 and 5")

    return normalized_level
