BEGIN;

--------------------------------------------------
-- SUBJECTS
--------------------------------------------------

INSERT INTO subject (id,institution_id,name,created_at,updated_at) VALUES
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Matemáticas',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Lengua',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Ciencias',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Historia',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Geografía',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Arte',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Música',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Educación Física',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Tecnología',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Inglés',NOW(),NOW());

--------------------------------------------------
-- ACADEMIC LEVELS
--------------------------------------------------

INSERT INTO academic_level (id,institution_id,name,order_index,education_stage,created_at,updated_at) VALUES
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 1',1,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 2',2,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 3',3,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 4',4,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 5',5,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 6',6,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 7',7,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 8',8,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 9',9,'primary',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','Nivel 10',10,'primary',NOW(),NOW());

--------------------------------------------------
-- STUDENTS
--------------------------------------------------

INSERT INTO student (id,institution_id,external_code,created_at,updated_at) VALUES
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU001',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU002',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU003',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU004',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU005',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU006',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU007',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU008',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU009',NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','STU010',NOW(),NOW());

--------------------------------------------------
-- INSTITUTIONAL USERS (TEACHERS)
--------------------------------------------------

INSERT INTO institutional_user
(id,institution_id,email,password_hash,full_name,is_active,is_superadmin,created_at,updated_at)
VALUES
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher1@test.com','hash','Ana Gómez',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher2@test.com','hash','Luis Pérez',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher3@test.com','hash','María Díaz',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher4@test.com','hash','Carlos Ruiz',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher5@test.com','hash','Laura Torres',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher6@test.com','hash','Pedro Castro',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher7@test.com','hash','Sara López',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher8@test.com','hash','Miguel Ortiz',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher9@test.com','hash','Julia Navarro',true,false,NOW(),NOW()),
(uuid_generate_v4(),'2914800d-0495-4fbf-afef-4ae5a9f6d754','teacher10@test.com','hash','Ricardo Vega',true,false,NOW(),NOW());

--------------------------------------------------
-- INDICATORS
--------------------------------------------------

INSERT INTO indicator (id,competency_id,description,total_stages,version_number,created_at,updated_at)
SELECT uuid_generate_v4(),id,'Indicador base',4,1,NOW(),NOW()
FROM competency
LIMIT 10;

--------------------------------------------------
-- INDICATOR STAGES
--------------------------------------------------

INSERT INTO indicator_stage
(id,indicator_id,stage_order,description,normalized_level,created_at,updated_at)
SELECT uuid_generate_v4(),i.id,s,'Stage '||s,s,NOW(),NOW()
FROM indicator i
CROSS JOIN generate_series(1,4) s;

--------------------------------------------------
-- STUDENT EVIDENCE
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
JOIN indicator i ON true
JOIN indicator_stage st ON st.indicator_id=i.id
LIMIT 120;

COMMIT;