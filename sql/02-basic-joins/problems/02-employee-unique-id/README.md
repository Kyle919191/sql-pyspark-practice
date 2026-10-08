# Employee unique ids

**Pattern:** LEFT JOIN, keep employees with no id. **LeetCode cousin:** 1378.

## Tables

`employees(id, name)`  
`employee_ids(id, unique_id)` — not every employee has a row

## Task

Return every employee’s `unique_id` and `name`. If they have no unique id, `unique_id` should be NULL.

Order does not matter.
