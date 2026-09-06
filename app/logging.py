import logging
from logging.config import dictConfig
from typing import Any


def build_logging_config(level: str = "INFO") -> dict[str, Any]:
    """Return a dictConfig-compatible logging configuration."""
    log_level = level.upper()
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "default": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {
            "level": log_level,
            "handlers": ["default"],
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["default"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn.error": {
                "handlers": ["default"],
                "level": log_level,
                "propagate": False,
            },
            "uvicorn.access": {
                "handlers": ["default"],
                "level": log_level,
                "propagate": False,
            },
            "arima": {
                "handlers": ["default"],
                "level": log_level,
                "propagate": False,
            },
        },
    }


def setup_logging(level: str = "INFO") -> dict[str, Any]:
    """Configure application and uvicorn loggers. Returns the config used."""
    config = build_logging_config(level)
    dictConfig(config)
    return config


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a logger under the ``arima`` namespace."""
    if not name:
        return logging.getLogger("arima")
    if name.startswith("arima."):
        return logging.getLogger(name)
    return logging.getLogger(f"arima.{name}")
