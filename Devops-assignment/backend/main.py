import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from worker import notify_task

app = FastAPI(title="Health Pay Notify API")

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/notify/")
def notify():
    task = notify_task.delay()
    return {"task_id": task.id, "status": "queued"}

@app.get("/task_status/{task_id}")
def task_status(task_id: str):
    task = notify_task.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result if task.status == "SUCCESS" else None,
    }

@app.get("/health")
def health():
    return {"status": "ok"}