with Q as (
    select 
        id,
        parent_id,
        size_of_colony,
        differentiation_date,
        genotype,
        case
            when MONTH(differentiation_date) in (1, 2, 3) then "1Q"
            when MONTH(differentiation_date) in (4, 5, 6) then "2Q"
            when MONTH(differentiation_date) in (7, 8, 9) then "3Q"
            when MONTH(differentiation_date) in (10, 11, 12) then "4Q"
        end as quarter  
    from ecoli_data
)

select quarter, count(*) as ecoli_count
from Q
group by quarter
order by quarter asc;
