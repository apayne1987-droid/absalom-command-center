import asyncio

from services.database.session import SessionLocal
from services.execution.services.execution_log_service import ExecutionLogService
from services.task.repositories.task_repository import TaskRepository
from services.worker.celery_app import celery_app
from services.workflow.services.workflow_service import WorkflowService


@celery_app.task(name="services.worker.tasks.ping")
def ping() -> str:
    return "pong"


@celery_app.task(
    name="services.worker.tasks.execute_runtime_task",
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def execute_runtime_task(self, task_id: int) -> dict[str, int | str]:
    try:
        asyncio.run(run_execution_lifecycle(task_id))

        return {
            "task_id": task_id,
            "status": "completed",
            "message": f"Task {task_id} executed successfully",
        }

    except Exception as exc:
        asyncio.run(mark_execution_failed(task_id, str(exc)))
        raise


async def run_execution_lifecycle(task_id: int) -> None:
    async with SessionLocal() as session:
        task_repository = TaskRepository(session)
        execution_log_service = ExecutionLogService(session)
        workflow_service = WorkflowService(session)

        task = await task_repository.get_by_id(task_id)

        if task is None:
            raise ValueError(f"Task not found: {task_id}")

        await task_repository.update_state(task, "ACTIVE")

        await execution_log_service.create_system_log(
            task_id=task.id,
            event_type="task.execution_started",
            message=f"Task {task.id} execution started",
        )

        await asyncio.sleep(2)

        task = await task_repository.get_by_id(task_id)

        if task is None:
            raise ValueError(f"Task not found during execution: {task_id}")

        await task_repository.update_state(task, "COMPLETED")

        await execution_log_service.create_system_log(
            task_id=task.id,
            event_type="task.execution_completed",
            message=f"Task {task.id} execution completed",
        )

        await workflow_service.recalculate_workflow_state(task.workflow_id)


async def mark_execution_failed(task_id: int, error_message: str) -> None:
    async with SessionLocal() as session:
        task_repository = TaskRepository(session)
        execution_log_service = ExecutionLogService(session)
        workflow_service = WorkflowService(session)

        task = await task_repository.get_by_id(task_id)

        if task is None:
            return

        await task_repository.update_state(task, "FAILED")

        await execution_log_service.create_system_log(
            task_id=task.id,
            event_type="task.execution_failed",
            message=error_message,
        )

        await workflow_service.recalculate_workflow_state(task.workflow_id)
