import uuid
from datetime import datetime
from backend.infrastructure.orm.student_orm import StudentORM


def create_student(session, institution_id):

    now = datetime.utcnow()

    student = StudentORM(
        id=uuid.uuid4(),
        institution_id=institution_id,
        external_code="TEST_STUDENT",
        created_at=now,
        updated_at=now,
    )

    session.add(student)
    session.flush()

    return student
