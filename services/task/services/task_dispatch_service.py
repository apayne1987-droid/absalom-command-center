from services.worker.tasks import execute_runtime_task


class TaskDispatchService:
    def dispatch_task(self, task_id: int):
        return execute_runtime_task.delay(task_id)
