from datetime import datetime
from pathlib import Path
from typing import Any, Callable
import time
from functools import wraps
from src.logger import LoggerManager


def get_timestamp() -> str:
    """Return the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def validate_file(file_path: str) -> bool:
    """Check whether the given path exists and is a file."""
    path = Path(file_path)

    if not path.exists():
        return False

    return path.is_file()


def validate_path(file_path: str) -> bool:
    """Check whether the given path exists."""
    return Path(file_path).exists()


def get_logger():
    """Return the application logger."""
    return LoggerManager.get_logger()


def read_config_value(config: dict, key: str) -> Any:
    """Read a value from a configuration dictionary."""
    return config.get(key)


def measure_execution_time(func: Callable) -> Callable:
    """Measure and log the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        logger = LoggerManager.get_logger()
        logger.info(
            f"{func.__name__} executed in {execution_time:.4f} seconds"
        )

        return result

    return wrapper