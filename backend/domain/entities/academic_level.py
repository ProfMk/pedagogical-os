# backend/domain/entities/academic_level.py

from dataclasses import dataclass
from uuid import UUID
from typing import Optional

from backend.domain.exceptions.academic_exceptions import AcademicLevelError


@dataclass
class AcademicLevel:
    id: UUID
    institution_id: UUID
    name: str
    order_index: int
    education_stage: Optional[str] = None

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise AcademicLevelError("Academic level name cannot be empty")

        if self.order_index < 0:
            raise AcademicLevelError("order_index must be greater than or equal to 0")
