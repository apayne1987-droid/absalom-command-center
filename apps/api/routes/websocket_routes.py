from datetime import UTC, datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect


router = APIRouter(prefix="/ws", tags=["websocket"])


@router.websocket("/runtime")
async def runtime_websocket(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            await websocket.send_json(
                {
                    "event": "runtime_heartbeat",
                    "status": "online",
                    "timestamp": datetime.now(UTC).isoformat(),
                }
            )

            await websocket.receive_text()

    except WebSocketDisconnect:
        return
