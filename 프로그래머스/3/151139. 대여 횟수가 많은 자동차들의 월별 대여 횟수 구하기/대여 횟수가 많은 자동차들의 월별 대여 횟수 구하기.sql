select 
    MONTH(c.start_date) as MONTH, 
    c.car_id as CAR_ID, 
    count(*) as RECORDS
from car_rental_company_rental_history c
where c.start_date >= '2022-08-01'
    and c.start_date < '2022-11-01'
    and c.car_id in (
        select car_id
        from car_rental_company_rental_history
        where start_date >= '2022-08-01'
            and start_date < '2022-11-01'
        group by car_id
        having count(*) >= 5
    )
group by MONTH(c.start_date), c.car_id
order by MONTH asc, c.car_id desc; 
