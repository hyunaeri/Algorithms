with ranking as (
    select
        id,
        percent_rank() over (order by size_of_colony desc) as colony_rank
    from ecoli_data
)

select 
    r.id,
    case 
        when r.colony_rank > 0.75 then 'LOW'
        when r.colony_rank > 0.5 then 'MEDIUM'
        when r.colony_rank > 0.25 then 'HIGH'
        else 'CRITICAL'
    end as colony_name
from ranking as r
order by r.id asc;