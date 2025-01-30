import random
from utils.decorators import retry


# Example Usage
@retry(max_attempts=5, delay=2)
def unstable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure")
    return "Success!"


if __name__ == '__main__':
    print(unstable_function())
