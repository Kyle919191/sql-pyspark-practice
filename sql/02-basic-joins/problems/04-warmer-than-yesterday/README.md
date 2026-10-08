# Warmer than yesterday

**Pattern:** self-join on consecutive dates. **LeetCode cousin:** 197.

## Table: `weather`

| column | type |
| --- | --- |
| id | integer |
| record_date | date |
| temp | integer |

One row per day.

## Task

Return the `id` of each day whose temperature is **strictly greater** than the temperature on the previous calendar day.

If a day has no row for the calendar day before it, skip it.

Order does not matter.

## Example

```text
id  record_date  temp
1   2024-01-01   10
2   2024-01-02   12
3   2024-01-03   11
4   2024-01-05   20
```

- Jan 2 is warmer than Jan 1 → 2
- Jan 3 is cooler than Jan 2 → skip
- Jan 5 has no Jan 4 row → skip
