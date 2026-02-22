from typing import Final

from domain.exceptions.domain_error import DomainError


MAX_CONSOLIDATION_WEIGHT: Final[float] = 0.3


def calculate_indicator_internal_level(
    stage_base_level: float,
    consolidation_score: float,
    consolidation_weight: float,
) -> float:
    """
    Calculates the internal normalized level for an indicator.

    Domain rule:
    - The consolidation impact is strictly limited.
    - This function is pure and deterministic.

    Pedagogical guardrail:
    The consolidation_weight MUST NOT exceed 0.3.
    Any value above this limit requires a major pedagogical version change.
    """

    if not 1.0 <= stage_base_level <= 5.0:
        raise DomainError(
            f"stage_base_level out of bounds: {stage_base_level}"
        )

    if not 0.0 <= consolidation_score <= 1.0:
        raise DomainError(
            f"consolidation_score out of bounds: {consolidation_score}"
        )

    if not 0.0 < consolidation_weight <= MAX_CONSOLIDATION_WEIGHT:
        raise DomainError(
            f"consolidation_weight out of bounds: {consolidation_weight}. "
            f"Maximum allowed is {MAX_CONSOLIDATION_WEIGHT}"
        )

    return stage_base_level + (consolidation_score * consolidation_weight)
