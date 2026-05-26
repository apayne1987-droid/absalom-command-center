import os

from celery import Celery

from services.worker.beat_schedule import beat_schedule


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
    beat_schedule=beat_schedule,
    timezone="UTC",
)
