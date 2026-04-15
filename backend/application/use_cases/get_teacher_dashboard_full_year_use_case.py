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
        teacher_id: UUID
    ) -> TeacherDashboardResponse:

        dataset = self.repository.get_teacher_dashboard_dataset(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            institutional_user_id=teacher_id,
        )

        # 🔥 reutilizamos EXACTAMENTE el mismo aggregation
        # pero SIN periodo

        if not dataset:
            return TeacherDashboardResponse(
                groups=[],
                alerts=[],
                period=None  # 👈 clave
            )

        groups_map: dict = {}

        for row in dataset:
            group_id = row["group_id"]
            student_id = row["student_id"]
            indicator_id = row["indicator_id"]
            indicator_description = row["indicator_description"]

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
                    "indicators_map": {},
                },
            )

            if indicator_id is None or indicator_description is None:
                continue

            indicators_map = student_entry["indicators_map"]

            if indicator_id not in indicators_map:
                indicators_map[indicator_id] = {
                    "indicator_id": indicator_id,
                    "indicator_description": indicator_description,
                    "currentStage": row["current_stage_order"],
                    "totalStages": row["total_stages"],
                    "consolidation": row["consolidation_score"],
                    "normalizedLevel": row["normalized_level_internal"],
                }

        groups = []

        for group in groups_map.values():
            students = []

            for student in group["students_map"].values():
                students.append({
                    "studentId": student["studentId"],
                    "studentName": student["studentName"],
                    "indicators": list(student["indicators_map"].values())
                })

            groups.append({
                "groupId": group["groupId"],
                "groupName": group["groupName"],
                "students": students
            })

        return TeacherDashboardResponse(
            groups=groups,
            alerts=[],
            period=None  # 🔥 FULL YEAR → SIN PERIODO
        )
