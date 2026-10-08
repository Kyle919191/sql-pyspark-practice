# Select and filter in PySpark

Read `pyspark/00-fundamentals/03-sql-to-pyspark.md` if you have not.

These five problems are the SQL Select set. Open the SQL `README.md` in the twin folder if you want the original wording. Same tables, same answers.

```python
result = products.filter(
    (F.col("organic") == "Y") & (F.col("on_sale") == "Y")
).select("product_id", "name")
```

Do not copy that into every starter. Write it from the SQL you already understand.

## Twins

| PySpark | SQL folder |
| --- | --- |
| `01-organic-onsale` | `sql/01-select/problems/01-organic-onsale` |
| `02-customers-without-referrer` | `sql/01-select/problems/02-customers-without-referrer` |
| `03-large-markets` | `sql/01-select/problems/03-large-markets` |
| `04-unique-viewers` | `sql/01-select/problems/04-unique-viewers` |
| `05-too-short-posts` | `sql/01-select/problems/05-too-short-posts` |

## Footguns

- `df.filter(a == 1 and b == 2)` — SyntaxError or wrong. Use `&`.
- `df.filter(F.col("x") != 2)` drops NULL, same as SQL.
- `F.length` counts characters for these ASCII strings.
