-- TRY the starter first.
SELECT e.department, e.name, e.score
FROM exams AS e
INNER JOIN (
    SELECT department, max(score) AS top_score
    FROM exams
    GROUP BY department
) AS t
    ON e.department = t.department
   AND e.score = t.top_score;
