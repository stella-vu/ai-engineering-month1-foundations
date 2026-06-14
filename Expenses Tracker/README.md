# Expense Tracker API

A backend Expense Tracker application built with FastAPI and PostgreSQL. This project demonstrates a complete data workflow from raw CSV data cleaning to database design and API development.

## Project Overview

The goal of this project is to build a production-style backend service for managing personal finance transactions.

The project covers:

- Data cleaning and preprocessing with Pandas
- PostgreSQL database design and data import
- FastAPI REST API development
- CRUD operations
- Filtering and pagination
- File upload handling
- Input validation with Pydantic
- Error handling and logging

## Architecture

```text
Raw Dataset
    ↓
Data Cleaning (Pandas)
    ↓
PostgreSQL Database
    ↓
FastAPI Service Layer
    ↓
REST API Endpoints
```

## Features

### Transaction Management
- Create transactions
- Retrieve transactions
- Update transactions
- Delete transactions

### Filtering & Pagination
- Filter by user_id
- Filter by transaction_type
- Filter by category
- Filter by amount range
- Limit and offset pagination

### File Uploads
Supported file types:
- PDF
- CSV
- TXT

### Validation
- Pydantic request validation
- Transaction type validation
- Payment mode validation
- Amount validation

### Error Handling & Logging
- HTTP exceptions
- Database error handling
- Application logging

## Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn

### Database
- PostgreSQL
- psycopg2

### Data Processing
- Pandas

### Validation
- Pydantic

### Configuration
- python-dotenv

## Project Structure

```text
expense-tracker-api/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── schemas.py
│   └── transaction_service.py
│
├── data/
│   ├── budgetwise_synthetic_dirty.csv
│   ├── budgetwise_synthetic_cleaned.csv
│   ├── categories.csv
│   └── synthetic_users.csv
│
├── data_processing/
│   ├── clean_data.ipynb
│   ├── generate_users.py
│   └── list_category.py
│
├── sql/
│   ├── ddl_users.sql
│   ├── ddl_categories.sql
│   └── ddl_transactions.sql
│
├── docs/
│   ├── api_documentation.md
│   ├── csv_to_postgresql.md
│   ├── data_cleaning_process.md
│   ├── database_schema.md
│   ├── project_overview.md
│   └── setup_guide.md
│
├── screenshots/
│   ├── Create Transaction.png
│   ├── File Upload.png
│   ├── Get Transactions.png
│   └── Swagger Documentation.png
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Dataset

Source dataset:

`budgetwise_synthetic_dirty.csv`

Data cleaning tasks:
- Removed duplicate records
- Fixed inconsistent date formats
- Cleaned amount values
- Standardized categories
- Corrected category typos
- Validated transaction types
- Standardized text fields
- Removed invalid records

Output dataset:

`budgetwise_synthetic_cleaned.csv`

## Database Design

The application uses three tables:

- Users
- Categories
- Transactions

Example transaction ID:

```text
T15001
```

Transaction IDs are automatically generated from a PostgreSQL sequence-backed transaction number.

See `docs/database_schema.md` for full details.

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /transactions | Retrieve transactions |
| GET | /transactions/{transaction_id} | Retrieve a transaction |
| POST | /transactions | Create transaction |
| PUT | /transactions/{transaction_id} | Update transaction |
| DELETE | /transactions/{transaction_id} | Delete transaction |
| POST | /upload | Upload file |

See `docs/api_documentation.md` for complete examples.

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd expense-tracker-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
POSTGRES_PASSWORD=your_password
```

### Create Database

```sql
CREATE DATABASE expense_tracker;
```

### Run SQL Scripts

```bash
psql -U postgres -d expense_tracker -f sql/ddl_users.sql
psql -U postgres -d expense_tracker -f sql/ddl_categories.sql
psql -U postgres -d expense_tracker -f sql/ddl_transactions.sql
```

### Run Application

```bash
fastapi dev app/main.py
```

Open:

```text
http://localhost:8000/docs
```

## Screenshots

### Swagger Documentation
<img src="screenshots/Swagger Documentation.png" width="600" height="600" alt="Swagger Documentation" />

### Get Transactions
<img src="screenshots/Get Transactions.png" width="600" height="600" alt="Get Transactions" />

### Create Transaction
<img src="screenshots/Create Transaction.png" width="600" height="600" alt="Create Transaction" />

### File Upload
<img src="screenshots/File Upload.png" width="600" height="600" alt="File Upload" />


## Future Improvements

- JWT Authentication
- User-specific transaction access
- Receipt OCR processing
- AI-powered transaction categorization
- Expense analytics dashboard
- RAG-based financial assistant

## Learning Outcomes

This project demonstrates practical experience with:

- Python backend development
- FastAPI
- PostgreSQL
- SQL schema design
- Data cleaning with Pandas
- API design
- Validation and error handling
- Dependency injection
- File uploads
- Logging and debugging
