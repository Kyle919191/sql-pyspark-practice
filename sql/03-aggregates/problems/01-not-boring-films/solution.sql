-- TRY the starter first.
SELECT id, title, description, rating
FROM films
WHERE id % 2 = 1 AND description != 'boring'
ORDER BY rating DESC;
