# AND / OR / NULL / IN / LIKE

Easy problems hide one trap: **NULL**. If you remember only one thing from this lesson, remember this:

> Any comparison with NULL is not TRUE. It is UNKNOWN. `WHERE` keeps only TRUE rows.

## NULL is not a value

```text
referrer_id = 2      -- TRUE or FALSE for real numbers
referrer_id = NULL   -- never TRUE. Use IS NULL
referrer_id != 2     -- FALSE when it is 2; UNKNOWN when it is NULL
```

So this query **drops** people with a missing referrer:

```sql
SELECT id, name
FROM customers
WHERE referrer_id != 2;
```

This one keeps them, which is usually what the English meant:

```sql
SELECT id, name
FROM customers
WHERE referrer_id != 2 OR referrer_id IS NULL;
```

The positive form of “is missing”:

```sql
WHERE referrer_id IS NULL
WHERE referrer_id IS NOT NULL
```

Never write `= NULL` or `!= NULL`.

This is the entire reason LeetCode 584 (Find Customer Referee) exists.

## IN and NOT IN

```sql
WHERE name IN ('oats', 'kale', 'chips')
```

is the same as a chain of ORs.

`NOT IN` plus NULL is another trap. If the list you are checking against contains NULL, `NOT IN` can return no rows. Prefer `NOT EXISTS` later, or keep NULL out of the list. For now: if a `NOT IN` looks “empty and cursed”, look for NULL.

## LIKE (pattern on text)

```sql
WHERE name LIKE 'c%'     -- starts with c
WHERE name LIKE '%ale'   -- ends with ale
WHERE name LIKE '%ap%'   -- contains ap
```

`%` is “any sequence”. `_` is “any one character”.

DuckDB `LIKE` is case-sensitive. LeetCode MySQL `LIKE` is often not. If a local problem cares, the prompt will say so.

## BETWEEN

```sql
WHERE price_cents BETWEEN 200 AND 400
```

Both ends are included.

## CASE (preview)

You will need this in later SQL 50 sections. It is if/else as a column:

```sql
SELECT
    name,
    CASE
        WHEN price_cents >= 300 THEN 'expensive'
        WHEN price_cents >= 200 THEN 'mid'
        ELSE 'cheap'
    END AS band
FROM products;
```

`CASE` is not a filter. It does not drop rows. It computes a value.

## Pattern: write the English, then the NULLs

Before coding, write:

1. Which rows do I want in plain English?
2. What does the table use for “missing”?
3. Does my WHERE still work when that column is NULL?

## You're ready when

You can explain why `WHERE col != 2` is not the same as “col is not 2” when `col` can be NULL. Then do local problems `02-customers-without-referrer` and `03-large-markets`.
