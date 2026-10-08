# Org-chart labels

**Pattern:** tree node types. **LeetCode cousin:** 608.

## Table: `staff(id, name, manager_id)`

`manager_id` is NULL for the root.

## Task

Return `id`, `name`, and `label`:

- `Root` — no manager
- `Inner` — someone reports to them
- `Leaf` — has a manager, and nobody reports to them

Order by `id`.
