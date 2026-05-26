from services.worker.celery_app import celery_app


@celery_app.task(name="services.worker.tasks.ping")
def ping() -> str:
    return "pong"
