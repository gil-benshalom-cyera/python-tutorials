import logging
import random
from utils.general import init_basic_logger


# 1️⃣ Logging Exceptions (Previously @log_exceptions)
def divide(a, b):
    """Performs division and logs exceptions manually."""
    try:
        return a / b
    except Exception as e:
        logging.warning(f"Exception in divide(): {e}")
        return None


def log_exception():
    """Calls divide() and handles exceptions manually."""
    print(divide(10, 2))  # ✅ Expected output: 5.0
    print(divide(10, 0))  # ❌ Logs warning, returns None


# 2️⃣ Retry Logic (Previously @retry)
def retry_unstable_function(max_attempts=5, delay=2):
    """Retries unstable_function() up to max_attempts times."""
    for attempt in range(max_attempts):
        try:
            if random.random() < 0.7:  # 70% chance of failure
                raise ValueError("Random failure")
            return "Success!"
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_attempts - 1:
                import time
                time.sleep(delay)  # Wait before retrying
    print(f"All {max_attempts} attempts failed.")
    return None


# 3️⃣ Caching Function Output (Previously @save_to_dict)
cache = {}


def fetch_data(key):
    """Simulates fetching data and manually storing in cache."""
    result = {"data": f"Value for {key}"}
    cache[key] = result  # Manually storing result in cache
    return result


def main():
    print("\n🔹 Exception Logging Example")
    log_exception()  # ✅ Demonstrates manual exception logging

    print("\n🔹 Retry Example")
    print(retry_unstable_function())  # ✅ Demonstrates manual retry logic

    print("\n🔹 Caching Example")
    """Manually stores function output in a dictionary."""
    fetch_data("user1")
    fetch_data("user2")
    print(cache)  # ✅ {'user1': {'data': 'Value for user1'}, 'user2': {'data': 'Value for user2'}}


# 🎯 Running the Script
if __name__ == '__main__':
    init_basic_logger()
    main()  # ✅ Demonstrates manual caching
