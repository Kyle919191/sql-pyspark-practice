# Strings, cleanup, and a few DML clauses

## Fix casing

```sql
-- DuckDB
SELECT upper(substr(name, 1, 1)) || lower(substr(name, 2)) AS name
FROM users;
```

MySQL often uses `LEFT`/`RIGHT`/`CONCAT`. LeetCode 1667 is “capitalize first letter, lowercase the rest.”

## Search inside text

```sql
WHERE conditions LIKE '%DIAB1%'
```

Be careful with false friends: `DIAB10` also contains `DIAB1`. The LeetCode 1527 trick is to match a condition as a **word** (`DIAB1` at start or after a space).

## Regex

LeetCode MySQL: `REGEXP '^pattern$'`.

DuckDB: `regexp_matches(col, 'pattern')`.

Email validation (1517) is a regex problem. Do it on LeetCode. Do not memorize the pattern; learn to read `^`, `$`, `[a-z]`, `+`, `{2,4}`.

## Group-concat

```sql
-- DuckDB
SELECT sell_date, string_agg(DISTINCT product, ',' ORDER BY product) AS products
FROM sales
GROUP BY sell_date;
```

MySQL: `GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')`.

LeetCode 1484.

## Second highest (again)

```sql
SELECT (
    SELECT DISTINCT score
    FROM exams
    ORDER BY score DESC
    LIMIT 1 OFFSET 1
) AS second_highest;
```

`OFFSET 1` skips the first. If it is missing, the scalar subquery is NULL. LeetCode 176.

## DELETE (know it, rarely write it here)

```sql
DELETE FROM person
WHERE id NOT IN (
    SELECT min(id) FROM person GROUP BY email
);
```

LeetCode 196. Some engines forbid deleting from a table you are selecting. Use a CTE or join. For this repo, prefer SELECT-only rewrites that return the rows you would keep.

## Dialect cheat sheet

| Idea | DuckDB (local) | MySQL (LeetCode) |
| --- | --- | --- |
| concat | `a \|\| b` | `CONCAT(a, b)` |
| group concat | `string_agg` | `GROUP_CONCAT` |
| regex | `regexp_matches` | `REGEXP` |
| substr | `substr` | `SUBSTRING` / `LEFT` |
| limit offset | `LIMIT n OFFSET k` | same |

## You're ready when

You can capitalize a name, filter a token in a csv-like string, and write second-highest as a scalar subquery. Then the SQL 50 string set.
