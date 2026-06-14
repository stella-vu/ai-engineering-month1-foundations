## Overview

The Expense Tracker uses a normalized PostgreSQL database with three main entities: Users, Categories, and Transactions. All database schemas are defined in SQL files located in the `sql/` folder.

## SQL Files

The database schema is maintained through the following SQL files:

- [ddl_users.sql](../sql/ddl_users.sql) — Users table definition
- [ddl_categories.sql](../sql/ddl_categories.sql) — Categories table definition
- [ddl_transactions.sql](../sql/ddl_transactions.sql) — Transactions table definition

To initialize the database, execute these files in order:

```bash
psql -U postgres -d expense_tracker -f sql/ddl_users.sql
psql -U postgres -d expense_tracker -f sql/ddl_categories.sql
psql -U postgres -d expense_tracker -f sql/ddl_transactions.sql
```

## Tables

### 1. Users Table

Stores user account information.

**Table Name:** `users`

**File:** [sql/ddl_users.sql](../sql/ddl_users.sql)

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `user_id` | TEXT | PRIMARY KEY | Unique user identifier |
| `first_name` | VARCHAR(100) | | User's first name |
| `last_name` | VARCHAR(100) | | User's last name |
| `email` | VARCHAR(100) | UNIQUE, NOT NULL | User email address |
| `dob` | DATE | | Date of birth |
| `registration_date` | DATE | | Account registration date |

---

### 2. Categories Table

Stores transaction categories.

**Table Name:** `categories`

**File:** [sql/ddl_categories.sql](../sql/ddl_categories.sql)

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `category_id` | SERIAL | PRIMARY KEY | Auto-incrementing category ID |
| `category_name` | VARCHAR(100) | UNIQUE, NOT NULL | Category name |

---

### 3. Transactions Table

Stores individual transaction records.

**Table Name:** `transactions`

**File:** [sql/ddl_transactions.sql](../sql/ddl_transactions.sql)

**Columns:**

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `transaction_id` | VARCHAR | GENERATED STORED | Auto-generated transaction ID (format: T + 5-digit number) |
| `transaction_number` | SERIAL | PRIMARY KEY | Internal sequence counter |
| `user_id` | TEXT | NOT NULL | Reference to users table |
| `date` | DATE | | Transaction date |
| `transaction_type` | VARCHAR(50) | | Type of transaction (e.g., income, expense) |
| `category` | VARCHAR(50) | | Transaction category |
| `amount` | NUMERIC(10, 2) | | Transaction amount |
| `payment_mode` | VARCHAR(50) | | Payment method (card, cash, etc.) |
| `location` | VARCHAR(50) | | Transaction location |
| `notes` | TEXT | | Additional notes |



## Key Relationships

### User to Transactions
- One user can have many transactions
- Each transaction must reference the user via `user_id`
- Relationship: **1:N**

### Category to Transactions
- One category can have many transactions
- A transaction belongs to one category
- Relationship: **1:N**

## Constraints

1. **Primary Keys:** Uniquely identify each record
2. **UNIQUE:** Prevents duplicate values (email, category_name)
3. **NOT NULL:** Ensures required data is present (email, category_name, user_id)
4. **GENERATED:** transaction_id is automatically generated from transaction_number

## Indexes

For optimal query performance, consider creating the following indexes:

```sql
CREATE INDEX idx_transactions_user_id ON transactions(user_id);
CREATE INDEX idx_transactions_date ON transactions(date);
CREATE INDEX idx_transactions_category ON transactions(category);
CREATE INDEX idx_users_email ON users(email);
```

## Data Integrity

- **Unique Constraints:** Email addresses and category names are unique
- **Auto-Generated IDs:** Transaction IDs are automatically generated using SERIAL and string formatting

## Common Queries

### Get all transactions for a user

```sql
SELECT * FROM transactions 
WHERE user_id = 'U001' 
ORDER BY date DESC;
```

### Get transactions by category

```sql
SELECT t.* FROM transactions t
WHERE t.category = 'Food'
ORDER BY t.date DESC;
```

### Get total spending by category

```sql
SELECT category, SUM(amount) as total
FROM transactions
WHERE transaction_type = 'Expense'
GROUP BY category
ORDER BY total DESC;
```

### Get monthly expense summary

```sql
SELECT DATE_TRUNC('month', date) as month, SUM(amount) as total
FROM transactions
WHERE transaction_type = 'Expense'
GROUP BY DATE_TRUNC('month', date)
ORDER BY month DESC;
```

## Performance Considerations

1. **Indexing:** Add indexes on frequently queried columns (user_id, date, category)
2. **Normalization:** Schema is normalized to reduce data redundancy
3. **Data Types:** Appropriate types for efficient storage and queries
4. **Partitioning:** Consider partitioning transactions by date for large datasets

## Related Documentation

- [API Documentation](api_documentation.md)
- [Setup Guide](setup_guide.md)
- [Data Cleaning Process](data_cleaning_process.md)
- [CSV to PostgreSQL Guide](csv_to_postgresql.md)
