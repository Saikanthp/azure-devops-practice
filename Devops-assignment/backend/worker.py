import os
import time
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "worker",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
)

notify_task = celery_app.task(name="notify_task")(lambda: None)

@celery_app.task(name="notify_task")
def notify_task():
    time.sleep(int(os.getenv("TASK_SLEEP_SECONDS", "5")))
    return {"message": "Notification sent successfully!", "status": "done"}