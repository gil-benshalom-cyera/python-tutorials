import time
import logging
from functools import wraps
from utils.general import init_basic_logger

logger = logging.getLogger(__name__)


def log_exceptions(func):
    """Decorator to catch and log exceptions as warnings instead of crashing."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"Exception in {func.__name__}: {e}")
            return None  # You can return a default value if needed

    return wrapper


# 1. Timing Decorator
def time_it(func):
    """Decorator to measure execution time of a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result

    return wrapper


def save_to_dict(storage_dict):
    """Decorator to save function output to a dictionary using the first argument as the key."""

    def decorator(func):
        @wraps(func)
        def wrapper(key, *args, **kwargs):
            result = func(key, *args, **kwargs)  # Call original function
            if isinstance(result, dict):  # Ensure output is a dictionary
                storage_dict[key] = result
            return result

        return wrapper

    return decorator


def retry(max_attempts=3, delay=1):
    """Decorator to retry a function multiple times if it fails."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
            print(f"All {max_attempts} attempts failed.")
            return None

        return wrapper

    return decorator
