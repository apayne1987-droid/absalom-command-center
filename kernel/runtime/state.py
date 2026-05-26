from enum import StrEnum


class RuntimeState(StrEnum):
    CREATED = "CREATED"
    READY = "READY"
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"


CURRENT_RUNTIME_STATE = RuntimeState.ACTIVE
