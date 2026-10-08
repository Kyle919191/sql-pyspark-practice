# Previous-day delta

**Pattern:** LAG. **LeetCode cousin:** 197, rewritten with a window.

## Table: `weather(record_date, temp)`

One row per day, not necessarily consecutive calendar days. “Previous” means the previous **row by date**, not date-1.

## Task

Return `record_date`, `temp`, `prev_temp`, and `delta` (`temp - prev_temp`). The first day has NULL `prev_temp` and NULL `delta`.

Order by `record_date`.
