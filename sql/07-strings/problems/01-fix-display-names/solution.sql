-- TRY the starter first.
SELECT
    user_id,
    upper(substr(name, 1, 1)) || lower(substr(name, 2)) AS name
FROM users
ORDER BY user_id;
