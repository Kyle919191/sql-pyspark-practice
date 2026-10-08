# Gaps and islands

An **island** is a consecutive run of rows that belong together (available seats in a row, days in the same status, ids with no gaps).

A **gap** is the hole between islands.

## The classic trick

Number the rows two ways. Their difference is constant inside an island.

```sql
WITH marked AS (
    SELECT
        seat_id,
        seat_id - row_number() OVER (ORDER BY seat_id) AS island
    FROM seats
    WHERE available = true
)
SELECT
    min(seat_id) AS start_id,
    max(seat_id) AS end_id
FROM marked
GROUP BY island;
```

Why it works: consecutive ids go 3,4,5 and row_numbers go 1,2,3. Differences are all 2. A jump in `seat_id` changes the difference.

LeetCode 1285 (start and end of continuous ranges) is this.

## Consecutive available seats (603)

Keep seats where `available` and a neighbor (id-1 or id+1) is also available. Self-join or `LAG`/`LEAD` on availability.

## Contiguous dates (1225)

You have success days and fail days as two streams. You want start/end of each consecutive run of the same status.

1. UNION the two streams with a status column
2. Island key = `date - row_number()` per status
3. `GROUP BY` status, island → min/max date

## Missing ids (1613)

Generate 1..max(id), anti-join the existing ids. Recursive CTE or a numbers table.

## Pattern

1. Define what “consecutive” means (id+1, next calendar day, next row after a filter)
2. Build an island key (`col - row_number()`, or `date - INTERVAL row_number DAY`)
3. Aggregate min/max per island

## You're ready when

You can explain why `id - row_number()` is constant on a run and changes after a gap. Then the local contiguous-status problem.
