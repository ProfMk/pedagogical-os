import pytest
from domain.services.stage_progression_policy import StageProgressionPolicy
from domain.exceptions.invalid_stage_jump_error import InvalidStageJumpError


# tests/domain/services/test_stage_progression_policy.py




def test_should_not_regress_stage_when_incoming_stage_is_lower():
    # Given
    current_stage = 3
    incoming_stage = 2
    total_stages = 5

    valid_evidence_count = 5
    evidence_scores = [90, 95, 85]
    consolidation_score = 0.90
    trend_stable = True

    # When
    result = StageProgressionPolicy.evaluate(
        current_stage=current_stage,
        incoming_stage=incoming_stage,
        total_stages=total_stages,
        valid_evidence_count=valid_evidence_count,
        evidence_scores=evidence_scores,
        consolidation_score=consolidation_score,
        trend_stable=trend_stable,
    )



    # Then
    assert result == current_stage
def test_should_raise_error_when_skipping_stage():
    # Given
    current_stage = 1
    incoming_stage = 3   # salto inválido
    total_stages = 5

    valid_evidence_count = 5
    evidence_scores = [90, 90, 90]
    consolidation_score = 0.95
    trend_stable = True

    # When / Then
    with pytest.raises(InvalidStageJumpError):
        StageProgressionPolicy.evaluate(
            current_stage=current_stage,
            incoming_stage=incoming_stage,
            total_stages=total_stages,
            valid_evidence_count=valid_evidence_count,
            evidence_scores=evidence_scores,
            consolidation_score=consolidation_score,
            trend_stable=trend_stable,
        )


def test_should_advance_stage_when_all_conditions_are_met():
    # Given
    current_stage = 2
    incoming_stage = 3   # intento válido: +1
    total_stages = 5

    valid_evidence_count = 3
    evidence_scores = [80, 85, 90]   # todas >= 80
    consolidation_score = 0.85       # >= 0.80
    trend_stable = True

    # When
    result = StageProgressionPolicy.evaluate(
        current_stage=current_stage,
        incoming_stage=incoming_stage,
        total_stages=total_stages,
        valid_evidence_count=valid_evidence_count,
        evidence_scores=evidence_scores,
        consolidation_score=consolidation_score,
        trend_stable=trend_stable,
    )

    # Then
    assert result == current_stage + 1

def test_should_not_advance_stage_when_consolidation_is_below_threshold():
    # Given
    current_stage = 2
    incoming_stage = 3
    total_stages = 5

    valid_evidence_count = 3
    evidence_scores = [85, 90, 95]
    consolidation_score = 0.79   # justo debajo
    trend_stable = True

    # When
    result = StageProgressionPolicy.evaluate(
        current_stage=current_stage,
        incoming_stage=incoming_stage,
        total_stages=total_stages,
        valid_evidence_count=valid_evidence_count,
        evidence_scores=evidence_scores,
        consolidation_score=consolidation_score,
        trend_stable=trend_stable,
    )

    # Then
    assert result == current_stage