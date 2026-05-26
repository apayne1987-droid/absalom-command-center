from celery.schedules import crontab


beat_schedule = {
    "runtime-health-check": {
        "task": "services.worker.tasks.ping",
        "schedule": crontab(minute="*/1"),
    },
}
