-- TRY the starter first.
SELECT
    department,
    name,
    score,
    dense_rank() OVER (PARTITION BY department ORDER BY score DESC) AS score_rank
FROM exams
ORDER BY department, score_rank, name;
