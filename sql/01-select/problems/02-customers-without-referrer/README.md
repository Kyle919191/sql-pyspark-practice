# Customers not referred by 2

**Pattern:** `!=` does not keep NULL. **LeetCode cousin:** 584.

## Table: `customers`

| column | type |
| --- | --- |
| id | integer |
| name | text |
| referrer_id | integer, NULL if nobody referred them |

One row per customer.

## Task

Return `id` and `name` of customers whose referrer is **not** customer `2`.

A customer with no referrer (`referrer_id` is NULL) should be included. They were not referred by 2.

Order does not matter.

## Example

```text
id  name  referrer_id
1   Amy   NULL
2   Ben   2
3   Cai   1
4   Dee   2
5   Eve   NULL
```

Expected:

```text
id  name
1   Amy
3   Cai
5   Eve
```

## Hint

Write `WHERE referrer_id != 2` alone, run the checker, look at who disappeared, then fix it with `IS NULL`.
