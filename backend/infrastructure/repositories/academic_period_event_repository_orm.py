from sqlalchemy.orm import Session

from backend.application.ports.academic_period_event_repository import (
    AcademicPeriodEventRepository,
)
from backend.infrastructure.orm.academic_period_event_orm import AcademicPeriodEventORM


class AcademicPeriodEventRepositoryORM(AcademicPeriodEventRepository):

    def __init__(self, session: Session):
        self._session = session

    def save(self, event):
        orm_obj = AcademicPeriodEventORM(
            id=event.id,
            academic_period_id=event.academic_period_id,
            event_type=event.event_type.value,
            reason=event.reason,
            performed_by_user_id=event.performed_by_user_id,
            created_at=event.created_at,
        )

        self._session.add(orm_obj)
        self._session.commit()
