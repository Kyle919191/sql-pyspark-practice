# Large markets

**Pattern:** keep a row if **either** threshold is met. **LeetCode cousin:** 595.

## Table: `markets`

| column | type |
| --- | --- |
| name | text |
| area_km2 | integer |
| population | integer |

One row per city.

## Task

A market is large if `area_km2 >= 3000000` **or** `population >= 25000000`.

Return `name`, `area_km2`, and `population` for large markets.

Order does not matter.

## Example

```text
name       area_km2   population
Lumen      9600000    18000000
Harbor     120000     31000000
Pebble     80000      900000
Ridge      3400000    4000000
```

Expected: Lumen (area), Harbor (population), Ridge (area).
