# 🚀 AI Engineering Month 1 - Foundations

A practical backend engineering repository showcasing Python applications with APIs, FastAPI, SQL, JSON, async workflows, and document processing.

---

# 🎯 Goal

Demonstrate foundational backend and AI system skills through real Python projects built with clean architecture, database integration, HTTP APIs, and file processing.

---

# 🛠️ Projects

---

## 📈 1. Crypto/API Tracker

A Python tracker that collects live cryptocurrency prices and market data from public APIs, then formats it for easy monitoring.

### ✨ Features
- Fetches live crypto data with `requests`
- Parses JSON responses cleanly
- Handles API errors and retries
- Logs activity for debugging
- Configures API keys and settings with environment variables
- Keeps code modular for reuse and testing

### 🧠 Skills Practiced
- REST API integration
- JSON parsing and data transformation
- Error handling and retry logic
- Environment-based configuration
- Logging and clean data flows

### 🎥 Demo
Preview: live price trends, top cryptocurrency summaries, and structured API response display.

<img src="Crypto Tracker/assets/dashboard.gif" alt="Crypto Tracker Dashboard" width="800px" />

---

## 💰 2. Expenses Tracker

A backend expense tracker using SQLite, built for recording and analyzing spending by category and month.

### ✨ Features
- Create, read, update, and delete expense records
- Categorize expenses with reusable labels
- Generate monthly spending summaries
- Store data safely in SQLite
- Follow a modular service-and-schema design

### 🧠 Skills Practiced
- PostgreSQL database integration
- SQL query design
- CRUD application structure
- Data validation with Python schemas
- Building maintainable backend modules
---

## ⚡ 3. FastAPI Backend Task API

A clean FastAPI app with task management endpoints, validation, and auto-generated OpenAPI documentation.

### ✨ Features
- CRUD task endpoints
- Pydantic request validation
- Swagger UI documentation
- Structured JSON responses
- Optional database integration support

### 🧠 Skills Practiced
- FastAPI development
- Pydantic modeling
- RESTful API design
- API docs with OpenAPI
- Clean endpoint structure

### 🎥 Demo
<img src="Expenses Tracker/screenshots/Swagger Documentation.png" alt="FastAPI Backend Task API" width="800px" />

---

## 📄 4. Document Upload API

A file upload service for ingesting and processing PDF and text documents, with metadata extraction and async handling.

### ✨ Features
- Upload PDF and text files via API
- Extract and parse document text
- Support async file processing
- Store metadata and upload details
- Deliver JSON response summaries

### 🧠 Skills Practiced
- Async Python patterns
- File upload handling
- Document parsing and extraction
- FastAPI endpoint design
- Building AI-ready backend workflows

### 🎥 Demo
<img src="Expenses Tracker/screenshots/File Upload.png" alt="Document Upload API" width="800px" />

---

# 🧰 Technologies Used

- 🐍 Python
- ⚡ FastAPI
- 🗄️ SQLite
- 📦 Pydantic
- 🌐 Requests
- 📬 Postman
- 🧠 Git & GitHub
- 📄 PyPDF2 / pdfplumber

---

# 📂 Folder Structure

```bash
ai-engineering-month1-foundations/
│
├── Crypto Tracker/
├── Expenses Tracker/
├── fast_api/
├── http_method/
├── PostgreSQL/
├── README.md
└── requirements.txt
```
