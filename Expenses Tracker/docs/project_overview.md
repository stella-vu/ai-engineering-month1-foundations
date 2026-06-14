# Project Overview

## Expense Tracker - A Full-Stack Data Pipeline & API

The **Expense Tracker** project demonstrates a complete data engineering and backend development workflow, from raw dataset cleanup to a PostgreSQL-backed FastAPI service.

### Project Goals

Provide a lightweight personal finance backend that supports transaction ingestion, storage, retrieval, and filtering with a clean database schema.

### Project Architecture

```
Raw data → Data cleaning → PostgreSQL database → FastAPI backend → Transaction API
```

### Key Features

1. **Data Cleaning Pipeline** - Scripts and notebooks for preparing raw datasets
2. **PostgreSQL Database** - Table definitions in the `sql/` folder
3. **FastAPI Backend** - Transaction API with read, create, update, and delete operations
4. **Filtering** - Filter transactions by user, type, category, amount range, limit, and offset
5. **Pagination** - Efficient results using `limit` and `offset`
6. **File Upload Endpoint** - Supports PDF, CSV, and TXT uploads
7. **Database-backed Transaction Storage** - Uses PostgreSQL via `psycopg2`
8. **Pydantic Validation** - Request and response schemas for transaction payloads

### Technologies Used

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL, psycopg2
- **Data Processing**: Pandas
- **Validation**: Pydantic
- **Environment Management**: python-dotenv

### Repository Structure

```
├── app/                          # FastAPI application code
│   ├── main.py                   # API endpoints and dependency wiring
│   ├── db.py                     # PostgreSQL connection helper
│   ├── schemas.py                # Pydantic models for transactions
│   └── transaction_service.py    # Transaction business logic and database queries
├── data/                         # Sample datasets and CSV files
│   ├── budgetwise_synthetic_cleaned.csv
│   ├── budgetwise_synthetic_dirty.csv
│   ├── categories.csv
│   └── synthetic_users.csv
├── data_processing/              # Data preparation scripts and notebooks
│   ├── clean_data.ipynb
│   ├── generate_users.py
│   └── list_category.py
├── sql/                          # Database DDL files
│   ├── ddl_users.sql
│   ├── ddl_categories.sql
│   └── ddl_transactions.sql
├── docs/                         # Project documentation
│   ├── api_documentation.md
│   ├── csv_to_postgresql.md
│   ├── data_cleaning_process.md
│   ├── database_schema.md
│   ├── project_overview.md
│   └── setup_guide.md
├── requirements.txt              # Python dependencies
└── README.md                     # Main project readme
```

### Data Model

- **Users**: Defined in `sql/ddl_users.sql` with `user_id`, `first_name`, `last_name`, `email`, `dob`, and `registration_date`
- **Categories**: Defined in `sql/ddl_categories.sql` with `category_name` and optional reference data from `data/categories.csv`
- **Transactions**: Defined in `sql/ddl_transactions.sql` and stored with `transaction_id`, `user_id`, `date`, `transaction_type`, `category`, `amount`, `payment_mode`, `location`, and `notes`

### API Endpoints

- `GET /transactions` - Retrieve transactions with optional filters (`user_id`, `transaction_type`, `category`, `min_amount`, `max_amount`, `limit`, `offset`)
- `GET /transactions/{transaction_id}` - Retrieve a single transaction by ID
- `POST /transactions` - Create a new transaction
- `PUT /transactions/{transaction_id}` - Update an existing transaction
- `DELETE /transactions/{transaction_id}` - Delete a transaction by ID
- `POST /upload` - Upload a file (PDF, CSV, TXT) for processing

### Notes

- Category values are stored directly on transactions as a string field.
- The repository does not currently expose separate category CRUD endpoints.
- Database credentials are loaded from environment variables via `python-dotenv` in `app/db.py`.

### Getting Started

See [setup_guide.md](setup_guide.md) for installation and environment setup.

For API details, see [api_documentation.md](api_documentation.md).

For schema details, see [database_schema.md](database_schema.md).
