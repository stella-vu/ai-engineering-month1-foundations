CREATE TABLE IF NOT EXISTS basics.value_examples (
    id SERIAL PRIMARY KEY,
    nickname TEXT,
    bio TEXT,
    score INTEGER
);

-- insert data into the table, including NULL values
INSERT INTO basics.value_examples (nickname, bio, score) VALUES
('Alice', 'Loves hiking and outdoor activities.', 85),
('Bob', NULL, 90), -- bio is NULL
(NULL, 'Enjoys cooking and trying new recipes.', 75), -- nickname is NULL
('Charlie', 'Avid reader and writer.', NULL); -- score is NULL