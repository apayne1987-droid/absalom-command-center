from services.observability.logger import logger


def validate_execution(result: str) -> bool:

    if not result:
        logger.error("Validation failed: empty result")
        return False

    logger.info("Validation passed")

    return True
