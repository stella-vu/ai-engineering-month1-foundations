-- DROP TABLE IF EXISTS transactions;

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(6) GENERATED ALWAYS AS ('T' || LPAD(transaction_number::text, 5, '0')) STORED,
    user_id TEXT NOT NULL,
    date DATE,
    transaction_type VARCHAR(50),
    category VARCHAR(50),
    amount NUMERIC(10, 2),
    payment_mode VARCHAR(50),
    location VARCHAR(50),
    notes TEXT,
    transaction_number SERIAL PRIMARY KEY
);

