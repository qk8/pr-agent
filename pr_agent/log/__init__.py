from __future__ import annotations

import logging
import os
import sys
from enum import Enum
from typing import TYPE_CHECKING

from loguru import logger

from pr_agent.config_loader import get_settings

if TYPE_CHECKING:
    from loguru._logger import Logger



class LoggingFormat(str, Enum):
    CONSOLE = "CONSOLE"
    JSON = "JSON"


def json_format(record: dict[str, object]) -> str:
    return record["message"]  # type: ignore[return-value]


def analytics_filter(record: dict[str, object]) -> bool:
    return record.get("extra", {}).get("analytics", False)  # type: ignore[return-value]


def inv_analytics_filter(record: dict[str, object]) -> bool:
    return not record.get("extra", {}).get("analytics", False)  # type: ignore[return-value]


def setup_logger(level: str = "INFO", fmt: LoggingFormat = LoggingFormat.CONSOLE) -> "Logger":  # pyright: ignore
    level: int = logging.getLevelName(level.upper())  # pyright: ignore
    if type(level) is not int:
        level = logging.INFO

    if fmt == LoggingFormat.JSON and os.getenv("LOG_SANE", "0").lower() == "0":  # better debugging github_app
        logger.remove(None)
        logger.add(  # pyright: ignore
            sys.stdout,
            filter=inv_analytics_filter,  # pyright: ignore
            level=level,
            format="{message}",
            colorize=False,
            serialize=True,
        )
    elif fmt == LoggingFormat.CONSOLE:  # does not print the 'extra' fields
        logger.remove(None)
        logger.add(sys.stdout, level=level, colorize=True, filter=inv_analytics_filter)  # pyright: ignore

    log_folder: str = get_settings().get("CONFIG.ANALYTICS_FOLDER", "")  # type: ignore[union-attr]
    if log_folder:
        pid = os.getpid()
        log_file = os.path.join(log_folder, f"pr-agent.{pid}.log")
        logger.add(  # pyright: ignore
            log_file,
            filter=analytics_filter,  # pyright: ignore
            level=level,
            format="{message}",
            colorize=False,
            serialize=True,
        )

    return logger  # pyright: ignore


def get_logger(*args: object, **kwargs: object) -> "Logger":
    return logger  # type: ignore[return-value]
