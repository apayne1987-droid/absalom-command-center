from services.worker.celery_app import celery_app


@celery_app.task(name="services.worker.tasks.ping")
def ping() -> str:
    return "pong"


@celery_app.task(name="services.worker.tasks.execute_runtime_task")
def execute_runtime_task(task_id: int) -> dict[str, int | str]:
    return {
        "task_id": task_id,
        "status": "completed",
        "message": f"Task {task_id} executed successfully",
    }
