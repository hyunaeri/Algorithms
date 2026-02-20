select a.animal_id, a.name
from animal_ins a
where a.intake_condition = 'Sick'
order by a.animal_id asc;