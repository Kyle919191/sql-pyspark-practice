# Sorting and grouping

`GROUP BY` splits the table into piles, then each pile gets its own aggregate.

English: “for each teacher, how many unique subjects?”

```sql
SELECT teacher_id, count(DISTINCT subject_id) AS n
FROM teacher
GROUP BY teacher_id;
```

## The rule

Every non-aggregated column in `SELECT` must appear in `GROUP BY`.

This is illegal in strict engines (and sloppy everywhere):

```sql
SELECT teacher_id, subject_id, count(*)   -- subject_id is neither grouped nor aggregated
FROM teacher
GROUP BY teacher_id;
```

## HAVING vs WHERE

- `WHERE` filters **rows** before grouping
- `HAVING` filters **groups** after aggregation

```sql
SELECT class, count(DISTINCT student) AS n
FROM courses
GROUP BY class
HAVING count(DISTINCT student) >= 5;
```

You cannot put `count(*)` in `WHERE`. The groups do not exist yet.

## Grain

`GROUP BY customer_id` → one row per customer  
`GROUP BY customer_id, date` → one row per customer-day

If the prompt says “for each X”, X is your GROUP BY.

## “Bought all products”

```sql
SELECT customer_id
FROM orders
GROUP BY customer_id
HAVING count(DISTINCT product_id) = (SELECT count(*) FROM products);
```

Compare a group’s distinct count to a scalar subquery. LeetCode 1045.

## “Biggest that appears once”

```sql
SELECT max(num) AS num
FROM (
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING count(*) = 1
) AS singles;
```

Group, keep singles, then max. LeetCode 619.

## Pattern card

| English | SQL |
| --- | --- |
| for each X, count/sum/avg | GROUP BY X |
| only groups that meet a threshold | HAVING |
| unique things inside a group | count(DISTINCT …) |
| this group covers a whole dimension | HAVING count(DISTINCT …) = (SELECT count(*) …) |

## You're ready when

You can point at a prompt and name the GROUP BY columns before you write SELECT. Then do the local problems and the SQL 50 grouping set.
