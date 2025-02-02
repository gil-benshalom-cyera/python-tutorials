import logging
from utils.general import init_complex_logger
from logger_usage.logger_disabled import log_all_levels


logger = logging.getLogger(__name__)


def main():
    logger.debug("This is an debug message")
    logger.info("This is an info message")
    log_all_levels()


if __name__ == '__main__':
    init_complex_logger()
    main()
