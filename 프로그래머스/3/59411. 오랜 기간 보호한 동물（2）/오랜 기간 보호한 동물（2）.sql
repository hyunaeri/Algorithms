select
    ai.animal_id,
    ai.name
from animal_ins as ai
join animal_outs as ao
on ai.animal_id = ao.animal_id
order by DATEDIFF(ao.datetime, ai.datetime) + 1 desc
limit 2;