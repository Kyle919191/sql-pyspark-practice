-- TRY the starter first.
SELECT class
FROM enrollments
GROUP BY class
HAVING count(DISTINCT student) >= 3;
