from datetime import datetime, UTC

from fastapi import FastAPI

from kernel.runtime.state import CURRENT_RUNTIME_STATE
from services.config.settings import settings
from services.telemetry.logger import log_event


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/health")
async def health():
    log_event("health.checked", runtime_state=CURRENT_RUNTIME_STATE)

    return {
        "status": "ok",
        "runtime": CURRENT_RUNTIME_STATE,
        "timestamp": datetime.now(UTC).isoformat(),
    }


@app.get("/runtime/status")
async def runtime_status():
    log_event("runtime.status.checked", runtime_state=CURRENT_RUNTIME_STATE)

    return {
        "runtime_state": CURRENT_RUNTIME_STATE,
        "platform": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment,
    }
