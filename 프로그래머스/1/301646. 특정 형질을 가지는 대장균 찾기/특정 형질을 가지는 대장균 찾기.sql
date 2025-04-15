select count(*) as count 
from ECOLI_DATA
where GENOTYPE & 2 = 0 
    and (GENOTYPE & 1 > 0 or GENOTYPE & 4 > 0);