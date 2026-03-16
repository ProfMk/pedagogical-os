import uuid
from datetime import datetime

from backend.infrastructure.orm.indicator_orm import IndicatorORM
from backend.infrastructure.orm.indicator_stage_orm import IndicatorStageORM


def build_indicator(session, competency_id, stages=4):

    now = datetime.utcnow()

    indicator = IndicatorORM(
        id=uuid.uuid4(),
        competency_id=competency_id,
        description="Test Indicator",
        total_stages=stages,
        version_number=1,
        created_at=now,
        updated_at=now,
    )

    session.add(indicator)
    session.flush()

    stage_objects = []

    for i in range(1, stages + 1):

        stage = IndicatorStageORM(
            id=uuid.uuid4(),
            indicator_id=indicator.id,
            stage_order=i,
            description=f"Stage {i}",
            normalized_level=i,
            created_at=now,
            updated_at=now,
        )

        session.add(stage)
        stage_objects.append(stage)

    session.flush()

    return indicator, stage_objects
