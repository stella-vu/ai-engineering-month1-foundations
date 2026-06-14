CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL,
    dob DATE,
    registration_date DATE
);