from typing import List
from datetime import date
from uuid import UUID

from pydantic import BaseModel, Field


class IndicatorDashboardDTO(BaseModel):
    indicator_id: UUID = Field(exclude=True)
    indicator_description: str
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


# -----------------------------
# NEW DTOs — PERIOD STATE
# -----------------------------

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
