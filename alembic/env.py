from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# 🔴 Cargar variables de entorno (.env)
load_dotenv()

# Alembic Config object
config = context.config

# 🔴 Obtener DATABASE_URL desde entorno
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise Exception("DATABASE_URL not set in environment")

config.set_main_option("sqlalchemy.url", database_url)

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata
from backend.infrastructure.orm.base import Base
target_metadata = Base.metadata

# 🔴 Importar modelos ORM (para autogenerate)
from backend.infrastructure.orm.student_orm import StudentORM
from backend.infrastructure.orm.indicator_orm import IndicatorORM
from backend.infrastructure.orm.student_indicator_progress_orm import StudentIndicatorProgressORM
from backend.infrastructure.orm.institution_orm import InstitutionORM
from backend.infrastructure.orm.academic_year_orm import AcademicYearORM
from backend.infrastructure.orm.academic_period_orm import AcademicPeriodORM
from backend.infrastructure.orm.academic_level_orm import AcademicLevelORM
from backend.infrastructure.orm.student_enrollment_orm import StudentEnrollmentORM
from backend.infrastructure.orm.subject_orm import SubjectORM
from backend.infrastructure.orm.nucleus_orm import NucleusORM
from backend.infrastructure.orm.competency_orm import CompetencyORM
from backend.infrastructure.orm.indicator_stage_orm import IndicatorStageORM
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM
from backend.infrastructure.orm.student_evidence_orm import StudentEvidenceORM


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()