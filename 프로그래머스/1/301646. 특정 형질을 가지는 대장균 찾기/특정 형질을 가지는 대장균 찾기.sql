select count(GENOTYPE) as COUNT from ECOLI_DATA
where (GENOTYPE & 1 > 0 or GENOTYPE & 4 > 0) and GENOTYPE & 2 = 0;