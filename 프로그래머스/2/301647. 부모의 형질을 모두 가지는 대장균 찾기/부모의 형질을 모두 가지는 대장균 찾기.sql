select 
    c.id as id, 
    c.genotype as genotype, 
    p.genotype as parent_genotype
from ecoli_data c
join ecoli_data p 
    on p.id = c.parent_id
where (c.genotype & p.genotype) = p.genotype
order by c.id asc;