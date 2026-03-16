from uuid import UUID
from sqlalchemy.orm import Session

from backend.application.ports.academic_period_repository import (
    AcademicPeriodRepository
)

from backend.infrastructure.orm.academic_period_orm import (
    AcademicPeriodORM
)


class AcademicPeriodRepositoryORM(AcademicPeriodRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, academic_period_id: UUID):

        return (
            self.session.query(AcademicPeriodORM)
            .filter(AcademicPeriodORM.id == academic_period_id)
            .first()
        )

    def save(self, academic_period):

        self.session.add(academic_period)
        self.session.commit()

        return academic_period
