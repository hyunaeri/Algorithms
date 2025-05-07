WITH target AS (
    SELECT
        YEAR(differentiation_date) AS year,
        MAX(size_of_colony) as max_colony
    FROM ecoli_data
    GROUP BY year
)

SELECT 
    year,
    (max_colony - size_of_colony) AS year_dev,
    id
FROM ecoli_data E
JOIN target T ON YEAR(E.differentiation_date) = T.year
ORDER BY year ASC, year_dev ASC;