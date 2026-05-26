import os

from celery import Celery


redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "absalom_command_center",
    broker=redis_url,
    backend=redis_url,
    include=["services.worker.tasks"],
)

celery_app.conf.update(
    task_track_started=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)
