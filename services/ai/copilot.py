from services.schemas.copilot import ExecutiveBriefing


async def generate_executive_briefing() -> ExecutiveBriefing:
    return ExecutiveBriefing(
        summary=(
            "Current operational momentum is strong. "
            "Infrastructure stability has significantly improved. "
            "The highest priority is now product differentiation and "
            "execution compression."
        ),

        main_bottleneck=(
            "Too much engineering attention is still being allocated "
            "toward infrastructure instead of product wedge expansion."
        ),

        highest_leverage_focus=(
            "Build structured AI operational intelligence systems "
            "that reduce executive cognitive load."
        ),

        elimination_target=(
            "Avoid premature multi-agent complexity and unnecessary "
            "dashboard expansion."
        ),

        execution_recommendation=(
            "Prioritize shipping the operational intelligence loop "
            "before advanced orchestration systems."
        ),
    )
