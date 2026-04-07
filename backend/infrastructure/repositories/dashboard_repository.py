from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.application.ports.dashboard_repository_port import DashboardRepositoryPort


class DashboardRepository(DashboardRepositoryPort):
    def __init__(self, session: Session):
        self.session = session

    def get_teacher_dashboard_dataset(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        institutional_user_id: UUID,
    ) -> List[dict]:

        query = text(
            """
            SELECT
                ag.id AS group_id,
                ag.name AS group_name,

                s.id AS student_id,
                s.external_code AS student_name,

                c.description AS competency_name,

                i.id AS indicator_id,
                i.description AS indicator_name,

                ist.description AS micro_stage_name,
                ist.stage_order AS stage_order,

                i.total_stages AS total_stages,

                sip.current_stage_order AS current_stage_order,
                sip.consolidation_score AS consolidation_score,
                sip.normalized_level_internal AS normalized_level_internal

            FROM teacher_subject_assignment tsa

            JOIN institutional_user iu
                ON iu.id = tsa.institutional_user_id

            JOIN institutional_user_role iur
                ON iur.institutional_user_id = iu.id
                AND iur.academic_year_id = tsa.academic_year_id
                AND iur.is_active = true

            JOIN role r
                ON r.id = iur.role_id
                AND r.code = 'TEACHER'

            JOIN subject_group sg
                ON sg.id = tsa.subject_group_id

            JOIN academic_group ag
                ON ag.id = sg.academic_group_id

            JOIN academic_year ay
                ON ay.id = ag.academic_year_id

            JOIN student_enrollment se
                ON se.academic_group_id = ag.id
                AND se.academic_year_id = ag.academic_year_id

            JOIN student s
                ON s.id = se.student_id

            LEFT JOIN student_indicator_progress sip
                ON sip.student_id = s.id
                AND sip.academic_year_id = se.academic_year_id

            LEFT JOIN indicator i
                ON i.id = sip.indicator_id

            LEFT JOIN competency c
                ON c.id = i.competency_id

            LEFT JOIN indicator_stage ist
                ON ist.indicator_id = i.id
                AND ist.stage_order = sip.current_stage_order

            WHERE
                ay.institution_id = :institution_id
                AND ag.academic_year_id = :academic_year_id
                AND tsa.academic_year_id = :academic_year_id
                AND tsa.is_active = true
                AND tsa.institutional_user_id = :institutional_user_id

            ORDER BY
                c.id NULLS LAST,
                i.id NULLS LAST,
                s.id,
                ist.stage_order NULLS LAST;
            """
        )

        result = self.session.execute(
            query,
            {
                "institution_id": institution_id,
                "academic_year_id": academic_year_id,
                "institutional_user_id": institutional_user_id,
            },
        )

        # 🔥 OPTIMIZACIÓN CRÍTICA
        rows = result.mappings().all()

        return rows  # ← YA SON dict-like, NO convertir


    def get_full_year_student_progress_flat(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
    ) -> List[dict]:

        query = text(
            """
            SELECT
                ag.id AS group_id,
                ag.name AS group_name,

                s.id AS student_id,
                s.external_code AS student_name,

                n.id AS nucleus_id,
                n.name AS nucleus_name,

                c.id AS competence_id,
                c.description AS competence_name,

                i.id AS indicator_id,
                i.description AS indicator_name,
                i.total_stages AS total_stages,

                sip.current_stage_order AS current_stage_order,
                sip.consolidation_score AS consolidation_score,
                sip.normalized_level_internal AS normalized_level_internal

            FROM teacher_subject_assignment tsa

            JOIN institutional_user iu
                ON iu.id = tsa.institutional_user_id

            JOIN institutional_user_role iur
                ON iur.institutional_user_id = iu.id
                AND iur.academic_year_id = tsa.academic_year_id
                AND iur.is_active = true

            JOIN role r
                ON r.id = iur.role_id
                AND r.code = 'TEACHER'

            JOIN subject_group sg
                ON sg.id = tsa.subject_group_id

            JOIN academic_group ag
                ON ag.id = sg.academic_group_id

            JOIN academic_year ay
                ON ay.id = ag.academic_year_id

            JOIN student_enrollment se
                ON se.academic_group_id = ag.id
                AND se.academic_year_id = ag.academic_year_id

            JOIN student s
                ON s.id = se.student_id

            LEFT JOIN student_indicator_progress sip
                ON sip.student_id = s.id
                AND sip.academic_year_id = se.academic_year_id

            LEFT JOIN indicator i
                ON i.id = sip.indicator_id

            LEFT JOIN competency c
                ON c.id = i.competency_id

            LEFT JOIN nucleus n
                ON n.id = c.nucleus_id

            WHERE
                ay.institution_id = :institution_id
                AND ag.academic_year_id = :academic_year_id
                AND tsa.academic_year_id = :academic_year_id
                AND tsa.is_active = true
                AND tsa.institutional_user_id = :teacher_id

            ORDER BY
                ag.id,
                s.id,
                n.name NULLS LAST,
                c.description NULLS LAST,
                i.id NULLS LAST;
            """
        )

        result = self.session.execute(
            query,
            {
                "institution_id": institution_id,
                "academic_year_id": academic_year_id,
                "teacher_id": teacher_id,
            },
        )

        return result.mappings().all()

    # ---------------------------------------
    # ACTIVE ACADEMIC PERIOD
    # ---------------------------------------

    def get_active_academic_period(
        self,
        academic_year_id: UUID,
    ) -> dict | None:

        query = text(
            """
            SELECT
                ap.id,
                ap.name,
                ap.start_date,
                ap.end_date,
                ap.is_closed
            FROM academic_period ap
            WHERE
                ap.academic_year_id = :academic_year_id
                AND ap.is_closed = false
            LIMIT 1
            """
        )

        result = self.session.execute(
            query,
            {"academic_year_id": academic_year_id},
        )

        row = result.mappings().first()

        if row is None:
            return None

        return row  # ← también evitar dict(row)