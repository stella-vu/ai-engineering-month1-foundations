# Setup Guide

## Prerequisites

- Python 3.14
- PostgreSQL 12+
- Git
- pip (Python package manager)

## Installation Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "Expenses Tracker"
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up PostgreSQL Database

#### Create Database and User

```sql
-- Connect to PostgreSQL as admin
sudo -u postgres psql

-- Create database
CREATE DATABASE expense_tracker;

-- Create user
CREATE USER postgres WITH PASSWORD 'your_password';

-- Grant privileges
ALTER ROLE postgres SET client_encoding TO 'utf8';
ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
ALTER ROLE postgres SET default_transaction_deferrable TO on;
ALTER ROLE postgres SET default_transaction_read_only TO off;
GRANT ALL PRIVILEGES ON DATABASE expense_tracker TO postgres;

-- Exit psql
\q
```

#### Run SQL Schema Files

```bash
# Navigate to sql directory
cd sql/

# Create tables
psql -U postgres -d expense_tracker -f sql/ddl_users.sql
psql -U postgres -d expense_tracker -f sql/ddl_categories.sql
psql -U postgres -d expense_tracker -f sql/ddl_transactions.sql

cd ..
```

### 6. Create Environment Variables

Create a `.env` file in the project root:

```env
POSTGRES_PASSWORD=your_password
```

### 7. Load Sample Data (Optional)

```bash
# Generate users
python data_processing/generate_users.py

# Load cleaned data
python data_processing/list_category.py
```

### 8. Run the Application

```bash
fastapi dev app/main.py
```

The API will be available at `http://localhost:8000`

### 9. Access API Documentation

- **Swagger UI**: `http://localhost:8000/docs`

## Troubleshooting

### PostgreSQL Connection Error

- Verify PostgreSQL is running: `sudo systemctl status postgresql`
- Check database credentials in `.env` file
- Ensure database `expense_tracker` exists

### Module Not Found Errors

- Confirm virtual environment is activated
- Run `pip install -r requirements.txt` again

### Port Already in Use

If port 8000 is already in use:

```bash
fastapi dev app/main.py --port 8001
```

## Development

### Data Processing

The data pipeline is documented in `data_processing/clean_data.ipynb`. Run it with:

```bash
jupyter notebook data_processing/clean_data.ipynb
```

## Deployment

For production deployment, see platform-specific guides (Docker, Heroku, AWS, etc.)

---

For API documentation, see [api_documentation.md](api_documentation.md)
