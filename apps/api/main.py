from datetime import UTC, datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.api.routes.auth_routes import router as auth_router
from apps.api.routes.protected_routes import router as protected_router
from apps.api.routes.websocket_routes import router as websocket_router
from apps.api.routes.executive_routes import router as executive_router
from apps.api.routes.copilot_routes import router as copilot_router

from apps.api.routes.execution_log_routes import router as execution_log_router
from apps.api.routes.metrics_routes import router as metrics_router
from apps.api.routes.task_routes import router as task_router
from apps.api.routes.workflow_routes import router as workflow_router
from kernel.runtime.state import CURRENT_RUNTIME_STATE
from services.config.settings import settings
from services.database.session import check_database_connection
from services.telemetry.logger import log_event


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(protected_router)
app.include_router(websocket_router)
app.include_router(executive_router)
app.include_router(copilot_router)
app.include_router(workflow_router)
app.include_router(task_router)
app.include_router(execution_log_router)
app.include_router(metrics_router)


@app.get("/health")
async def health():
    database_connected = await check_database_connection()

    log_event(
        "health.checked",
        runtime_state=CURRENT_RUNTIME_STATE,
        database_connected=database_connected,
    )

    return {
        "status": "ok" if database_connected else "degraded",
        "runtime": CURRENT_RUNTIME_STATE,
        "database": "connected" if database_connected else "disconnected",
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





