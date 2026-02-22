from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
from datetime import datetime


@dataclass
class IndicatorResult:
    id: UUID
    student_id: UUID
    indicator_id: UUID
    calculated_level: Decimal
    final_level: Decimal
    override_flag: bool
    override_comment: str | None
    created_at: datetime
    updated_at: datetime