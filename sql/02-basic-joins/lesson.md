# Joins

A join builds a new table by pairing rows from two tables that “match” on a key.

If SELECT/WHERE is “filter one list”, a join is “look something up in another list”.

## Two tables, one question

`orders` (one row per order):

| order_id | product_id | qty |
| ---: | ---: | ---: |
| 10 | 1 | 2 |
| 11 | 3 | 1 |

`products` (one row per product):

| product_id | name |
| ---: | --- |
| 1 | oats |
| 2 | kale |
| 3 | chips |

Question: “order id and product name”. The name does not live on `orders`. You join.

## INNER JOIN — only matches

```sql
SELECT o.order_id, p.name
FROM orders AS o
INNER JOIN products AS p
    ON o.product_id = p.product_id;
```

Read it as:

1. Take every order.
2. Find the product whose `product_id` equals the order’s `product_id`.
3. If there is no such product, **drop the order**.

Result: order 10/oats, order 11/chips. Kale never appears (no order). A dangling order with a missing product would also disappear.

`INNER JOIN` is the default meaning of `JOIN`.

## LEFT JOIN — keep the left table

```sql
SELECT e.id, e.name, u.unique_id
FROM employees AS e
LEFT JOIN employee_ids AS u
    ON e.id = u.id;
```

Take every employee. If they have a unique id, attach it. If not, keep the employee and put NULL in `unique_id`.

Left = the table after `FROM`. Right = the table you join.

**LEFT JOIN is how you find “who has no match”:**

```sql
SELECT v.visit_id
FROM visits AS v
LEFT JOIN transactions AS t
    ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL;
```

That pattern has a name: **anti-join**. “Rows on the left with no partner on the right.” LeetCode 1581 is this.

`RIGHT JOIN` is LEFT JOIN with the tables swapped. You can always rewrite it as LEFT. `FULL JOIN` keeps unmatched rows from both sides. DuckDB supports it; MySQL does not (use UNION of two LEFT JOINs).

## The ON clause is the match rule

```sql
ON a.id = b.a_id
ON a.id = b.a_id AND b.status = 'ok'   -- extra conditions allowed
```

Putting a right-table filter in `WHERE` after a LEFT JOIN can accidentally turn it into an INNER JOIN, because `WHERE right.col = 'ok'` drops rows where `right.col` is NULL.

Rule:

- Conditions that define the match → `ON`
- Conditions that filter the **final** result, especially on the left table → `WHERE`
- Filters on the right table that should not kill unmatched left rows → `ON`

## Self-join — the same table twice

To compare a row to another row in the same table, join the table to itself under two aliases.

“Days that were warmer than the previous calendar day”:

```sql
SELECT w.id
FROM weather AS w
INNER JOIN weather AS prev
    ON w.record_date = prev.record_date + INTERVAL 1 DAY
WHERE w.temp > prev.temp;
```

You are pairing today with yesterday. LeetCode 197 is this.

## CROSS JOIN — every pair

```sql
SELECT s.student_id, e.exam_id
FROM students AS s
CROSS JOIN exams AS e;
```

One row per student-exam pair, whether or not they sat it. Then LEFT JOIN the actual attempts. LeetCode 1280 (Students and Examinations) is this shape.

Use CROSS JOIN on purpose. If you forget `ON`, some engines give you a cross join and a huge wrong table.

## Grain after a join

Joins multiply rows.

- 1 customer with 3 orders → 3 rows after joining orders
- If you then join order_lines (2 lines each) → 6 rows

If you expected one row per customer and you join orders without aggregating, your counts will explode. This is a **fan-out**. Always ask: one row per what, after the join?

## Pattern card

| English | SQL |
| --- | --- |
| Lookup a name / attribute | INNER JOIN on the id |
| Keep everyone, fill extra info if it exists | LEFT JOIN |
| Who never did X | LEFT JOIN … WHERE right.key IS NULL |
| Compare a row to another row | Self-join |
| All combinations, then attach facts | CROSS JOIN + LEFT JOIN |

## Common mistakes

- Joining on the wrong key (`name` instead of `id`) → duplicated or dropped rows
- Forgetting table aliases when both tables have `id`
- Filtering the right table in WHERE after LEFT JOIN
- Not checking grain (row count jumped and you did not notice)

## You're ready when

You can say, for a prompt, whether you need inner, left, anti, or self, and what one output row represents. Then do the five local problems before the SQL 50 join set.
