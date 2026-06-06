# Task Manager API 🚀

A professional REST API built with Python and FastAPI.

## Features
- ✅ User registration and login
- ✅ JWT authentication
- ✅ Create, read, update, delete tasks
- ✅ Filter tasks by priority and status
- ✅ Persistent database with SQLAlchemy
- ✅ Professional project structure

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Deployed on Railway

## Live API
🌐 [View Live API](https://solomon-tasks.up.railway.app/docs)

## Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Create account |
| POST | /auth/login | Login and get token |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /tasks | Create a task |
| GET | /tasks | Get all my tasks |
| GET | /tasks/{id} | Get one task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Developer
**Solomon Bekele** — Python Backend Developer
- GitHub: github.com/Solomon-Bekele789