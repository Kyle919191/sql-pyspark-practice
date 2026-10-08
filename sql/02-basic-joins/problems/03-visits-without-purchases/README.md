# Visits without purchases

**Pattern:** anti-join (LEFT JOIN + right key IS NULL). **LeetCode cousin:** 1581.

LeetCode 1581 then counts those visits per customer. Do that after the aggregates lesson. Here you only find the unmatched visits.

## Tables

`visits(visit_id, customer_id)` — one row per store visit  
`purchases(purchase_id, visit_id)` — one row per purchase; a visit can have many or none

## Task

Return `visit_id` and `customer_id` for every visit that has **no** purchase.

Order does not matter.

## Example

Visits 1 and 5 have purchases. Visits 2, 3, 4 do not. Return those three visits.
