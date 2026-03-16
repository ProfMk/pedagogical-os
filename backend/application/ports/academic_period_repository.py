from uuid import UUID


class AcademicPeriodRepository:

    def get_by_id(self, academic_period_id: UUID):
        raise NotImplementedError

    def save(self, period) -> None:
        raise NotImplementedError
