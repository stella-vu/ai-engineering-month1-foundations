DROP TABLE IF EXISTS basics.students;

CREATE TABLE IF NOT EXISTS basics.students (
    -- Create an auto-incrementing primary key column named "id"
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 18),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 


-- inseting data into the table
INSERT INTO basics.students (name, email, age) VALUES
('Alice Johnson', 'alice.johnson@example.com', 45),
('Bob Smith', 'bob.smith@example.com', 22),
('Charlie Brown', 'charlie.brown@example.com', 31);
