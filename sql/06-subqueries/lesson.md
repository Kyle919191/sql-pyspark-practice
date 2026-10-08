# Subqueries and CTEs

A subquery is a query used as a value, a list, or a table.

## Scalar subquery — one value

```sql
SELECT max(score) AS second_highest
FROM exams
WHERE score < (SELECT max(score) FROM exams);
```

If nothing matches, the result is NULL. That is what “second highest salary” wants when there is no second.

## IN / EXISTS — a list or a yes/no

```sql
SELECT name
FROM employees
WHERE manager_id NOT IN (SELECT id FROM employees);   -- dangerous if NULL ids

SELECT name
FROM employees AS e
WHERE e.manager_id IS NOT NULL
  AND NOT EXISTS (
      SELECT 1 FROM employees AS m WHERE m.id = e.manager_id
  );
```

Prefer `EXISTS` / `NOT EXISTS` when the list can contain NULL. LeetCode 1978.

## Derived table — a query in FROM

```sql
SELECT department, max(score) AS top
FROM (
    SELECT department, score
    FROM exams
) AS t
GROUP BY department;
```

Always alias the subquery (`AS t`).

## Correlated subquery — depends on the outer row

```sql
SELECT e.name
FROM exams AS e
WHERE e.score >= (
    SELECT max(score) FROM exams AS x WHERE x.department = e.department
);
```

Runs once per outer row (conceptually). Fine on small data. On large data, a join + window is usually clearer.

“Top 3 per department” (185) is this idea, done cleanly with `DENSE_RANK()` in the advanced module.

## CTE — a named subquery

```sql
WITH first_orders AS (
    SELECT customer_id, min(order_date) AS first_date
    FROM delivery
    GROUP BY customer_id
)
SELECT
    avg(CASE WHEN d.order_date = d.customer_pref_date THEN 1.0 ELSE 0 END) AS immediate_rate
FROM delivery AS d
INNER JOIN first_orders AS f
    ON d.customer_id = f.customer_id
   AND d.order_date = f.first_date;
```

CTEs are the same as derived tables. Use them when you would nest more than one level. They are the way adults write multi-step SQL.

You can stack CTEs: `WITH a AS (...), b AS (SELECT ... FROM a)`.

## Pattern: one idea per CTE

1. Build the grain you need (`first_orders`)
2. Join it back to facts
3. Aggregate

If a query has four jobs, it should have named steps, not one 80-line SELECT.

## You're ready when

You can replace a messy nest with one or two CTEs and explain whether a subquery is scalar, IN/EXISTS, or a table. Then the SQL 50 subquery set.
