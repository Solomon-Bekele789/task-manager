from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, tasks

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A professional task management API built with FastAPI",
    version="1.0"
)

# Register routers
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def home():
    return {
        "message": "Task Manager API 🚀",
        "docs": "Visit /docs to test all endpoints",
        "version": "1.0",
        "endpoints": {
            "auth": ["/auth/register", "/auth/login"],
            "tasks": ["/tasks", "/tasks/{id}"]
        }
    }