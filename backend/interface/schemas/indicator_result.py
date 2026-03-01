from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class IndicatorResultOverrideRequest(BaseModel):
    academic_year_id: UUID
    student_id: UUID
    indicator_id: UUID
    new_final_level: Decimal
    override_comment: str


class IndicatorResultResponse(BaseModel):
    id: UUID
    academic_year_id: UUID
    student_id: UUID
    indicator_id: UUID
    calculated_level: Decimal
    final_level: Decimal
    override_flag: bool
    override_comment: str | None