from dataclasses import dataclass
from typing import List
from uuid import UUID


@dataclass(frozen=True)
class IndicatorProgressDTO:
    indicator_id: UUID
    description: str
    stage_average: float
    consolidation_average: float
    total_stages: int


@dataclass(frozen=True)
class CompetencyNodeDTO:
    competency_id: UUID
    description: str
    indicators: List[IndicatorProgressDTO]


@dataclass(frozen=True)
class NucleusNodeDTO:
    nucleus_id: UUID
    name: str
    competencies: List[CompetencyNodeDTO]


@dataclass(frozen=True)
class GroupProgressTreeResponseDTO:
    group_id: UUID
    group_name: str
    nuclei: List[NucleusNodeDTO]
