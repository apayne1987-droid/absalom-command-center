from services.schemas.priority import PriorityItem


def calculate_priority_score(
    roi_score: int,
    leverage_score: int,
    automation_score: int,
    strategic_alignment_score: int,
    difficulty_score: int,
) -> int:

    return (
        roi_score
        + leverage_score
        + automation_score
        + strategic_alignment_score
        - difficulty_score
    )


def get_priority_items() -> list[PriorityItem]:

    raw_items = [
        {
            "title": "Build operational memory layer",
            "roi_score": 9,
            "leverage_score": 10,
            "automation_score": 8,
            "strategic_alignment_score": 10,
            "difficulty_score": 6,
        },

        {
            "title": "Expand infrastructure monitoring",
            "roi_score": 5,
            "leverage_score": 5,
            "automation_score": 4,
            "strategic_alignment_score": 5,
            "difficulty_score": 4,
        },

        {
            "title": "Build weekly executive review engine",
            "roi_score": 9,
            "leverage_score": 9,
            "automation_score": 7,
            "strategic_alignment_score": 10,
            "difficulty_score": 5,
        },

        {
            "title": "Premature multi-agent orchestration",
            "roi_score": 3,
            "leverage_score": 4,
            "automation_score": 6,
            "strategic_alignment_score": 2,
            "difficulty_score": 9,
        },
    ]

    results = []

    for item in raw_items:

        priority_score = calculate_priority_score(
            item["roi_score"],
            item["leverage_score"],
            item["automation_score"],
            item["strategic_alignment_score"],
            item["difficulty_score"],
        )

        results.append(
            PriorityItem(
                title=item["title"],
                roi_score=item["roi_score"],
                leverage_score=item["leverage_score"],
                automation_score=item["automation_score"],
                strategic_alignment_score=item["strategic_alignment_score"],
                difficulty_score=item["difficulty_score"],
                priority_score=priority_score,
            )
        )

    results.sort(
        key=lambda x: x.priority_score,
        reverse=True,
    )

    return results
