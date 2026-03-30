from uuid import UUID

from backend.application.dto.student_detail_dto import (
    CompetencyDTO,
    IndicatorDetailDTO,
    IndicatorProgressDTO,
    NucleusDTO,
    StageDTO,
    StudentDetailDTO,
)
from backend.domain.repositories.student_detail_repository import StudentDetailRepository


class GetStudentDetailUseCase:
    def __init__(self, repository: StudentDetailRepository):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        student_id: UUID,
    ) -> StudentDetailDTO:
        rows = self.repository.get_student_detail(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            student_id=student_id,
        )

        if not rows:
            raise ValueError("Student detail not found")

        first_row = rows[0]

        nuclei_map: dict[UUID, dict] = {}

        for row in rows:
            nucleus_id = row["nucleus_id"]
            competency_id = row["competency_id"]
            indicator_id = row["indicator_id"]

            nucleus_entry = nuclei_map.setdefault(
                nucleus_id,
                {
                    "dto": NucleusDTO(
                        nucleusId=nucleus_id,
                        nucleusName=row["nucleus_name"],
                        competencies=[],
                    ),
                    "competencies": {},
                },
            )

            competency_map: dict[UUID, dict] = nucleus_entry["competencies"]
            competency_entry = competency_map.setdefault(
                competency_id,
                {
                    "dto": CompetencyDTO(
                        competencyId=competency_id,
                        competencyDescription=row["competency_description"],
                        indicators=[],
                    ),
                    "indicators": {},
                },
            )

            indicator_map: dict[UUID, dict] = competency_entry["indicators"]
            indicator_entry = indicator_map.setdefault(
                indicator_id,
                {
                    "dto": IndicatorDetailDTO(
                        indicatorId=indicator_id,
                        indicatorDescription=row["indicator_description"],
                        progress=IndicatorProgressDTO(
                            currentStage=row["current_stage"],
                            totalStages=row["total_stages"],
                            consolidation=(
                                float(row["consolidation"])
                                if row["consolidation"] is not None
                                else None
                            ),
                        ),
                        stages=[],
                    )
                },
            )

            if row["stage_number"] is not None:
                indicator_entry["dto"].stages.append(
                    StageDTO(
                        stageNumber=row["stage_number"],
                        consolidation=(
                            float(row["stage_consolidation"])
                            if row["stage_consolidation"] is not None
                            else None
                        ),
                        evidenceCount=row["evidence_count"],
                    )
                )

        nuclei = []

        for nucleus_id in sorted(nuclei_map):
            nucleus_entry = nuclei_map[nucleus_id]
            competencies = []

            for competency_id in sorted(nucleus_entry["competencies"]):
                competency_entry = nucleus_entry["competencies"][competency_id]
                indicators = []

                for indicator_id in sorted(competency_entry["indicators"]):
                    indicator_entry = competency_entry["indicators"][indicator_id]
                    indicators.append(indicator_entry["dto"])

                competency_entry["dto"].indicators = indicators
                competencies.append(competency_entry["dto"])

            nucleus_entry["dto"].competencies = competencies
            nuclei.append(nucleus_entry["dto"])

        return StudentDetailDTO(
            studentId=first_row["student_id"],
            studentName=first_row["student_name"],
            nuclei=nuclei,
        )
