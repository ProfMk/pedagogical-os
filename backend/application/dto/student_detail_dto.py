from typing import List
from uuid import UUID

from pydantic import BaseModel


class StageDTO(BaseModel):
    stageNumber: int
    consolidation: float | None
    evidenceCount: int


class IndicatorProgressDTO(BaseModel):
    currentStage: int
    totalStages: int
    consolidation: float | None


class IndicatorDetailDTO(BaseModel):
    indicatorId: UUID
    indicatorDescription: str
    progress: IndicatorProgressDTO
    stages: List[StageDTO]


class CompetencyDTO(BaseModel):
    competencyId: UUID
    competencyDescription: str
    indicators: List[IndicatorDetailDTO]


class NucleusDTO(BaseModel):
    nucleusId: UUID
    nucleusName: str
    competencies: List[CompetencyDTO]


class StudentDetailDTO(BaseModel):
    studentId: UUID
    studentName: str
    nuclei: List[NucleusDTO]
