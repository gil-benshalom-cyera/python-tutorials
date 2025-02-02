from utils.decorators import log_exceptions
from utils.general import init_basic_logger


@log_exceptions
def divide(a, b):
    return a / b


def log_exception():
    print(divide(10, 2))  # 5.0
    print(divide(10, 0))  # Logs warning, returns None


if __name__ == '__main__':
    init_basic_logger()
    log_exception()
