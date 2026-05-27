from services.schemas.runtime_trace import RuntimeTrace


runtime_traces: list[RuntimeTrace] = []


def add_runtime_trace(trace: RuntimeTrace) -> None:
    runtime_traces.append(trace)


def get_runtime_traces() -> list[RuntimeTrace]:
    return runtime_traces[-25:]
