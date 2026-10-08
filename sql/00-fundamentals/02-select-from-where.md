# SELECT, FROM, WHERE

This is 80% of easy SQL. Everything later is this idea plus one new clause.

## Skeleton

```sql
SELECT column_a, column_b
FROM table_name
WHERE some_condition;
```

- `FROM` names the input table.
- `WHERE` is a yes/no test for each row. The row is kept only if the test is true.
- `SELECT` lists output columns. `SELECT *` means “all columns”. Useful while exploring, sloppy as a final answer.

## Comparisons you will use constantly

```sql
price_cents >= 300
name = 'oats'          -- text in single quotes
in_stock = true
id <> 3                -- not equal; != also works
```

Text matching is exact. `'Oats'` is not `'oats'` in DuckDB (LeetCode MySQL string compares are often case-insensitive — do not rely on that).

## AND / OR

```sql
WHERE in_stock = true AND price_cents < 400
WHERE name = 'kale' OR name = 'oats'
```

AND is stricter (both must be true). OR is looser (either). Use parentheses when you mix them:

```sql
WHERE in_stock = true AND (name = 'kale' OR name = 'oats')
```

## Aliases

Rename a column in the result:

```sql
SELECT name AS product_name, price_cents / 100.0 AS price_dollars
FROM products;
```

`AS` is optional. Use it. Future you will thank you.

## Computed columns

`SELECT` can create values that are not stored:

```sql
SELECT name, price_cents * 2 AS double_price
FROM products;
```

## Pattern: filter then project

Almost every easy LeetCode problem is:

1. Name the table (`FROM`)
2. Write the row rule (`WHERE`)
3. List the columns the prompt asked for (`SELECT`), in the order it asked

Do not add extra columns. Do not forget a column. The checker and LeetCode both care.

## Common mistakes

- Using double quotes for text (`"oats"`). SQL strings are single quotes.
- Filtering in `SELECT` instead of `WHERE`. `SELECT` does not drop rows.
- Comparing a number to a string by accident (`price_cents = '399'` can bite you by dialect).

## Practice in the playground

Open `sql/00-fundamentals/playground/starter.sql` and write:

1. All products cheaper than 300 cents.
2. Only the `name` of in-stock products.
3. `name` and a column `price_dollars`.

There is no expected file for those three — you are exploring. When you move to `sql/01-select/problems/`, the checker starts scoring you.

## You're ready when

You can translate an English sentence like “names of in-stock products under $3” into one SELECT/FROM/WHERE without looking at notes.
