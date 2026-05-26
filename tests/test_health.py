from fastapi.testclient import TestClient

from apps.api.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"


def test_runtime_status():
    response = client.get("/runtime/status")

    assert response.status_code == 200

    data = response.json()

    assert data["runtime_state"] == "ACTIVE"
