-- TRY the starter first.
SELECT
    id,
    name,
    CASE
        WHEN manager_id IS NULL THEN 'Root'
        WHEN id IN (SELECT manager_id FROM staff WHERE manager_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS label
FROM staff
ORDER BY id;
