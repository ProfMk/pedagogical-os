from typing import List
from domain.exceptions.invalid_stage_jump_error import InvalidStageJumpError


class StageProgressionPolicy:
    @staticmethod
    def evaluate(
        current_stage: int,
        incoming_stage: int,
        total_stages: int,
        valid_evidence_count: int,
        evidence_scores: List[int],
        consolidation_score: float,
        trend_stable: bool,
    ) -> int:
        if incoming_stage < 1 or incoming_stage > total_stages:
            raise InvalidStageJumpError()

        if incoming_stage <= current_stage:
            return current_stage

        if incoming_stage > current_stage + 1:
            raise InvalidStageJumpError()

        if valid_evidence_count < 3:
            return current_stage

        if any(score < 80 for score in evidence_scores):
            return current_stage

        if consolidation_score < 0.80:
            return current_stage

        if not trend_stable:
            return current_stage

        return current_stage + 1
