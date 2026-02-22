from uuid import UUID
from pydantic import BaseModel


class StudentIndicatorProgressResponse(BaseModel):
    studentId: UUID
    studentName: str

    indicatorId: UUID
    indicatorDescription: str

    currentStage: int
    totalStages: int

    normalizedLevelInternal: float
    consolidationScore: float

    hasLowConsolidationAlert: bool

    class Config:
        orm_mode = True
