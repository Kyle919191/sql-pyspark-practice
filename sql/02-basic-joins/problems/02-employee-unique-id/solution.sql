-- TRY the starter first.
SELECT u.unique_id, e.name
FROM employees AS e
LEFT JOIN employee_ids AS u
    ON e.id = u.id;
