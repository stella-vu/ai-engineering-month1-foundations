CREATE TABLE IF NOT EXISTS basics.products_basic (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    stock INTEGER CHECK (stock >= 0) DEFAULT 0,
    --store larger whole numbers, which can exceed the limit of INTEGER
    total_views BIGINT DEFAULT 0,

    --store prices with up to 10 digits in total, and 2 digits after the decimal point (e.g., 99999999.99)
    price NUMERIC(10, 2) CHECK (price >= 0),

    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

-- insert data into the table
INSERT INTO basics.products_basic (name, description, stock, total_views, price) VALUES
('Laptop', 'A high-performance laptop suitable for gaming and work.', 50, 100
, 999.99),
('Smartphone', 'A latest model smartphone with advanced features.', 200, 500, 699.99),
('Headphones', 'Noise-cancelling over-ear headphones.', 150, 300, 199.99);


-- queries
SELECT * FROM basics.products_basic;