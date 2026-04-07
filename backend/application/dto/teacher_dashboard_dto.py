from datetime import date
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field


class IndicatorDashboardDTO(BaseModel):
    indicatorId: UUID
    currentStage: int
    totalStages: int
    consolidation: float | None
    normalizedLevel: float | None


class CompetenceDashboardDTO(BaseModel):
    competenceId: UUID
    competenceName: str
    indicators: List[IndicatorDashboardDTO]
    averageNormalizedLevel: float | None = None
    indicatorCount: int = 0


class NucleusDashboardDTO(BaseModel):
    nucleusId: UUID
    nucleusName: str
    competences: List[CompetenceDashboardDTO]
    averageNormalizedLevel: float | None = None
    competenceCount: int = 0


class StudentDashboardDTO(BaseModel):
    studentId: UUID
    studentName: str | None
    indicators: List[IndicatorDashboardDTO] = Field(default_factory=list)
    nucleus: List[NucleusDashboardDTO] = Field(default_factory=list)


class GroupDashboardDTO(BaseModel):
    groupId: UUID
    groupName: str
    students: List[StudentDashboardDTO]


class TimelineContextDTO(BaseModel):
    startDate: date
    endDate: date


class PeriodStateDTO(BaseModel):
    activePeriodId: UUID
    periodName: str
    periodStatus: str
    timelineContext: TimelineContextDTO


class TeacherDashboardResponse(BaseModel):
    groups: List[GroupDashboardDTO]
    alerts: List
    period: PeriodStateDTO | None = None
