BEGIN;

--------------------------------------------------
-- CONSTANTES
--------------------------------------------------

-- institution existente
-- 2914800d-0495-4fbf-afef-4ae5a9f6d754

-- academic year existente
-- 6f2a7ab7-dc62-44d6-a6bc-11864e903ede


--------------------------------------------------
-- SUBJECTS
--------------------------------------------------

INSERT INTO subject (id,institution_id,name,created_at,updated_at) VALUES
('11111111-0000-0000-0000-000000000001','2914800d-0495-4fbf-afef-4ae5a9f6d754','Matemáticas',NOW(),NOW()),
('11111111-0000-0000-0000-000000000002','2914800d-0495-4fbf-afef-4ae5a9f6d754','Lengua',NOW(),NOW()),
('11111111-0000-0000-0000-000000000003','2914800d-0495-4fbf-afef-4ae5a9f6d754','Ciencias',NOW(),NOW()),
('11111111-0000-0000-0000-000000000004','2914800d-0495-4fbf-afef-4ae5a9f6d754','Historia',NOW(),NOW()),
('11111111-0000-0000-0000-000000000005','2914800d-0495-4fbf-afef-4ae5a9f6d754','Geografía',NOW(),NOW()),
('11111111-0000-0000-0000-000000000006','2914800d-0495-4fbf-afef-4ae5a9f6d754','Inglés',NOW(),NOW());

--------------------------------------------------
-- ACADEMIC LEVEL
--------------------------------------------------

INSERT INTO academic_level
(id,institution_id,name,order_index,education_stage,created_at,updated_at)
VALUES
('22222222-0000-0000-0000-000000000001','2914800d-0495-4fbf-afef-4ae5a9f6d754','Primaria',1,'primary',NOW(),NOW());

--------------------------------------------------
-- GRADES
--------------------------------------------------

INSERT INTO academic_grade
(id,institution_id,academic_level_id,name,order_index,created_at,updated_at)
VALUES
('33333333-0000-0000-0000-000000000001','2914800d-0495-4fbf-afef-4ae5a9f6d754','22222222-0000-0000-0000-000000000001','Grado 3',1,NOW(),NOW()),
('33333333-0000-0000-0000-000000000002','2914800d-0495-4fbf-afef-4ae5a9f6d754','22222222-0000-0000-0000-000000000001','Grado 4',2,NOW(),NOW()),
('33333333-0000-0000-0000-000000000003','2914800d-0495-4fbf-afef-4ae5a9f6d754','22222222-0000-0000-0000-000000000001','Grado 5',3,NOW(),NOW());

--------------------------------------------------
-- GROUPS
--------------------------------------------------

INSERT INTO academic_group
(id,academic_year_id,academic_grade_id,name,created_at,updated_at) VALUES
('44444444-0000-0000-0000-000000000001','6f2a7ab7-dc62-44d6-a6bc-11864e903ede','33333333-0000-0000-0000-000000000001','3A',NOW(),NOW()),
('44444444-0000-0000-0000-000000000002','6f2a7ab7-dc62-44d6-a6bc-11864e903ede','33333333-0000-0000-0000-000000000001','3B',NOW(),NOW()),
('44444444-0000-0000-0000-000000000003','6f2a7ab7-dc62-44d6-a6bc-11864e903ede','33333333-0000-0000-0000-000000000002','4A',NOW(),NOW()),
('44444444-0000-0000-0000-000000000004','6f2a7ab7-dc62-44d6-a6bc-11864e903ede','33333333-0000-0000-0000-000000000002','4B',NOW(),NOW()),
('44444444-0000-0000-0000-000000000005','6f2a7ab7-dc62-44d6-a6bc-11864e903ede','33333333-0000-0000-0000-000000000003','5A',NOW(),NOW()),
('44444444-0000-0000-0000-000000000006','6f2a7ab7-dc62-44d6-a6bc-11864e903ede','33333333-0000-0000-0000-000000000003','5B',NOW(),NOW());

--------------------------------------------------
-- STUDENTS (120)
--------------------------------------------------

