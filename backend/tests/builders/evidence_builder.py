import uuid
from datetime import datetime

from backend.infrastructure.orm.student_evidence_orm import StudentEvidenceORM


def build_evidence(
    session,
    student_id,
    indicator_id,
    stage_id,
    academic_year_id,
    scores
):

    now = datetime.utcnow()

    evidences = []

    for score in scores:

        ev = StudentEvidenceORM(
            id=uuid.uuid4(),
            academic_year_id=academic_year_id,
            student_id=student_id,
            indicator_id=indicator_id,
            indicator_stage_id=stage_id,
            raw_score=score,
            created_at=now,
            updated_at=now,
        )

        session.add(ev)
        evidences.append(ev)

    session.flush()

    return evidences