BEGIN;

---------------------------------------------------------
-- CONSTANTS
---------------------------------------------------------

-- Student
-- 9000 range reservado para seeds

---------------------------------------------------------
-- SUBJECT
---------------------------------------------------------

INSERT INTO subject (
    id,
    institution_id,
    name,
    created_at,
    updated_at
)
VALUES (
    '90000000-0000-0000-0000-000000000001',
    '2914800d-0495-4fbf-afef-4ae5a9f6d754',
    'Mathematics Test',
    now(),
    now()
)
ON CONFLICT (id) DO NOTHING;

---------------------------------------------------------
-- CURRICULUM VERSION (usar uno existente)
---------------------------------------------------------

-- usamos el existente porque tu tabla lo exige

---------------------------------------------------------
-- NUCLEUS (2)
---------------------------------------------------------

INSERT INTO nucleus (
    id,
    name,
    description,
    curriculum_version_id,
    created_at,
    updated_at
)
VALUES
(
'90000000-0000-0000-0000-000000000101',
'Nucleus A',
'Test nucleus',
(SELECT id FROM curriculum_version LIMIT 1),
now(),
now()
),
(
'90000000-0000-0000-0000-000000000102',
'Nucleus B',
'Test nucleus',
(SELECT id FROM curriculum_version LIMIT 1),
now(),
now()
)
ON CONFLICT (id) DO NOTHING;

---------------------------------------------------------
-- COMPETENCIES (2 PER NUCLEUS)
---------------------------------------------------------

INSERT INTO competency (
    id,
    nucleus_id,
    description,
    created_at,
    updated_at
)
VALUES
('90000000-0000-0000-0000-000000000201','90000000-0000-0000-0000-000000000101','Competency A1',now(),now()),
('90000000-0000-0000-0000-000000000202','90000000-0000-0000-0000-000000000101','Competency A2',now(),now()),
('90000000-0000-0000-0000-000000000203','90000000-0000-0000-0000-000000000102','Competency B1',now(),now()),
('90000000-0000-0000-0000-000000000204','90000000-0000-0000-0000-000000000102','Competency B2',now(),now())
ON CONFLICT (id) DO NOTHING;

---------------------------------------------------------
-- INDICATORS (3 PER COMPETENCY)
---------------------------------------------------------

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
('90000000-0000-0000-0000-000000000301','90000000-0000-0000-0000-000000000201','Indicator 1',4,1,now(),now()),
('90000000-0000-0000-0000-000000000302','90000000-0000-0000-0000-000000000201','Indicator 2',4,1,now(),now()),
('90000000-0000-0000-0000-000000000303','90000000-0000-0000-0000-000000000201','Indicator 3',4,1,now(),now()),

('90000000-0000-0000-0000-000000000304','90000000-0000-0000-0000-000000000202','Indicator 4',4,1,now(),now()),
('90000000-0000-0000-0000-000000000305','90000000-0000-0000-0000-000000000202','Indicator 5',4,1,now(),now()),
('90000000-0000-0000-0000-000000000306','90000000-0000-0000-0000-000000000202','Indicator 6',4,1,now(),now()),

('90000000-0000-0000-0000-000000000307','90000000-0000-0000-0000-000000000203','Indicator 7',4,1,now(),now()),
('90000000-0000-0000-0000-000000000308','90000000-0000-0000-0000-000000000203','Indicator 8',4,1,now(),now()),
('90000000-0000-0000-0000-000000000309','90000000-0000-0000-0000-000000000203','Indicator 9',4,1,now(),now()),

('90000000-0000-0000-0000-000000000310','90000000-0000-0000-0000-000000000204','Indicator 10',4,1,now(),now()),
('90000000-0000-0000-0000-000000000311','90000000-0000-0000-0000-000000000204','Indicator 11',4,1,now(),now()),
('90000000-0000-0000-0000-000000000312','90000000-0000-0000-0000-000000000204','Indicator 12',4,1,now(),now())
ON CONFLICT (id) DO NOTHING;

---------------------------------------------------------
-- INDICATOR STAGES (4 POR INDICADOR)
---------------------------------------------------------

INSERT INTO indicator_stage (
    id,
    indicator_id,
    stage_order,
    description,
    normalized_level,
    created_at,
    updated_at
)
SELECT
uuid_generate_v4(),
indicator_id,
stage,
'Stage ' || stage,
stage,
now(),
now()
FROM (
    SELECT id AS indicator_id
    FROM indicator
    WHERE id::text LIKE '90000000%'
) i
CROSS JOIN generate_series(1,4) stage
ON CONFLICT (indicator_id, stage_order) DO NOTHING;

---------------------------------------------------------
-- STUDENT
---------------------------------------------------------

INSERT INTO student (
    id,
    institution_id,
    external_code,
    created_at,
    updated_at
)
VALUES (
    '90000000-0000-0000-0000-000000000401',
    '2914800d-0495-4fbf-afef-4ae5a9f6d754',
    'TEST_STUDENT',
    now(),
    now()
)
ON CONFLICT (id) DO NOTHING;

---------------------------------------------------------
-- STUDENT PROGRESS
---------------------------------------------------------

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
'6f2a7ab7-dc62-44d6-a6bc-11864e903ede',
'90000000-0000-0000-0000-000000000401',
id,
1,
0.72,
1.2,
now(),
now()
FROM indicator
WHERE id::text LIKE '90000000%'
ON CONFLICT DO NOTHING;

COMMIT;