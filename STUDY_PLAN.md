# Study plan

Pace: **2–3 problems a day**, about 45–90 minutes. Skip a day if you need to; do not skip the lesson that belongs to a problem.

SQL first. PySpark starts once SELECT / WHERE / NULL feel boring. That is on purpose. Spark DataFrames are SQL ideas with method names.

Before any PySpark day: `source tools/env.sh` so Java 17 is on your PATH (PySpark 4 will not start on Java 11).

Official lists:

- SQL 50: https://leetcode.com/studyplan/top-sql-50/
- Advanced SQL 50: https://leetcode.com/studyplan/premium-sql-50/ (Premium). Do the local advanced problems even if you do not have Premium.

---

## Week 1 — SQL foundations + Select

Goal: read a table, keep some rows, keep some columns. Understand NULL.

| Day | Read first | Then do |
| --- | --- | --- |
| 1 | `sql/00-fundamentals/01-what-is-sql.md` and `02-select-from-where.md` | Run the playground. Local problem `01-organic-onsale` |
| 2 | `sql/00-fundamentals/03-logic-null-in-like.md` | Local `02-customers-without-referrer`, `03-large-markets` |
| 3 | `sql/00-fundamentals/04-order-distinct-limit.md` and `sql/01-select/lesson.md` | Local `04-unique-viewers`, `05-too-short-posts` |
| 4 | Re-read any lesson that felt shaky | LeetCode SQL 50 #1–5 (see `sql/01-select/leetcode.md`) |
| 5 | Buffer / review | Rewrite yesterday’s queries from memory. Update PROGRESS.md |

## Week 2 — Joins

Goal: combine two tables. Inner vs left. Self-join.

| Day | Read first | Then do |
| --- | --- | --- |
| 6 | `sql/02-basic-joins/lesson.md` through “INNER JOIN” | Local `01-orders-with-products` |
| 7 | Same lesson, “LEFT JOIN” and “anti-join” | Local `02-employee-unique-id`, `03-visits-without-purchases` |
| 8 | Same lesson, “self-join” | Local `04-warmer-than-yesterday`, `05-employees-below-bonus` |
| 9–10 | — | LeetCode SQL 50 Basic Joins (9 problems) |

## Week 3 — Aggregates + GROUP BY

| Day | Read first | Then do |
| --- | --- | --- |
| 11 | `sql/03-aggregates/lesson.md` | Local aggregate problems, then SQL 50 aggregate set |
| 12–13 | `sql/04-sorting-grouping/lesson.md` | Local grouping problems, then SQL 50 sorting/grouping set |

## Week 4 — Harder SELECT / joins + subqueries

| Day | Read first | Then do |
| --- | --- | --- |
| 14 | `sql/05-advanced-select-joins/lesson.md` | Local + SQL 50 “Advanced Select and Joins” |
| 15–16 | `sql/06-subqueries/lesson.md` | Local + SQL 50 Subqueries |
| 17 | `sql/07-strings/lesson.md` | Local + SQL 50 string / regex set |

## Week 5 — Start PySpark, remirror Select + Joins

| Day | Read first | Then do |
| --- | --- | --- |
| 18 | `pyspark/00-fundamentals/` (all three lessons) | `pyspark/00-fundamentals/playground/hello_spark.py` |
| 19 | `pyspark/01-select-filter/lesson.md` | All 5 select problems in PySpark |
| 20 | `pyspark/02-joins/lesson.md` | All 5 join problems in PySpark |

## Week 6 — PySpark aggregates + SQL windows

| Day | Read first | Then do |
| --- | --- | --- |
| 21 | `pyspark/03-aggregates/lesson.md` | PySpark aggregate problems |
| 22 | `sql/08-advanced/01-window-functions.md` | Local window problems |
| 23 | `pyspark/04-windows/lesson.md` | Same window problems in PySpark |

## Weeks 7–8 — Advanced SQL patterns + Spark-only ideas

| Day | Read first | Then do |
| --- | --- | --- |
| 24 | `sql/08-advanced/02-ctes.md` | Local CTE problems |
| 25 | `sql/08-advanced/03-gaps-islands.md` | Local gaps/islands problem |
| 26 | `sql/08-advanced/04-pivot.md` | Local pivot problem |
| 27 | `sql/08-advanced/05-trees-hierarchy.md` | Local tree problem |
| 28+ | `pyspark/05-spark-specific/lesson.md` and `sql/08-advanced/leetcode.md` | Remaining Advanced SQL 50 problems you can access; rewrite hard SQL in PySpark |

---

## What “done” looks like for a problem

- Checker is green (local problems).
- You can explain the grain of the answer (one row per what?).
- You can name the pattern in one sentence.
- For LeetCode: accepted submission, solution saved under `sql/solutions/leetcode/` or `pyspark/solutions/`.
