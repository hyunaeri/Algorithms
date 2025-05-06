-- ANIMAL_INS 테이블 : animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake
-- ANIMAL_OUTS 테이블 : animal_id, animal_type, datetime, name, sex_upon_outcome
SELECT i.name, i.datetime
FROM animal_ins AS i
LEFT OUTER JOIN animal_outs AS o ON i.animal_id = o.animal_id
WHERE o.animal_id IS NULL
ORDER BY i.datetime ASC
LIMIT 3;