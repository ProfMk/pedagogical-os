from uuid import UUID

from backend.application.dto.teacher_dashboard_dto import TeacherDashboardResponse
from backend.application.ports.dashboard_repository_port import DashboardRepositoryPort


class GetTeacherDashboardFullYearUseCase:

    def __init__(self, repository: DashboardRepositoryPort):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
    ) -> TeacherDashboardResponse:

        dataset = self.repository.get_full_year_student_progress_flat(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            teacher_id=teacher_id,
        )

        if not dataset:
            return TeacherDashboardResponse(
                groups=[],
                alerts=[],
                period=None,
            )

        groups_map: dict = {}

        for row in dataset:
            group_id = row["group_id"]
            student_id = row["student_id"]
            nucleus_id = row["nucleus_id"]
            competence_id = row["competence_id"]
            indicator_id = row["indicator_id"]

            group_entry = groups_map.setdefault(
                group_id,
                {
                    "groupId": group_id,
                    "groupName": row["group_name"],
                    "students_map": {},
                },
            )

            student_entry = group_entry["students_map"].setdefault(
                student_id,
                {
                    "studentId": student_id,
                    "studentName": row["student_name"],
                    "nucleus_map": {},
                    "indicators_map": {},
                },
            )

            if indicator_id is None or nucleus_id is None or competence_id is None:
                continue

            nucleus_entry = student_entry["nucleus_map"].setdefault(
                nucleus_id,
                {
                    "nucleusId": nucleus_id,
                    "nucleusName": row["nucleus_name"],
                    "competences_map": {},
                    "normalized_sum": 0.0,
                    "normalized_count": 0,
                },
            )

            competence_entry = nucleus_entry["competences_map"].setdefault(
                competence_id,
                {
                    "competenceId": competence_id,
                    "competenceName": row["competence_name"],
                    "indicators_map": {},
                    "normalized_sum": 0.0,
                    "normalized_count": 0,
                },
            )

            if indicator_id in competence_entry["indicators_map"]:
                continue

            indicator = {
                "indicatorId": indicator_id,
                "currentStage": row["current_stage_order"],
                "totalStages": row["total_stages"],
                "consolidation": row["consolidation_score"],
                "normalizedLevel": row["normalized_level_internal"],
            }

            competence_entry["indicators_map"][indicator_id] = indicator
            student_entry["indicators_map"][indicator_id] = indicator

            normalized_level = row["normalized_level_internal"]
            if normalized_level is not None:
                competence_entry["normalized_sum"] += normalized_level
                competence_entry["normalized_count"] += 1
                nucleus_entry["normalized_sum"] += normalized_level
                nucleus_entry["normalized_count"] += 1

        groups = []

        for group in groups_map.values():
            students = []

            for student in group["students_map"].values():
                nucleus = []

                for nucleus_entry in student["nucleus_map"].values():
                    competences = []

                    for competence_entry in nucleus_entry["competences_map"].values():
                        normalized_count = competence_entry["normalized_count"]
                        average_normalized_level = (
                            competence_entry["normalized_sum"] / normalized_count
                            if normalized_count > 0
                            else None
                        )

                        competences.append(
                            {
                                "competenceId": competence_entry["competenceId"],
                                "competenceName": competence_entry["competenceName"],
                                "indicators": list(competence_entry["indicators_map"].values()),
                                "averageNormalizedLevel": average_normalized_level,
                                "indicatorCount": len(competence_entry["indicators_map"]),
                            }
                        )

                    nucleus_normalized_count = nucleus_entry["normalized_count"]
                    nucleus_average = (
                        nucleus_entry["normalized_sum"] / nucleus_normalized_count
                        if nucleus_normalized_count > 0
                        else None
                    )

                    nucleus.append(
                        {
                            "nucleusId": nucleus_entry["nucleusId"],
                            "nucleusName": nucleus_entry["nucleusName"],
                            "competences": competences,
                            "averageNormalizedLevel": nucleus_average,
                            "competenceCount": len(nucleus_entry["competences_map"]),
                        }
                    )

                students.append(
                    {
                        "studentId": student["studentId"],
                        "studentName": student["studentName"],
                        "nucleus": nucleus,
                        "indicators": list(student["indicators_map"].values()),
                    }
                )

            groups.append(
                {
                    "groupId": group["groupId"],
                    "groupName": group["groupName"],
                    "students": students,
                }
            )

        return TeacherDashboardResponse(
            groups=groups,
            alerts=[],
            period=None,
        )
