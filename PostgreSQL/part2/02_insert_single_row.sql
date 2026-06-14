INSERT INTO products (
    name, category, price, stock, sku, description
) 
VALUES (
    'Wireless Mouse', 'Electronics', 29.99, 100, 'WM122', 'A comfortable wireless mouse with long battery life.'
);

SELECT * FROM products
WHERE sku = 'WM122';