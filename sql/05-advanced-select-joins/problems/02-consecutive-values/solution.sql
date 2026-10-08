-- TRY the starter first.
SELECT DISTINCT a.num
FROM logs AS a
INNER JOIN logs AS b ON a.id = b.id - 1 AND a.num = b.num
INNER JOIN logs AS c ON b.id = c.id - 1 AND b.num = c.num;
