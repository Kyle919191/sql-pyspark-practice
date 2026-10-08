# Window functions

A window aggregate looks at other rows **and still keeps every input row**.

`GROUP BY` collapses. A window does not.

```sql
SELECT
    name,
    department,
    score,
    rank() OVER (PARTITION BY department ORDER BY score DESC) AS rnk
FROM exams;
```

Amy stays a row. She also gets a rank inside her department.

## The template

```sql
function(...) OVER (
    PARTITION BY some_columns    -- optional "group"
    ORDER BY some_columns        -- optional order inside the group
    ROWS BETWEEN ...             -- optional frame; defaults depend on the function
)
```

- `PARTITION BY` is “GROUP BY but do not collapse”.
- `ORDER BY` inside `OVER` is **not** the query’s output order. It is the order the function walks.

## Ranking family

| function | ties | gaps after a tie |
| --- | --- | --- |
| `ROW_NUMBER()` | unique 1,2,3… even if values tie | never |
| `RANK()` | same value → same rank | yes (1,1,3) |
| `DENSE_RANK()` | same value → same rank | no (1,1,2) |

“Top 3 salaries per department, include ties” → `DENSE_RANK() <= 3` (LeetCode 185).

“Most recent N orders per customer” → `ROW_NUMBER()` ordered by date desc, keep `<= N`.

Always write down: do ties share a place, and do you want a gap?

## LAG / LEAD — the previous or next row

```sql
SELECT
    record_date,
    temp,
    lag(temp) OVER (ORDER BY record_date) AS prev_temp
FROM weather;
```

Rising temperature without a self-join. Previous-day delta. “First time the value changed.”

`lag(col, 2)` is two rows back. The first rows in a partition get NULL.

## Running totals

```sql
SELECT
    sale_date,
    amount,
    sum(amount) OVER (ORDER BY sale_date ROWS UNBOUNDED PRECEDING) AS running
FROM sales;
```

Without an explicit frame, `SUM() OVER (ORDER BY …)` in DuckDB/MySQL uses a range-like default that can surprise you on ties. Prefer `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` until you know you want “all peers with the same order key.”

Last person on the bus (1204): running sum of weight, filter `running <= 1000`, take the last row.

## First / last in a group without collapsing

```sql
first_value(status) OVER (PARTITION BY user_id ORDER BY event_at)
```

Or `ROW_NUMBER() = 1` in a CTE, then filter. The CTE form is easier to read.

## Pattern card

| English | Window |
| --- | --- |
| rank inside a group | `RANK` / `DENSE_RANK` / `ROW_NUMBER` |
| previous row’s value | `LAG` |
| next row’s value | `LEAD` |
| cumulative sum | `SUM() OVER (ORDER BY … ROWS …)` |
| latest N per entity | `ROW_NUMBER` desc, filter |

## You're ready when

You can rewrite a self-join “previous day” and a “top N per group” as windows. Then do the three local window problems.
