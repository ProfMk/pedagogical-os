from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(frozen=True)
class StudentIndicatorDTO:
    indicator_id: UUID
    indicator_description: str
    current_stage_order: int
    consolidation_score: Decimal
