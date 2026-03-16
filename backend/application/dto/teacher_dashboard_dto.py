from typing import List
from uuid import UUID

from pydantic import BaseModel


class IndicatorDashboardDTO(BaseModel):
    indicatorId: UUID
    competencyName: str | None = None
    indicatorName: str | None = None
    microStageName: str | None = None
    currentStage: int
    totalStages: int
    consolidation: float | None
    normalizedLevel: float | None


class StudentDashboardDTO(BaseModel):
    studentId: UUID
    studentName: str | None
    indicators: List[IndicatorDashboardDTO]


class GroupDashboardDTO(BaseModel):
    groupId: UUID
    groupName: str
    students: List[StudentDashboardDTO]


class TeacherDashboardResponse(BaseModel):
    groups: List[GroupDashboardDTO]
    alerts: List