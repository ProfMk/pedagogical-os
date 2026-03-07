class InMemorySession:

    def __init__(self):
        self.items = []
        self.committed = False

    def add(self, item):
        self.items.append(item)

    def commit(self):
        self.committed = True


class FakeIndicatorResultRepository:

    def get_all_by_period(self, academic_period_id):
        return []


class FakeEnrollmentRepository:

    def get_active_students(self, academic_year_id):
        return []


class FakeReportCardRepository:

    def save_nucleus_results(self, results):
        pass

    def save_subject_results(self, results):
        pass