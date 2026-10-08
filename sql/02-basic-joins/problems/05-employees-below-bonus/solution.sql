-- TRY the starter first.
SELECT e.name, b.bonus
FROM employees AS e
LEFT JOIN bonuses AS b
    ON e.id = b.emp_id
WHERE b.bonus < 500 OR b.bonus IS NULL;
