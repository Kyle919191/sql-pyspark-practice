# SQL track

Start in `00-fundamentals/` even if you have seen a SELECT before. The later LeetCode problems fail on NULL, grain, and join type — not on syntax.

## Order

1. `00-fundamentals/` — what a table is, SELECT / WHERE, NULL, ORDER BY
2. `01-select/` through `07-strings/` — SQL 50, one topic per folder
3. `08-advanced/` — window functions and the Advanced SQL 50 patterns

## Local vs LeetCode

Each topic folder has:

- `lesson.md` — read this first
- `problems/` — original problems you can check offline
- `leetcode.md` — official problem numbers to submit on LeetCode

Local SQL runs in **DuckDB**. LeetCode usually offers MySQL. The ideas are the same. Dialect traps are called out in the lessons (dates, string concat, regex).

## Saving LeetCode solutions

Put accepted queries here so the daily push has something concrete:

```text
sql/solutions/leetcode/1757_recyclable_and_low_fat_products.sql
```
