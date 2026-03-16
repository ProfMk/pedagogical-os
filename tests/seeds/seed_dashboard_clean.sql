BEGIN;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

------------------------------------------------------------
-- INSTITUTION
------------------------------------------------------------

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
'11111111-1111-1111-1111-111111111111',
'{"name":"Test School"}',
'{"type":"private"}',
'{"model":"standard"}',
'standard',
NOW(),
NOW()
);

------------------------------------------------------------
-- ACADEMIC YEAR
------------------------------------------------------------

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
VALUES (
'22222222-2222-2222-2222-222222222222',
'11111111-1111-1111-1111-111111111111',
'2026',
'2026-01-01',
'2026-12-31',
'active',
NOW(),
NOW()
);

------------------------------------------------------------
-- ACADEMIC LEVEL
------------------------------------------------------------

INSERT INTO academic_level (
id,
institution_id,
name,
order_index,
created_at,
updated_at
)
VALUES (
'33333333-3333-3333-3333-333333333333',
'11111111-1111-1111-1111-111111111111',
'Primary',
1,
NOW(),
NOW()
);

------------------------------------------------------------
-- ACADEMIC GRADE
------------------------------------------------------------

INSERT INTO academic_grade (
id,
institution_id,
academic_level_id,
name,
order_index,
created_at,
updated_at
)
VALUES (
'44444444-4444-4444-4444-444444444444',
'11111111-1111-1111-1111-111111111111',
'33333333-3333-3333-3333-333333333333',
'5',
5,
NOW(),
NOW()
);

------------------------------------------------------------
-- ACADEMIC GROUP
------------------------------------------------------------

INSERT INTO academic_group (
id,
academic_grade_id,
academic_year_id,
name,
created_at,
updated_at
)
VALUES (
'55555555-5555-5555-5555-555555555555',
'44444444-4444-4444-4444-444444444444',
'22222222-2222-2222-2222-222222222222',
'5A',
NOW(),
NOW()
);

------------------------------------------------------------
-- SUBJECT
------------------------------------------------------------

INSERT INTO subject (
id,
institution_id,
name,
created_at,
updated_at
)
VALUES (
'66666666-6666-6666-6666-666666666666',
'11111111-1111-1111-1111-111111111111',
'Mathematics',
NOW(),
NOW()
);

------------------------------------------------------------
-- CURRICULUM VERSION
------------------------------------------------------------

INSERT INTO curriculum_version (
id,
institution_id,
academic_year_id,
academic_level_id,
academic_grade_id,
subject_id,
version_number,
status,
parent_version_id,
created_at,
updated_at
)
VALUES (
'77777777-7777-7777-7777-777777777777',
'11111111-1111-1111-1111-111111111111',
'22222222-2222-2222-2222-222222222222',
'33333333-3333-3333-3333-333333333333',
'44444444-4444-4444-4444-444444444444',
'66666666-6666-6666-6666-666666666666',
1,
'active',
NULL,
NOW(),
NOW()
);

------------------------------------------------------------
-- NUCLEUS
------------------------------------------------------------

INSERT INTO nucleus (
id,
name,
description,
created_at,
updated_at,
curriculum_version_id
)
VALUES (
'88888888-8888-8888-8888-888888888888',
'Numbers',
'Numerical thinking',
NOW(),
NOW(),
'77777777-7777-7777-7777-777777777777'
);

------------------------------------------------------------
-- COMPETENCY
------------------------------------------------------------

INSERT INTO competency (
id,
nucleus_id,
description,
created_at,
updated_at
)
VALUES
(
'99999999-0000-0000-0000-000000000001',
'88888888-8888-8888-8888-888888888888',
'Understand number systems',
NOW(),
NOW()
);

------------------------------------------------------------
-- INDICATOR
------------------------------------------------------------

INSERT INTO indicator (
id,
competency_id,
description,
total_stages,
version_number,
created_at,
updated_at
)
VALUES
(
'aaaa0000-0000-0000-0000-000000000001',
'99999999-0000-0000-0000-000000000001',
'Identify place value',
4,
1,
NOW(),
NOW()
);

------------------------------------------------------------
-- INDICATOR STAGES
------------------------------------------------------------

