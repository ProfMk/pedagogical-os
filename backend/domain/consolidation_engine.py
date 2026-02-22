from typing import List


MAX_EVIDENCES = 5
DEFAULT_WEIGHTS = [3, 2, 2, 1, 1]


def calculate_consolidation(
    evidences: List[float],
    weights: List[int] = DEFAULT_WEIGHTS,
) -> float:
    """
    Calculates the consolidation score for an indicator stage using
    a weighted moving window of evidences.

    Rules (Mes 1 – Point 4):
    - Uses at most the 5 most recent evidences.
    - If fewer than 5 evidences exist, uses only the available ones.
    - Applies weights in order [3, 2, 2, 1, 1].
    - Returns 0.0 if no evidences are provided.
    - Result is a float between 0.0 and 1.0.

    This function is pure domain logic:
    - No database access
    - No framework dependencies
    - Deterministic and testable
    """

    # Limit evidences to the defined moving window
    limited_evidences = evidences[:MAX_EVIDENCES]

    # Defensive rule: no evidences means no consolidation
    if not limited_evidences:
        return 0.0

    # Match weights to the number of evidences used
    limited_weights = weights[:len(limited_evidences)]

    total_weighted_score = 0.0
    total_weight = 0

    for score, weight in zip(limited_evidences, limited_weights):
        total_weighted_score += score * weight
        total_weight += weight

    return total_weighted_score / total_weight

