# Advanced SELECT and joins

Same clauses, tighter grain. These problems need a plan on paper before SQL.

## CASE as a column (classify rows)

```sql
SELECT
    CASE
        WHEN a + b > c AND a + c > b AND b + c > a THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM triangle;
```

LeetCode 610. Classification is not a filter.

Salary buckets (1907): do **not** GROUP BY a category that might have zero rows. Build the three category names first, then LEFT JOIN counts. Empty categories must still appear with 0.

## Consecutive rows

“Three in a row with the same value” (180):

- Self-join `id`, `id+1`, `id+2` if ids are consecutive, **or**
- `LEAD` / `LAG` (window lesson)

If ids can have gaps, do not add 1 to `id`. Use windows.

## Point-in-time lookup

“Price on date D” (1164): each product has price-change rows. Take the latest change on or before D; default 10 if none.

Pattern:

1. Filter `change_date <= D`
2. Per product, take the row with max(change_date) — `GROUP BY` + join back, or `ROW_NUMBER`
3. LEFT JOIN that onto the product list so missing products get the default

## Running fill / capacity

“Last person who still fits” (1204): order people, running sum of weight, last row where running sum <= 1000.

That is a window `sum() OVER (ORDER BY …)`. You can fake it with a self-join (`sum of all people with turn <= me`) before you know windows. Learn the window version in `08-advanced`.

## Reports-to / manager

The employees table is a hierarchy: `manager_id` points at another `id`. Join the table to itself: worker and manager. Then `GROUP BY` manager and `HAVING count(*) >= 5` (570, 1731).

## Primary among many

An employee can have several departments, one marked primary. If they have only one row, that row is primary even if the flag says N (1789).

```sql
-- keep a row if it is primary OR the employee has exactly one department
```

## Pattern: sketch the grain twice

1. Grain of the **input** tables
2. Grain of the **answer**
3. What intermediate table do you need to get from 1 to 2?

If you cannot name the intermediate grain, do not start typing.

## You're ready when

You can solve triangle / consecutive / manager-count style problems without guessing join types. Then the SQL 50 advanced-select set.
