# ORDER BY, DISTINCT, LIMIT

A query result is a table. Unless you sort it, the engine may return rows in any order. LeetCode sometimes cares about order; sometimes it does not. The local checker’s `meta.json` has `"ordered": true` when order matters.

## ORDER BY

```sql
SELECT name, price_cents
FROM products
ORDER BY price_cents;              -- cheapest first (ASC is the default)

SELECT name, price_cents
FROM products
ORDER BY price_cents DESC;         -- most expensive first

SELECT name, price_cents
FROM products
ORDER BY in_stock DESC, name;      -- two keys: stock first, then name
```

You can sort by a column you did not SELECT in some engines. Do not rely on that. Select what you need, sort by those names or by a clear expression.

## DISTINCT

```sql
SELECT DISTINCT viewer_id
FROM views;
```

`DISTINCT` applies to the whole selected row. `SELECT DISTINCT viewer_id, article_id` is unique **pairs**, not unique viewers.

If a person viewed the same article twice, `SELECT DISTINCT viewer_id, article_id` still returns one pair. That is what LeetCode 1148 (Article Views I) is about: unique viewer/article pairs, often with a “did not view their own article” style filter in variants.

## LIMIT

```sql
SELECT name, price_cents
FROM products
ORDER BY price_cents DESC
LIMIT 3;
```

“Top 3” without `ORDER BY` is meaningless. Always sort first.

MySQL/DuckDB: `LIMIT n`. SQL Server: `TOP n`. Same idea.

## LENGTH / CHAR_LENGTH

```sql
WHERE length(content) > 20
```

LeetCode 1683 (Invalid Tweets) is this plus a threshold. DuckDB’s `length` on text counts characters for typical ASCII practice data.

## Pattern: unique entities vs unique events

Ask: does the prompt want every event, or each person/product once?

- Every event → no DISTINCT
- Each person once → `SELECT DISTINCT person_id` or `GROUP BY` (later)

## You're ready when

You can say whether a problem needs DISTINCT, a sort, or just a filter. Then finish the Select local set and the five LeetCode Select problems.
