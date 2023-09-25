"""
(c) Copyright Jalasoft. 2023

logger.py
    configuration of logger file
"""
import logging
import os.path
import pathlib
import sys
from datetime import datetime
from logging import handlers

DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(asctime)s UTC %(levelname)-15s  %(name) %(message)s"


def get_logger(name, level=DEFAULT_LOG_LEVEL, log_format=DEFAULT_LOG_FORMAT):
    """
    Configure logging instance
    :param name:
    :param level:
    :param log_format:
    :return:
    """
    logger = logging.getLogger(name)
    logg_file_name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

    for handler in logger.handlers:
        logger.removeHandler(handler)
    handler = logging.StreamHandler(sys.__stdout__)
    handler.setLevel(level)

    abs_path = os.path.abspath(__file__ + "../../../")
    # print("Path absoluto" + abs_path)

    # crea el folder en caso de que no exista
    pathlib.Path(f"{abs_path}/logs").mkdir(parents=True, exist_ok=True)

    handler_file = handlers.RotatingFileHandler(f"{abs_path}/logs/{logg_file_name}.log",
                                                maxBytes=1000000,
                                                backupCount=5)
    handler_file.setLevel(level)

    fmt = logging.Formatter(log_format)
    handler.setFormatter(fmt)
    handler_file.setFormatter(fmt)

    logger.addHandler(handler)
    logger.addHandler(handler_file)
    logger.propagate = False

    logger.setLevel(level)

    return logger
