select
    round(avg(fi2.convert_length), 2) as average_length
from fish_info fi
join (
    select
        id,
        case
            when length is null then 10
            else length
        end as convert_length
    from fish_info
) as fi2
on fi.id = fi2.id;


