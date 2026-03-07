import uuid
from datetime import datetime

from backend.infrastructure.orm.student_indicator_progress_orm import (
    StudentIndicatorProgressORM
)


def build_progress(
    session,
    student_id,
    indicator_id,
    academic_year_id,
    stage_order=1,
):

    now = datetime.utcnow()

    progress = StudentIndicatorProgressORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year_id,
        student_id=student_id,
        indicator_id=indicator_id,
        current_stage_order=stage_order,
        consolidation_score=0.0,
        normalized_level_internal=stage_order,
        created_at=now,
        updated_at=now,
    )

    session.add(progress)
    session.flush()

    return progress