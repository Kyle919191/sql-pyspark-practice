# Group tags by day

**Pattern:** string_agg / GROUP_CONCAT of distinct values. **LeetCode cousin:** 1484.

## Table: `events(event_date, tag)`

The same tag can be logged twice on one day.

## Task

For each `event_date`, return:

- `event_date`
- `n_tags` — distinct tags that day
- `tags` — those tags joined with commas, **sorted alphabetically**

Order by `event_date`.
