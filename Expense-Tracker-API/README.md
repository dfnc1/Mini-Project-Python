Oke, ini adalah draft **README.md** untuk **Expense Tracker API** kamu, disesuaikan dengan format yang kamu berikan tapi sudah ditambahkan instruksi **Docker** dan tools **UV** yang terbaru:

```markdown
# Expense Tracker API

A robust REST API for an Expense Tracker built with FastAPI and PostgreSQL, featuring secure JWT Authentication, smart date filtering, and fully containerized with Docker.

## Requirements

* Docker & Docker Compose
* Python 3.10+ (if running locally)
* UV (Python package manager)
* PostgreSQL

## Installation

### 1. Clone Repo
```bash
git clone [https://github.com/username/Expense-Tracker-API.git](https://github.com/username/Expense-Tracker-API.git)
cd Expense-Tracker-API
```

### 2. Setup Environment
Create a `.env` file in the root directory and add these lines:
```env
DATABASE_URL="postgresql://user:password@db:5432/expense_db"
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_DB="expense_db"

# To generate a new secret key run: openssl rand -hex 32
SECRET_KEY="6d385d43458b4e3388943f46707cc37c48172089fb2a68d48c4483ea3ece8334"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. Run with Docker (Recommended)
You don't need to install dependencies or setup PostgreSQL manually.
```bash
docker-compose up --build
```

### 4. Run Locally (Alternative)
If you prefer running without Docker:

**Install Dependencies:**
```bash
uv sync
```

**Activate Virtual Environment:**
```bash
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

**Run Migration:**
```bash
alembic upgrade head
```

**Run App:**
```bash
uvicorn app.main:app --reload
```

## Features & Filters

This API provides flexible filtering for your expenses. You can use either a simple day offset or a custom date range.

### 1. Simple Day Offset
Input an integer to get data from the last X days.
* **Example:** `GET /expenses?filter_date=9` (Returns expenses from the last 9 days)

### 2. Custom Date Range
Input specific dates to get data between those periods.
* **Example:** `GET /expenses?start_date=2026-04-29&end_date=2026-04-30`

> **Note:** The API prioritizes `filter_date`. If `filter_date` is provided, `start_date` and `end_date` will be ignored.
## API Documentation

Once the server is running, open:
* **Swagger UI:** http://127.0.0.1:8000/docs
* **Redoc:** http://127.0.0.1:8000/redoc

---