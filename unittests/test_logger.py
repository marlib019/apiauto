import logging
import unittest

# from api.projects import LOGGER
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestLogger(unittest.TestCase):
    def test_logger(self):
        LOGGER.debug("log debug level")
        LOGGER.info("log info level")
        LOGGER.warning("log warning level")
        LOGGER.error("log error level")
        LOGGER.critical("log critical level")
