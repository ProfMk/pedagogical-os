from enum import Enum


class AcademicPeriodEventType(str, Enum):
    PERIOD_CLOSED = "PERIOD_CLOSED"
    PERIOD_REOPENED = "PERIOD_REOPENED"
