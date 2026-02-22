from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class StudentIndicatorProgressReadDTO:
    student_id: UUID
    student_name: str

    indicator_id: UUID
    indicator_description: str

    current_stage: int
    total_stages: int

    normalized_level_internal: float
    consolidation_score: float

    has_low_consolidation_alert: bool
