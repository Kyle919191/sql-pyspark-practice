-- TRY the starter first.
SELECT (
    SELECT DISTINCT score
    FROM exams
    ORDER BY score DESC
    LIMIT 1 OFFSET 1
) AS second_highest;