INSERT INTO student (id,institution_id,external_code,created_at,updated_at)
SELECT
uuid_generate_v4(),
'2914800d-0495-4fbf-afef-4ae5a9f6d754',
'STU-'||LPAD(i::text,4,'0'),
NOW(),
NOW()
FROM generate_series(1,120) i;

--------------------------------------------------
-- ENROLLMENTS
--------------------------------------------------

INSERT INTO student_enrollment
(id,academic_year_id,student_id,academic_group_id,enrolled_at,is_active,created_at,updated_at)
SELECT
uuid_generate_v4(),
'6f2a7ab7-dc62-44d6-a6bc-11864e903ede',
s.id,
g.id,
NOW(),
TRUE,
NOW(),
NOW()
FROM student s
JOIN academic_group g
ON TRUE
LIMIT 120;

--------------------------------------------------
-- TEACHERS
--------------------------------------------------

INSERT INTO institutional_user
(id,institution_id,email,password_hash,full_name,is_active,is_superadmin,created_at,updated_at)
VALUES
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher_math@test.com','hash','Profesor Matemáticas',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher_lang@test.com','hash','Profesor Lengua',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher_science@test.com','hash','Profesor Ciencias',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher_history@test.com','hash','Profesor Historia',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher_geo@test.com','hash','Profesor Geografía',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher_english@test.com','hash','Profesor Inglés',true,false,NOW(),NOW());

--------------------------------------------------
-- CURRICULUM VERSION
--------------------------------------------------

INSERT INTO curriculum_version
(id,institution_id,academic_year_id,academic_level_id,academic_grade_id,subject_id,version_number,status,created_at,updated_at)
SELECT
uuid_generate_v4(),
'2914800d-0495-4fbf-afef-4ae5a9f6d754',
'6f2a7ab7-dc62-44d6-a6bc-11864e903ede',
'22222222-0000-0000-0000-000000000001',
'33333333-0000-0000-0000-000000000003',
s.id,
1,
'active',
NOW(),
NOW()
FROM subject s;

--------------------------------------------------
-- NUCLEUS
--------------------------------------------------

INSERT INTO nucleus
(id,name,description,created_at,updated_at,curriculum_version_id)
SELECT
uuid_generate_v4(),
'Núcleo '||i,
'Descripción núcleo '||i,
NOW(),
NOW(),
cv.id
FROM curriculum_version cv
CROSS JOIN generate_series(1,3) i;

--------------------------------------------------
-- COMPETENCIES
--------------------------------------------------

INSERT INTO competency
(id,nucleus_id,description,created_at,updated_at)
SELECT
uuid_generate_v4(),
n.id,
'Competencia '||g,
NOW(),
NOW()
FROM nucleus n
CROSS JOIN generate_series(1,4) g;

--------------------------------------------------
-- INDICATORS
--------------------------------------------------

INSERT INTO indicator
(id,competency_id,description,total_stages,version_number,created_at,updated_at)
SELECT
uuid_generate_v4(),
c.id,
'Indicador '||g,
4,
1,
NOW(),
NOW()
FROM competency c
CROSS JOIN generate_series(1,3) g;

--------------------------------------------------
-- STAGES
--------------------------------------------------

INSERT INTO indicator_stage
(id,indicator_id,stage_order,description,normalized_level,created_at,updated_at)
SELECT
uuid_generate_v4(),
i.id,
s,
'Stage '||s,
s,
NOW(),
NOW()
FROM indicator i
CROSS JOIN generate_series(1,4) s;

--------------------------------------------------
-- STUDENT EVIDENCE (~5000)
--------------------------------------------------

INSERT INTO student_evidence
(id,academic_year_id,student_id,indicator_id,indicator_stage_id,raw_score,created_at,updated_at)
SELECT
uuid_generate_v4(),
'6f2a7ab7-dc62-44d6-a6bc-11864e903ede',
s.id,
i.id,
st.id,
(60 + floor(random()*40))::int,
NOW(),
NOW()
FROM student s
JOIN indicator i ON TRUE
JOIN indicator_stage st ON st.indicator_id=i.id
LIMIT 5000;

COMMIT;