INSERT INTO indicator_stage (
id,
indicator_id,
stage_order,
description,
normalized_level,
created_at,
updated_at
)
VALUES
(uuid_generate_v4(),'aaaa0000-0000-0000-0000-000000000001',1,'Stage 1',1,NOW(),NOW()),
(uuid_generate_v4(),'aaaa0000-0000-0000-0000-000000000001',2,'Stage 2',2,NOW(),NOW()),
(uuid_generate_v4(),'aaaa0000-0000-0000-0000-000000000001',3,'Stage 3',3,NOW(),NOW()),
(uuid_generate_v4(),'aaaa0000-0000-0000-0000-000000000001',4,'Stage 4',4,NOW(),NOW());

------------------------------------------------------------
-- STUDENTS
------------------------------------------------------------

INSERT INTO student (
id,
institution_id,
external_code,
created_at,
updated_at
)
VALUES
(uuid_generate_v4(),'11111111-1111-1111-1111-111111111111','STUDENT_LUIS',NOW(),NOW()),
(uuid_generate_v4(),'11111111-1111-1111-1111-111111111111','STUDENT_MARIA',NOW(),NOW()),
(uuid_generate_v4(),'11111111-1111-1111-1111-111111111111','STUDENT_ANA',NOW(),NOW()),
(uuid_generate_v4(),'11111111-1111-1111-1111-111111111111','STUDENT_DIEGO',NOW(),NOW());

------------------------------------------------------------
-- STUDENTS ENROLLMENT
------------------------------------------------------------

INSERT INTO student_enrollment (
id,
academic_year_id,
student_id,
academic_group_id,
enrolled_at,
is_active,
withdrawn_at,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
'22222222-2222-2222-2222-222222222222',
s.id,
'55555555-5555-5555-5555-555555555555',
NOW(),
TRUE,
NULL,
NOW(),
NOW()
FROM student s;

------------------------------------------------------------
-- SUBJECT GROUP
------------------------------------------------------------

INSERT INTO subject_group (
id,
academic_year_id,
subject_id,
academic_group_id,
name,
created_at,
updated_at
)
VALUES (
'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
'22222222-2222-2222-2222-222222222222',
'66666666-6666-6666-6666-666666666666',
'55555555-5555-5555-5555-555555555555',
'Mathematics 5A',
NOW(),
NOW()
);

------------------------------------------------------------
-- TEACHER USER
------------------------------------------------------------

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
VALUES (
'cccccccc-cccc-cccc-cccc-cccccccccccc',
'11111111-1111-1111-1111-111111111111',
'teacher@test.com',
'dev',
'Teacher Demo',
TRUE,
FALSE,
NOW(),
NOW()
);

------------------------------------------------------------
-- TEACHER ROLE
------------------------------------------------------------

INSERT INTO institutional_user_role (
id,
academic_year_id,
institutional_user_id,
role_id,
is_active,
assigned_at,
revoked_at,
created_at,
updated_at
)
VALUES (
uuid_generate_v4(),
'22222222-2222-2222-2222-222222222222',
'cccccccc-cccc-cccc-cccc-cccccccccccc',
(SELECT id FROM role LIMIT 1),
TRUE,
NOW(),
NULL,
NOW(),
NOW()
);

------------------------------------------------------------
-- TEACHER SUBJECT ASSIGNMENT
------------------------------------------------------------

INSERT INTO teacher_subject_assignment (
id,
institutional_user_id,
subject_group_id,
academic_year_id,
created_at,
updated_at
)
VALUES (
uuid_generate_v4(),
'cccccccc-cccc-cccc-cccc-cccccccccccc',
'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
'22222222-2222-2222-2222-222222222222',
NOW(),
NOW()
);

------------------------------------------------------------
-- STUDENT INDICATOR PROGRESS
------------------------------------------------------------

INSERT INTO student_indicator_progress (
id,
student_id,
indicator_id,
current_stage_order,
consolidation_score,
created_at,
updated_at
)
SELECT
uuid_generate_v4(),
s.id,
'aaaa0000-0000-0000-0000-000000000001',
1,
0.72,
NOW(),
NOW()
FROM student s;

COMMIT;