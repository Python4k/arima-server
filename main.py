from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.db import engine
from app.logging import get_logger, setup_logging

logging_config = setup_logging(settings.LOG_LEVEL)
logger = get_logger("main")


@asynccontextmanager
async def lifespan(_app: FastAPI):
    logger.info("Starting ARIMA Server (log_level=%s)", settings.LOG_LEVEL)
    yield
    logger.info("Stopping ARIMA Server")
    await engine.dispose()
    logger.info("Shutting down ARIMA Server")


app = FastAPI(
    title="ARIMA Server",
    description="Main API for ARIMA project",
    debug=settings.LOG_LEVEL == "DEBUG",
    lifespan=lifespan,
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.LOG_LEVEL == "DEBUG",
        log_config=logging_config,
    )
