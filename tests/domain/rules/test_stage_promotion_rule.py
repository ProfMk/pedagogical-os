# tests/domain/rules/test_stage_promotion_rule.py

from datetime import datetime, timedelta
from domain.rules.stage_promotion_rule import evaluate_stage_promotion


def test_should_not_promote_stage_if_less_than_three_valid_evidences():
    """
    Rule:
    - Stage promotion requires at least 3 evidences with score >= 80
    - Consolidation alone is NOT sufficient
    """

    current_stage = 2

    evidences = [
        {"score": 85, "timestamp": datetime.now() - timedelta(days=1)},
        {"score": 90, "timestamp": datetime.now() - timedelta(days=2)},
    ]

    consolidation_score = 0.92

    new_stage = evaluate_stage_promotion(
        current_stage=current_stage,
        evidences=evidences,
        consolidation_score=consolidation_score,
    )

    assert new_stage == current_stage

def test_should_not_promote_stage_if_any_evidence_is_below_80():
    """
    Rule:
    - Requires at least 3 evidences
    - ALL evidences must have score >= 80
    """

    current_stage = 2

    evidences = [
        {"score": 85, "timestamp": datetime.now() - timedelta(days=1)},
        {"score": 90, "timestamp": datetime.now() - timedelta(days=2)},
        {"score": 70, "timestamp": datetime.now() - timedelta(days=3)},  # Invalid
    ]

    consolidation_score = 0.95

    new_stage = evaluate_stage_promotion(
        current_stage=current_stage,
        evidences=evidences,
        consolidation_score=consolidation_score,
    )

    assert new_stage == current_stage

def test_should_promote_stage_when_all_conditions_are_met():
    """
    Rule:
    - At least 3 evidences
    - All scores >= 80
    - Consolidation >= 0.80
    - Stable trend (non-decreasing scores)
    """

    current_stage = 2

    evidences = [
        {"score": 80, "timestamp": datetime.now() - timedelta(days=3)},
        {"score": 85, "timestamp": datetime.now() - timedelta(days=2)},
        {"score": 90, "timestamp": datetime.now() - timedelta(days=1)},
    ]

    consolidation_score = 0.85

    new_stage = evaluate_stage_promotion(
        current_stage=current_stage,
        evidences=evidences,
        consolidation_score=consolidation_score,
    )

    assert new_stage == current_stage + 1

def test_should_promote_stage_with_single_drop_but_prior_stability_v2():
    """
    v2.0 Rule:
    - Single drop is allowed
    - There must be prior stability (at least 2 non-decreasing evidences before the drop)
    """

    current_stage = 2

    evidences = [
        {"score": 80, "timestamp": datetime.now() - timedelta(days=4)},
        {"score": 85, "timestamp": datetime.now() - timedelta(days=3)},  # stable
        {"score": 83, "timestamp": datetime.now() - timedelta(days=2)},  # single drop
        {"score": 86, "timestamp": datetime.now() - timedelta(days=1)},  # recovery
    ]

    consolidation_score = 0.88

    new_stage = evaluate_stage_promotion(
        current_stage=current_stage,
        evidences=evidences,
        consolidation_score=consolidation_score,
    )

    assert new_stage == current_stage + 1
