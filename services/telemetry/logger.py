import structlog


logger = structlog.get_logger("absalom-command-center")


def log_event(event: str, **kwargs):
    logger.info(event, **kwargs)
