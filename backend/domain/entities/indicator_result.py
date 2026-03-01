from dataclasses import dataclass
from uuid import UUID
from decimal import Decimal
from datetime import datetime
from typing import Optional


@dataclass
class IndicatorResult:

    id: UUID
    academic_year_id: UUID
    student_id: UUID
    indicator_id: UUID

    calculated_level: Decimal
    final_level: Decimal
    override_flag: bool
    override_comment: Optional[str]

    created_at: datetime
    updated_at: datetime

    def apply_override(self, new_final_level: Decimal, comment: Optional[str]) -> None:
        """
        Applies teacher override without modifying calculated level.
        """

        if new_final_level <= Decimal("0"):
            raise ValueError("Final level must be positive.")

        self.final_level = new_final_level
        self.override_flag = new_final_level != self.calculated_level
        self.override_comment = comment