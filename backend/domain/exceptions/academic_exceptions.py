# backend/domain/exceptions/academic_exceptions.py


class AcademicYearError(Exception):
    """Raised when an AcademicYear business rule is violated."""
    pass


class AcademicPeriodError(Exception):
    """Raised when an AcademicPeriod business rule is violated."""
    pass


class AcademicLevelError(Exception):
    """Raised when an AcademicLevel business rule is violated."""
    pass


class StudentEnrollmentError(Exception):
    """Raised when a StudentEnrollment business rule is violated."""
    pass