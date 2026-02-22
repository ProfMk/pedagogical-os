from uuid import UUID
from dataclasses import dataclass


@dataclass(frozen=True)
class StudentIndicatorProgress:
    """
    Domain entity representing the current consolidated state
    of a student for a specific indicator.

    This entity is READ-ONLY from the dashboard perspective.
    Any mutation must occur through domain services or engines.
    """

    student_id: UUID
    indicator_id: UUID

    current_stage_order: int
    consolidation_score: float
