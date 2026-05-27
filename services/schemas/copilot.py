from pydantic import BaseModel


class ExecutiveBriefing(BaseModel):
    summary: str
    main_bottleneck: str
    highest_leverage_focus: str
    elimination_target: str
    execution_recommendation: str
