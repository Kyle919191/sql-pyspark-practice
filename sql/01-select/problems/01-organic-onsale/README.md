# Organic and on sale

**Pattern:** keep rows that match two flags. **LeetCode cousin:** 1757.

## Table: `products`

| column | type |
| --- | --- |
| product_id | integer |
| name | text |
| organic | text, `'Y'` or `'N'` |
| on_sale | text, `'Y'` or `'N'` |

One row per product.

## Task

Return `product_id` and `name` of products that are both organic and on sale.

Order does not matter.

## Example

```text
product_id  name     organic  on_sale
1           apples   Y        Y
2           chips    N        Y
3           kale     Y        N
4           oats     Y        Y
```

Expected:

```text
product_id  name
1           apples
4           oats
```

## Hint

You need **both** conditions. That is `AND`, not `OR`.
