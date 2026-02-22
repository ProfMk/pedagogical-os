# domain/rules/stage_promotion_rule.py

def evaluate_stage_promotion(
    current_stage: int,
    evidences: list,
    consolidation_score: float,
) -> int:
    """
    Domain rule v2.0:
    Promote stage if:
    - >= 3 evidences
    - all scores >= 80
    - consolidation >= 0.80
    - EITHER stable trend (no drops)
      OR single drop with sufficient prior stability
    """

    # 1. At least 3 evidences
    if len(evidences) < 3:
        return current_stage

    # 2. All evidences must have score >= 80
    for evidence in evidences:
        if evidence["score"] < 80:
            return current_stage

    # 3. Consolidation threshold
    if consolidation_score < 0.80:
        return current_stage

    # 4. Order evidences by time
    ordered = sorted(evidences, key=lambda e: e["timestamp"])
    scores = [e["score"] for e in ordered]

    # 5. Detect drops
    drop_indices = []
    for i in range(1, len(scores)):
        if scores[i] < scores[i - 1]:
            drop_indices.append(i)

    # Case A: no drops → promote
    if len(drop_indices) == 0:
        return current_stage + 1

    # Case B: more than one drop → block
    if len(drop_indices) > 1:
        return current_stage

    # Case C: exactly one drop → check prior stability
    drop_index = drop_indices[0]

    # Need at least 2 evidences BEFORE the drop
    if drop_index < 2:
        return current_stage

    # Check non-decreasing prior stability
    prior_scores = scores[:drop_index]
    for i in range(1, len(prior_scores)):
        if prior_scores[i] < prior_scores[i - 1]:
            return current_stage

    # Prior stability sufficient → promote
    return current_stage + 1
