# Trees and hierarchy

Many employee / folder / task tables are trees: each row has a parent id.

## Label the node type

```sql
SELECT
    id,
    CASE
        WHEN manager_id IS NULL THEN 'Root'
        WHEN id IN (SELECT manager_id FROM staff WHERE manager_id IS NOT NULL) THEN 'Inner'
        ELSE 'Leaf'
    END AS label
FROM staff;
```

LeetCode 608 (Tree Node): Root / Inner / Leaf.

## Walk down: recursive CTE

Start at a manager, repeatedly attach people who report to someone already found. See `02-ctes.md`. LeetCode 1270.

## Walk up

Same idea, but the recursive step joins `s.id = tree.manager_id` (move to the parent). Stop at NULL.

## Reporting depth

Keep a `level` column in the recursive CTE. Filter `level <= 3` if the problem only wants three layers (common in Advanced SQL 50).

## Graph-ish variants

- Page recommendations (1264): friends of friends who are not already friends, minus self
- Calls between two persons (1699): treat (a,b) and (b,a) as the same pair (`LEAST`/`GREATEST` or UNION)

Those are graphs, not trees, but you still start with a self-join and a clear grain (one row per pair).

## You're ready when

You can label Root/Inner/Leaf and write a recursive walk from a given manager. Then the local org-chart problem.
