BEGIN;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-------------------------
-- INSTITUTION
-------------------------

INSERT INTO institution (
id,
identity,
governance,
pedagogical_framework,
organization_model,
created_at,
updated_at
)
VALUES (
uuid_generate_v4(),
'{}'::jsonb,
'{}'::jsonb,
'{}'::jsonb,
'school',
NOW(),
NOW()
);

-------------------------
-- ACADEMIC YEAR
-------------------------

INSERT INTO academic_year (
id,
institution_id,
name,
start_date,
end_date,
status,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
id,
'2026',
'2026-01-01',
'2026-12-31',
'active',
NOW(),
NOW()
FROM institution
LIMIT 1;

-------------------------
-- ACADEMIC LEVEL
-------------------------

INSERT INTO academic_level (
id,
institution_id,
name,
order_index,
education_stage,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
id,
'Primary',
1,
'primary',
NOW(),
NOW()
FROM institution;

-------------------------
-- GRADE
-------------------------

INSERT INTO academic_grade (
id,
institution_id,
academic_level_id,
name,
order_index,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
i.id,
al.id,
'Grade 5',
1,
NOW(),
NOW()
FROM institution i
JOIN academic_level al ON al.institution_id = i.id
LIMIT 1;

-------------------------
-- GROUP
-------------------------

INSERT INTO academic_group (
id,
academic_year_id,
academic_grade_id,
name,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
ay.id,
ag.id,
'5A',
NOW(),
NOW()
FROM academic_year ay
JOIN academic_grade ag ON TRUE
LIMIT 1;

-------------------------
-- SUBJECTS
-------------------------

INSERT INTO subject (
id,
institution_id,
name,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Mathematics', NOW(), NOW() FROM institution;

INSERT INTO subject (
id,
institution_id,
name,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Language', NOW(), NOW() FROM institution;

INSERT INTO subject (
id,
institution_id,
name,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Science', NOW(), NOW() FROM institution;

-------------------------
-- SUBJECT GROUP
-------------------------

INSERT INTO subject_group (
id,
academic_year_id,
subject_id,
academic_group_id,
name,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
ay.id,
s.id,
ag.id,
s.name || ' - 5A',
NOW(),
NOW()
FROM subject s
JOIN academic_year ay ON TRUE
JOIN academic_group ag ON TRUE;

-------------------------
-- TEACHER
-------------------------

INSERT INTO institutional_user (
id,
institution_id,
email,
password_hash,
full_name,
is_active,
is_superadmin,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
id,
'teacher@test.com',
'password',
'Teacher Demo',
true,
false,
NOW(),
NOW()
FROM institution;

-------------------------
-- TEACHER ASSIGNMENT
-------------------------

INSERT INTO teacher_subject_assignment (
id,
academic_year_id,
institutional_user_id,
subject_group_id,
is_active,
assigned_at,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
ay.id,
u.id,
sg.id,
true,
NOW(),
NOW(),
NOW()
FROM academic_year ay
JOIN institutional_user u ON TRUE
JOIN subject_group sg ON TRUE;

-------------------------
-- CURRICULUM VERSION
-------------------------

INSERT INTO curriculum_version (
id,
institution_id,
academic_year_id,
academic_level_id,
academic_grade_id,
subject_id,
version_number,
status,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
i.id,
ay.id,
al.id,
ag.id,
s.id,
1,
'active',
NOW(),
NOW()
FROM subject s
JOIN institution i ON TRUE
JOIN academic_year ay ON TRUE
JOIN academic_level al ON TRUE
JOIN academic_grade ag ON TRUE;

-------------------------
-- NUCLEUS
-------------------------

INSERT INTO nucleus (
id,
name,
description,
curriculum_version_id,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
'Nucleus A',
'Core Skills',
cv.id,
NOW(),
NOW()
FROM curriculum_version cv;

INSERT INTO nucleus (
id,
name,
description,
curriculum_version_id,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
'Nucleus B',
'Advanced Skills',
cv.id,
NOW(),
NOW()
FROM curriculum_version cv;

-------------------------
-- COMPETENCIES
-------------------------

INSERT INTO competency (
id,
nucleus_id,
description,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Competency 1', NOW(), NOW() FROM nucleus;

INSERT INTO competency (
id,
nucleus_id,
description,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Competency 2', NOW(), NOW() FROM nucleus;

-------------------------
-- INDICATORS
-------------------------

INSERT INTO indicator (
id,
competency_id,
description,
total_stages,
version_number,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Indicator A', 4, 1, NOW(), NOW() FROM competency;

INSERT INTO indicator (
id,
competency_id,
description,
total_stages,
version_number,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Indicator B', 4, 1, NOW(), NOW() FROM competency;

INSERT INTO indicator (
id,
competency_id,
description,
total_stages,
version_number,
created_at,
updated_at
)
SELECT uuid_generate_v4(), id, 'Indicator C', 4, 1, NOW(), NOW() FROM competency;

-------------------------
-- INDICATOR STAGES
-------------------------

INSERT INTO indicator_stage
(id,indicator_id,stage_order,description,normalized_level,created_at,updated_at)
SELECT uuid_generate_v4(), id,1,'Stage 1',1,NOW(),NOW() FROM indicator;

INSERT INTO indicator_stage
(id,indicator_id,stage_order,description,normalized_level,created_at,updated_at)
SELECT uuid_generate_v4(), id,2,'Stage 2',2,NOW(),NOW() FROM indicator;

INSERT INTO indicator_stage
(id,indicator_id,stage_order,description,normalized_level,created_at,updated_at)
SELECT uuid_generate_v4(), id,3,'Stage 3',3,NOW(),NOW() FROM indicator;

INSERT INTO indicator_stage
(id,indicator_id,stage_order,description,normalized_level,created_at,updated_at)
SELECT uuid_generate_v4(), id,4,'Stage 4',4,NOW(),NOW() FROM indicator;

-------------------------
-- STUDENTS
-------------------------

INSERT INTO student
(id,institution_id,external_code,created_at,updated_at)
SELECT uuid_generate_v4(),id,'STUDENT_ANA',NOW(),NOW() FROM institution;

INSERT INTO student
(id,institution_id,external_code,created_at,updated_at)
SELECT uuid_generate_v4(),id,'STUDENT_LUIS',NOW(),NOW() FROM institution;

INSERT INTO student
(id,institution_id,external_code,created_at,updated_at)
SELECT uuid_generate_v4(),id,'STUDENT_MARIA',NOW(),NOW() FROM institution;

INSERT INTO student
(id,institution_id,external_code,created_at,updated_at)
SELECT uuid_generate_v4(),id,'STUDENT_DIEGO',NOW(),NOW() FROM institution;

-------------------------
-- ENROLLMENT
-------------------------

INSERT INTO student_enrollment (
id,
academic_year_id,
student_id,
academic_group_id,
enrolled_at,
is_active,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
ay.id,
s.id,
ag.id,
NOW(),
true,
NOW(),
NOW()
FROM student s
JOIN academic_year ay ON TRUE
JOIN academic_group ag ON TRUE;

-------------------------
-- INITIAL PROGRESS
-------------------------

INSERT INTO student_indicator_progress (
id,
academic_year_id,
student_id,
indicator_id,
current_stage_order,
consolidation_score,
normalized_level_internal,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
ay.id,
s.id,
i.id,
1,
0.72,
1.00,
NOW(),
NOW()
FROM student s
JOIN indicator i ON TRUE
JOIN academic_year ay ON TRUE;

COMMIT;