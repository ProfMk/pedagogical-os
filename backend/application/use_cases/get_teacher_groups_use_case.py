from uuid import UUID

from backend.application.dto.teacher_dashboard_dto import (
    GroupDashboardDTO,
    IndicatorDashboardDTO,
    StudentDashboardDTO,
    TeacherDashboardResponse,
)


class GetTeacherGroupsUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
    ) -> TeacherDashboardResponse:

        dataset = self.repository.get_teacher_dashboard_dataset(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
        )

        groups_map: dict = {}

        for row in dataset:
            group_id = row["group_id"]
            student_id = row["student_id"]
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
                    "indicators_map": {},
                },
            )

            if indicator_id not in student_entry["indicators_map"]:
                student_entry["indicators_map"][indicator_id] = IndicatorDashboardDTO(
                    indicatorId=indicator_id,
                    indicatorName=row.get("indicator_name"),
                    microStageName=row.get("micro_stage_name"),
                    currentStage=row["current_stage_order"],
                    totalStages=row["total_stages"],
                    consolidation=row["consolidation_score"],
                    normalizedLevel=row["normalized_level_internal"],
                )

        groups = []

        for group_entry in groups_map.values():

            students = []

            for student_entry in group_entry["students_map"].values():

                indicators = list(student_entry["indicators_map"].values())

                students.append(
                    StudentDashboardDTO(
                        studentId=student_entry["studentId"],
                        studentName=student_entry["studentName"],
                        indicators=indicators,
                    )
                )

            groups.append(
                GroupDashboardDTO(
                    groupId=group_entry["groupId"],
                    groupName=group_entry["groupName"],
                    students=students,
                )
            )

        return TeacherDashboardResponse(
            groups=groups,
            alerts=[],
        )