-- TRY the starter first.
SELECT
    a,
    b,
    c,
    CASE
        WHEN a + b > c AND a + c > b AND b + c > a THEN 'Yes'
        ELSE 'No'
    END AS is_triangle
FROM triangle;
