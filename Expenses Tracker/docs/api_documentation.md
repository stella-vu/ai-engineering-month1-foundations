## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. Future versions will include API key or JWT-based authentication.

## Response Format

All responses are in JSON format. Successful responses return HTTP 200, while errors return appropriate HTTP status codes.

## Endpoints

### 1. Get Transactions

**Endpoint:** `GET /transactions`

**Description:** Retrieve transactions with filtering and pagination support.

**Query Parameters:**

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `user_id` | string | Filter by user ID | No |
| `transaction_type` | string | Filter by type (income/expense) | No |
| `category` | string | Filter by category | No |
| `min_amount` | float | Minimum transaction amount | No |
| `max_amount` | float | Maximum transaction amount | No |
| `limit` | integer | Results per page (default: 20, max: 100) | No |
| `offset` | integer | Number of records to skip (default: 0) | No |

**Example Request:**

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/transactions?user_id=U001&category=Food&min_amount=50&limit=20&offset=0' \
  -H 'accept: application/json'
```

**Response:**

```json
[
  {
    "date": "2021-11-19",
    "transaction_type": "Expense",
    "category": "Food",
    "amount": "1421.00",
    "payment_mode": "Bank Transfer",
    "location": "Pune",
    "notes": null,
    "transaction_id": "T14657",
    "user_id": "U001"
  },
  ...
]
```

**Status Codes:**
- `200 OK` - Transactions retrieved successfully

---

### 2. Get Transaction by ID

**Endpoint:** `GET /transactions/{transaction_id}`

**Description:** Retrieve a specific transaction by its ID.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `transaction_id` | string | Unique transaction identifier |

**Example Request:**

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/transactions/T00001' \
  -H 'accept: application/json'
```

**Response:**

```json
{
  "date": "2022-05-16",
  "transaction_type": "Expense",
  "category": "Entertainment",
  "amount": "492.00",
  "payment_mode": "Card",
  "location": "Chennai",
  "notes": "Dinner at resto",
  "transaction_id": "T00001",
  "user_id": "U175"
}
```

**Status Codes:**
- `200 OK` - Transaction found
- `404 Not Found` - Transaction not found

---

### 3. Create Transaction

**Endpoint:** `POST /transactions`

**Description:** Create a new transaction record.

**Request Body:**

```json
{
  "date": "2026-06-12",
  "transaction_type": "Expense",
  "category": "string",
  "amount": 1,
  "payment_mode": "Cash",
  "location": "string",
  "notes": "string",
  "user_id": "string"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/transactions" \
  -H "Content-Type: application/json" \
  -d '{
  "date": "2026-06-12",
  "transaction_type": "Expense",
  "category": "Rent",
  "amount": 500,
  "payment_mode": "Cash",
  "location": "Sydney",
  "notes": "Studio Rent",
  "user_id": "U012"
  }'
```

**Response:**

```json
{
  "message": "Add transaction successfully",
  "transaction_id": "T15012",
  "detail": {
    "date": "2026-06-12",
    "transaction_type": "Expense",
    "category": "Rent",
    "amount": "500",
    "payment_mode": "Cash",
    "location": "Sydney",
    "notes": "Studio Rent",
    "user_id": "U012"
  }
}
```

**Status Codes:**
- `201 Created` - Transaction created successfully
- `400 Bad Request` - Invalid request body

---

### 4. Update Transaction

**Endpoint:** `PUT /transactions/{transaction_id}`

**Description:** Update an existing transaction.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `transaction_id` | string | Unique transaction identifier |

**Request Body:** (same as Create Transaction)

**Example Request:**

```bash
curl -X PUT "http://localhost:8000/transactions/T00001" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 50.00,
    "notes": "Updated lunch expense"
  }'
```

**Status Codes:**
- `200 OK` - Transaction updated successfully
- `404 Not Found` - Transaction not found
- `400 Bad Request` - Invalid request body

---

### 5. Delete Transaction

**Endpoint:** `DELETE /transactions/{transaction_id}`

**Description:** Delete a transaction.

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `transaction_id` | string | Unique transaction identifier |

**Example Request:**

```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/transactions/T15011' \
  -H 'accept: application/json'
```

**Response:**

```json
{
  "message": "Successfully deleted transaction T15011"
}
```

**Status Codes:**
- `200 OK` - Transaction deleted successfully
- `404 Not Found` - Transaction not found

---

### 6. Upload File

**Endpoint:** `POST /upload`

**Description:** Upload transaction files (PDF, CSV, or TXT).

**Request Body:** Form data with file

**Supported File Types:**
- `application/pdf` - PDF files
- `text/csv` - CSV files
- `text/plain` - TXT files

**Example Request:**

```bash
curl -X POST "http://localhost:8000/upload" \
  -F "file=@transactions.csv"
```

**Response:**

```json
{
  "file_name": "transactions.csv",
  "content_type": "text/csv",
  "size_bytes": 1024
}
```

**Status Codes:**
- `200 OK` - File uploaded successfully
- `400 Bad Request` - Unsupported file type

---

## Error Handling

### Common Error Responses

**404 Not Found:**
```json
{
  "detail": "Transaction not found"
}
```

**400 Bad Request:**
```json
{
  "detail": "Invalid request parameters"
}
```

**500 Internal Server Error:**
```json
{
  "detail": "Internal server error"
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. This may be added in future versions.

---

## Interactive API Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation where you can test all endpoints directly.

---

For setup instructions, see [setup_guide.md](setup_guide.md)

For database schema, see [database_schema.md](database_schema.md)
