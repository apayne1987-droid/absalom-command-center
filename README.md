# ABSALOM COMMAND CENTER™

Canonical enterprise platform architecture v14.0.

## Current Status

Foundational execution spine is active.

## Current Capabilities

- FastAPI runtime
- Health endpoint
- Runtime status endpoint
- Runtime state model
- Config service
- Structured telemetry
- Automated tests
- Ruff linting
- MyPy type checks
- Docker foundation

## Local Development

Create virtual environment:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r apps\api\requirements.txt

Run API:

uvicorn apps.api.main:app --reload

Test:

pytest
ruff check .
mypy .

Docker:

docker compose up --build
