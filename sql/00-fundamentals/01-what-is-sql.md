# What SQL is

SQL (Structured Query Language) is how you ask a database for a subset of a table, or a new table built from old ones.

You do not loop over rows. You describe the result you want. The engine figures out how to get it.

That one idea is the whole language:

> Start from table(s) → keep some rows → keep or compute some columns → maybe collapse rows into groups → return a table.

## A table

A table is a grid.

| id | name | price_cents | in_stock |
| ---: | --- | ---: | --- |
| 1 | oats | 399 | true |
| 2 | kale | 249 | true |
| 3 | chips | 199 | false |

- A **column** has a name and a type (`id` is an integer, `name` is text).
- A **row** is one entity (one product).
- A **cell** is one value. It can also be **NULL**, which means “unknown / missing”. NULL is not `0` and not `''`.

The **grain** of a table is “one row per what?”. Products above are one row per product. An orders table is often one row per order, or one row per order-line. Wrong grain is the #1 reason a query looks right and is still wrong.

## A query returns a table

```sql
SELECT name, price_cents
FROM products
WHERE in_stock = true;
```

Read it in this order, even though `SELECT` is written first:

1. `FROM products` — start with this table
2. `WHERE in_stock = true` — keep some rows
3. `SELECT name, price_cents` — keep some columns

The result is another table. You can query that result again. That is why SQL composes.

## What you will not do yet

No joins, no `GROUP BY`, no windows. If a problem needs two tables, you are in a later module.

## Try it

```bash
python tools/check.py sql/00-fundamentals/playground
```

The playground `starter.sql` is a blank query against a tiny `products` table. Make it return every column of every row (`SELECT * FROM products;`), then change it as you read lesson 02.

## You're ready when

You can look at a grid of data and say: grain, columns, which values might be NULL.
