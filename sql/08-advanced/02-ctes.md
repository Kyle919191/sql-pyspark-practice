# CTEs, including recursive

You already used CTEs as named subqueries. Two more ideas matter for advanced problems.

## Multiple steps

```sql
WITH daily AS (
    SELECT sale_date, sum(amount) AS revenue
    FROM sales
    GROUP BY sale_date
),
rolling AS (
    SELECT
        sale_date,
        revenue,
        avg(revenue) OVER (
            ORDER BY sale_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS avg_7
    FROM daily
)
SELECT * FROM rolling;
```

Restaurant growth (1321) is this: daily totals, then a 7-day window.

One idea per CTE. Name the grain in the CTE name (`daily`, `first_login`, `ranked`).

## Recursive CTE — walk a chain

A recursive CTE has an **anchor** (the start rows) and a **recursive** part that reads the CTE itself.

Org chart: everyone who reports up to manager 1, any number of levels.

```sql
WITH RECURSIVE tree AS (
    SELECT id, name, manager_id, 1 AS level
    FROM staff
    WHERE id = 1

    UNION ALL

    SELECT s.id, s.name, s.manager_id, tree.level + 1
    FROM staff AS s
    INNER JOIN tree ON s.manager_id = tree.id
)
SELECT * FROM tree;
```

Anchor: the root. Recursive step: people whose manager is already in `tree`. Repeat until nobody new appears.

LeetCode 1270 (all people report to a given manager) is this. 1767 (unexecuted subtasks) is “generate a list of n, then anti-join”.

## Generate a series

```sql
WITH RECURSIVE n AS (
    SELECT 1 AS i
    UNION ALL
    SELECT i + 1 FROM n WHERE i < 10
)
SELECT * FROM n;
```

Useful when a table stores `n_tasks = 5` and you need rows 1..5.

## Safety

Recursive CTEs can loop if the data has a cycle. Practice data will not. In real jobs you add a `level < 20` guard or a path string you check.

## You're ready when

You can split a two-step metric into two CTEs, and you can walk a `manager_id` chain one level at a time. Then the local CTE problem and the tree problem.
