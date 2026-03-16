from abc import ABC, abstractmethod
from uuid import UUID


class DashboardRepositoryPort(ABC):

    @abstractmethod
    def get_teacher_dashboard_dataset(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
    ):
        pass