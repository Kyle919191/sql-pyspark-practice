# Select — applying the fundamentals

You already know the clauses. This module is reps: read a prompt, write a filter, return the asked columns.

## The habit

1. Write the grain of the answer (“one row per product”).
2. Write the WHERE in English, including what happens to NULL.
3. SELECT only the requested columns.
4. Add DISTINCT or ORDER BY only if the prompt needs them.

## Patterns in this folder

| Local problem | Pattern | Matching LeetCode |
| --- | --- | --- |
| `01-organic-onsale` | two equality filters with AND | 1757 |
| `02-customers-without-referrer` | `!=` plus `IS NULL` | 584 |
| `03-large-markets` | OR of two numeric predicates | 595 |
| `04-unique-viewers` | DISTINCT + inequality | 1148 |
| `05-too-short-posts` | `length(col)` | 1683 |

## After the local five

Submit the five LeetCode Select problems. Save accepted SQL under `sql/solutions/leetcode/`.
