# Unique viewers

**Pattern:** DISTINCT on the columns that define a unique pair. **LeetCode cousin:** 1148.

## Table: `views`

| column | type |
| --- | --- |
| article_id | integer |
| viewer_id | integer |
| author_id | integer |

One row per view event. The same person can view the same article more than once.

## Task

Find viewers who viewed someone else's article (viewer_id != author_id).

Return each such `viewer_id` once.

Order does not matter.

## Example

```text
article_id  viewer_id  author_id
1           10         3
1           10         3
2           7          7
3           10         4
3           8          4
```

- 10 viewed articles 1 and 3 (not their own) → include 10 once
- 7 viewed their own article → exclude
- 8 viewed article 3 → include 8

Expected: 8 and 10.
