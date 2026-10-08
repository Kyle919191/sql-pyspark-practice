# Too-short posts

**Pattern:** filter on `length(text)`. **LeetCode cousin:** 1683.

## Table: `posts`

| column | type |
| --- | --- |
| post_id | integer |
| content | text |

One row per post.

## Task

A post is invalid if `content` has 15 characters or fewer.

Return the `post_id` of every invalid post.

Order does not matter.

## Example

```text
post_id  content
1        hello world!!!!    -- 15 chars, invalid
2        a much longer post about sql
3        too short
```

Count characters yourself if you want to verify. Spaces count.
