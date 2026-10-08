# Movie and user favorites

**Pattern:** two CTEs, then UNION. **LeetCode cousin:** 1341.

## Tables

`movies(movie_id, title)`  
`users(user_id, name)`  
`reviews(user_id, movie_id, rating, created_on)`

## Task

Return one column `results` with **exactly two rows**, in this order:

1. The user who gave the most reviews. Tie → the name that is lexicographically smaller.
2. The movie with the highest average rating. Tie → the title that is lexicographically smaller.
