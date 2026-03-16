from tests.builders.indicator_builder import build_indicator
from tests.builders.evidence_builder import build_evidence
from tests.builders.progress_builder import build_progress


def build_indicator_progress(
    session,
    competency_id,
    student_id,
    academic_year_id,
    scores=[90, 85, 88]
):

    indicator, stages = build_indicator(session, competency_id)

    stage = stages[0]

    evidences = build_evidence(
        session,
        student_id,
        indicator.id,
        stage.id,
        academic_year_id,
        scores
    )

    progress = build_progress(
        session,
        student_id,
        indicator.id,
        academic_year_id,
        stage_order=1
    )

    return {
        "indicator": indicator,
        "stage": stage,
        "evidences": evidences,
        "progress": progress,
    }
