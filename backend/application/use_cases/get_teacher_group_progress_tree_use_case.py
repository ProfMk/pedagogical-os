from uuid import UUID

from backend.application.dto.teacher_group_progress_tree_dto import (
    CompetencyNodeDTO,
    GroupProgressTreeResponseDTO,
    IndicatorProgressDTO,
    NucleusNodeDTO,
)
from backend.application.ports.teacher_group_progress_repository_port import (
    TeacherGroupProgressRepositoryPort,
)


class GetTeacherGroupProgressTreeUseCase:

    def __init__(self, repository: TeacherGroupProgressRepositoryPort):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
        subject_id: UUID,
        group_id: UUID,
    ) -> GroupProgressTreeResponseDTO:
        rows = self.repository.get_group_progress_tree(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            teacher_id=teacher_id,
            subject_id=subject_id,
            group_id=group_id,
        )

        if not rows:
            return GroupProgressTreeResponseDTO(
                group_id=group_id,
                group_name="",
                nuclei=[],
            )

        group_name = rows[0].get("group_name", "")
        nuclei_map: dict = {}

        for row in rows:
            nucleus_id = row["nucleus_id"]
            competency_id = row["competency_id"]

            if nucleus_id not in nuclei_map:
                nuclei_map[nucleus_id] = {
                    "nucleus_id": nucleus_id,
                    "name": row["nucleus_name"],
                    "competencies": {},
                }

            nucleus_entry = nuclei_map[nucleus_id]

            if competency_id not in nucleus_entry["competencies"]:
                nucleus_entry["competencies"][competency_id] = {
                    "competency_id": competency_id,
                    "description": row["competency_description"],
                    "indicators": [],
                }

            nucleus_entry["competencies"][competency_id]["indicators"].append(
                IndicatorProgressDTO(
                    indicator_id=row["indicator_id"],
                    description=row["indicator_description"],
                    stage_average=row["stage_average"],
                    consolidation_average=row["consolidation_average"],
                    total_stages=row["total_stages"],
                )
            )

        nuclei = []
        for nucleus in nuclei_map.values():
            competencies = []
            for competency in nucleus["competencies"].values():
                competencies.append(
                    CompetencyNodeDTO(
                        competency_id=competency["competency_id"],
                        description=competency["description"],
                        indicators=competency["indicators"],
                    )
                )

            nuclei.append(
                NucleusNodeDTO(
                    nucleus_id=nucleus["nucleus_id"],
                    name=nucleus["name"],
                    competencies=competencies,
                )
            )

        return GroupProgressTreeResponseDTO(
            group_id=group_id,
            group_name=group_name,
            nuclei=nuclei,
        )
