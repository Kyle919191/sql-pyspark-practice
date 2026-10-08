# Aggregates

An aggregate turns many rows into one number: count, sum, average, min, max.

```sql
SELECT
    count(*) AS n_rows,
    count(bonus) AS n_bonuses,   -- NULLs not counted
    avg(price_cents) AS avg_price,
    sum(qty) AS units,
    min(temp) AS coldest,
    max(temp) AS hottest
FROM orders;
```

No `GROUP BY` yet. The whole table is one group. One output row.

## count(*) vs count(col)

- `count(*)` — number of rows
- `count(col)` — number of rows where `col` is not NULL
- `count(DISTINCT col)` — number of distinct non-NULL values

Rates are usually `sum(CASE WHEN ... THEN 1 ELSE 0 END) / count(*)` or `avg(CASE WHEN ... THEN 1.0 ELSE 0 END)`.

## CASE inside an aggregate

“Share of immediate orders”:

```sql
SELECT
    avg(CASE WHEN order_date = customer_pref_date THEN 1.0 ELSE 0 END) AS immediate_rate
FROM delivery;
```

This is the pattern behind confirmation rate and immediate-delivery problems.

## Dates and buckets (preview)

```sql
SELECT date_trunc('month', txn_date) AS month, sum(amount) AS revenue
FROM txns
GROUP BY 1;          -- GROUP BY is the next lesson
```

DuckDB: `date_trunc`, `strftime`. MySQL: `DATE_FORMAT`. Same idea, different spelling. For LeetCode, use the dialect picker’s functions.

## Rounding

```sql
round(avg(price), 2)
```

LeetCode is picky about 2 decimal places. Round in the query, do not trust display.

## Pattern: metric = numerator / denominator

Write both parts in English first.

- Average selling price → sum(price * units) / sum(units), not avg(price)
- Contest attendance → users in contest / all users
- Confirmation rate → confirmed / (confirmed + timeout), leftovers are 0 not NULL

If the denominator can be 0, use `NULLIF(denom, 0)` or a CASE.

## Common mistakes

- `avg(price)` when the prompt wants a weighted average
- Forgetting to treat NULL as 0 in a rate
- Counting the wrong table after a join (fan-out)

## You're ready when

You can write a single-row metric query and a rate with CASE. Then do the local problems and the SQL 50 aggregate set. Several of those also use `GROUP BY` — read the next lesson as soon as a problem says “for each”.
