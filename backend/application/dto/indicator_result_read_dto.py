from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
from typing import Optional


@dataclass
class IndicatorResultReadDTO:
    academic_year_id: UUID
    student_id: UUID
    indicator_id: UUID

    calculated_level: Decimal
    final_level: Decimal

    override_flag: bool
    override_comment: Optional[str]