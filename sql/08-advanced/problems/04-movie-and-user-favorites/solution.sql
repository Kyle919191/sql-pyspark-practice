-- TRY the starter first.
WITH user_counts AS (
    SELECT u.name, count(*) AS n
    FROM reviews AS r
    INNER JOIN users AS u ON r.user_id = u.user_id
    GROUP BY u.name
),
top_user AS (
    SELECT name
    FROM user_counts
    ORDER BY n DESC, name
    LIMIT 1
),
movie_avg AS (
    SELECT m.title, avg(r.rating) AS avg_rating
    FROM reviews AS r
    INNER JOIN movies AS m ON r.movie_id = m.movie_id
    GROUP BY m.title
),
top_movie AS (
    SELECT title
    FROM movie_avg
    ORDER BY avg_rating DESC, title
    LIMIT 1
)
SELECT name AS results FROM top_user
UNION ALL
SELECT title FROM top_movie;
