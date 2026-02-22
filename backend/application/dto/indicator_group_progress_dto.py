from uuid import UUID
from pydantic import BaseModel


class IndicatorGroupProgressDTO(BaseModel):
    indicatorId: UUID
    indicatorName: str

    stageAverage: float
    totalStages: int

    consolidationAverage: float
