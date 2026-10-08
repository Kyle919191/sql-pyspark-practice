CREATE TABLE movies (
    movie_id INTEGER,
    title VARCHAR
);

INSERT INTO movies VALUES
    (1, 'Avengers'),
    (2, 'Frozen'),
    (3, 'Dune');

CREATE TABLE users (
    user_id INTEGER,
    name VARCHAR
);

INSERT INTO users VALUES
    (1, 'Ada'),
    (2, 'Bea'),
    (3, 'Cal');

CREATE TABLE reviews (
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    created_on DATE
);

INSERT INTO reviews VALUES
    (1, 1, 5, DATE '2024-02-01'),
    (1, 2, 3, DATE '2024-02-02'),
    (1, 3, 4, DATE '2024-02-03'),
    (2, 1, 5, DATE '2024-02-01'),
    (2, 2, 5, DATE '2024-02-04'),
    (3, 2, 5, DATE '2024-02-05');
