from services.worker.tasks import execute_runtime_task


class TaskDispatchService:
    def dispatch_task(self, task_id: int):
        return execute_runtime_task.apply_async(
            args=[task_id],
            retry=True,
            retry_policy={
                "max_retries": 3,
                "interval_start": 1,
                "interval_step": 2,
                "interval_max": 10,
            },
        )
