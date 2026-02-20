select a.animal_id, a.name
from animal_ins a
where a.intake_condition != 'Aged'
order by a.animal_id;