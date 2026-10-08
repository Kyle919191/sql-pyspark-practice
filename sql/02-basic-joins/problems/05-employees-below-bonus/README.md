# Employees below bonus threshold

**Pattern:** LEFT JOIN, then keep “missing or small”. **LeetCode cousin:** 577.

## Tables

`employees(id, name, supervisor_id)`  
`bonuses(emp_id, bonus)` — not every employee has a bonus row

## Task

Return `name` and `bonus` for employees whose bonus is **less than 500**, including employees who have **no bonus row** (treat that as “below threshold”; `bonus` should be NULL).

Order does not matter.

## Trap

`WHERE bonus < 500` alone drops NULLs. You want missing bonuses too.
