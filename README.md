# SQL + PySpark Practice

A beginner-first practice repo. You learn one concept, then solve a few problems that use only that concept. SQL follows [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) and [Advanced SQL 50](https://leetcode.com/studyplan/premium-sql-50/). PySpark uses the same problem shapes so the two skills reinforce each other.

If you know nothing about SQL or Spark, start at Day 1 in [STUDY_PLAN.md](STUDY_PLAN.md). Do not jump to LeetCode yet.

## How this repo is organized

```text
sql/            SQL lessons, local problems, LeetCode checklists
pyspark/        Spark lessons and the same problems in DataFrame API
tools/          checker that tells you if your query/script is right
```

Every module looks like this:

1. Read `lesson.md` (or the numbered lesson files).
2. Type the examples yourself in the playground or a starter file.
3. Solve the local problems. Run the checker.
4. Only then do the matching LeetCode problems and commit your solutions.

## Setup

You need Python 3.10+ and, for PySpark, a JDK (17 recommended).

```bash
cd sql-pyspark-practice
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tools/doctor.py
```

PySpark 4 needs **Java 17+**. If `doctor.py` says Java is missing or too old:

```bash
# macOS: use an installed 17+ JDK for this shell
source tools/env.sh
python tools/doctor.py
```

To install a JDK if you have none: `brew install openjdk@17`, then `source tools/env.sh` again.

## Daily loop

```bash
source .venv/bin/activate

# SQL
python tools/check.py sql/01-select/problems/01-organic-onsale

# PySpark (same problem, later in the plan)
python tools/check.py pyspark/01-select-filter/problems/01-organic-onsale
```

Edit `starter.sql` or `starter.py`. Leave `solution.*` closed until you have tried for about 20 minutes.

After you finish a problem:

1. Check the box in [PROGRESS.md](PROGRESS.md).
2. Copy your working query into `sql/solutions/` or `pyspark/solutions/` if you want a clean record.
3. Commit and push.

```bash
git add -A
git commit -m "practice: sql select organic-onsale"
git push
```

## Tracks

| Track | Where | What you learn |
| --- | --- | --- |
| SQL foundations | `sql/00-fundamentals/` | tables, SELECT, WHERE, NULL, ORDER BY |
| SQL 50 | `sql/01-select/` … `sql/07-strings/` | the 50 official problems, by topic |
| Advanced SQL | `sql/08-advanced/` | windows, CTEs, gaps/islands, pivot, trees |
| PySpark | `pyspark/` | same transformations, plus Spark-only ideas |

Local problems are original. They teach the same patterns as LeetCode without copying LeetCode text. Each module’s `leetcode.md` lists the official problems to submit on LeetCode.

## Rules that make this stick

- Read the lesson before the problems in that folder.
- Type examples. Do not paste them.
- When a check fails, name the edge case (NULL, duplicate, wrong grain) before opening the solution.
- After you peek, close the solution and rewrite from a blank starter.
- Say the pattern out loud: “filter two flags”, “left join to find missing matches”, “group then filter groups”.
