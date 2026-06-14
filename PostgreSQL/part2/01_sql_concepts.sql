CREATE EXTENSION IF NOT EXISTS pgcrypto;

DROP TABLE IF EXISTS products;
CREATE TABLE IF NOT EXISTS products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0) DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE NOT NULL,
    sku TEXT UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, category, price, stock,is_active, sku, description) VALUES
('Laptop', 'Electronics', 999.99, 50, TRUE, 'LAP123', 'A high-performance laptop suitable for gaming and work.'),
('Smartphone', 'Electronics', 699.99, 200, TRUE, 'SMP456', 'A latest model smartphone with advanced features.'),
('Headphones', 'Audio', 199.99, 150, TRUE, 'HDP789', 'Noise-cancelling over-ear headphones.'),
('Coffee Maker', 'Home Appliances', 49.99, 100, TRUE, 'CMK321', 'A compact coffee maker for quick and easy brewing.'),
('Electric Kettle', 'Home Appliances', 29.99, 80, TRUE, 'EKT654', 'A fast-boiling electric kettle with auto shut-off.'),
('Gaming Chair', 'Furniture', 199.99, 20, TRUE, 'GCH987', 'Ergonomic gaming chair with adjustable features.'),
('Office Desk', 'Furniture', 299.99, 15, TRUE, 'ODK543', 'Spacious office desk with cable management system.'),
('Smart Watch', 'Wearables', 199.99, 120, TRUE, 'SWT210', NULL),
('Bluetooth Speaker', 'Audio', 89.99, 60, TRUE, 'BSP432', 'Portable Bluetooth speaker with high-quality sound.'),
('Air Purifier', 'Home Appliances', 149.99, 30, TRUE, 'APF876', 'Air purifier with HEPA filter for cleaner air.');

SELECT * FROM products;