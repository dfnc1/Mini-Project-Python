# Todo List API

---
A simple REST API for a Todo List built with FastAPI and PostgreSQL, featuring secure JWT Authentication.

## Requirements
- Python 3.14+
- UV
- PostgreSQL

## Installation

---
1. Clone Repo
```commandline
git clone https://github.com/dfnc1/Mini-Project-Python.git
cd ./Mini-Project-Python/Blogging-Platform-API/
```
2. Install Depedencies 
```commandline
uv sync
```
3. Activate Virtual Environment
```commandline
source .venv/bin/activate
```
4. Create `.env` file and add this line
```dotenv
DB_URL="postgresql://username:password@localhost:port/db-name"
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY="6d385d43458b4e3388943f46707cc37c48172089fb2a68d48c4483ea3ece8334"
ALGORITHM="HS256"
```
5. Migration
```commandline
alembic upgrade head
```
6. Run App
```commandline
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, open:

> http://127.0.0.1:8000/docs
> 
> or
> 
> http://127.0.0.1:8000/redoc
