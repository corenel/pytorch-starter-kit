"""Custom logger with color."""

import logging
import logging.handlers
import os
from datetime import datetime

import config as cfg
from color_streamhandler import ColorStreamHandler

# init logger
_logger = logging.getLogger(cfg.project_name)
_logger.setLevel(logging.INFO)

# init log folder
log_file = "{}.log".format(datetime.now().strftime('%Y%m%d%H%M%S'))
log_path = os.path.join(cfg.log_root, log_file)
if (not os.path.exists(os.path.dirname(log_path))):
    os.makedirs(os.path.dirname(log_path))

# init log handlers
file_handler = logging.FileHandler(log_path)
console_handler = ColorStreamHandler()

# init log formatter
formatter = logging.Formatter("%(message)s")
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

_logger.addHandler(file_handler)
_logger.addHandler(console_handler)

level_dict = {
    "debug": logging.INFO,
    "info": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


def debug(*args, **kwargs):
    """DEBUG loglevel."""
    _logger.debug(*args, **kwargs)


def info(*args, **kwargs):
    """INFO loglevel."""
    _logger.info(*args, **kwargs)


def warning(*args, **kwargs):
    """WARNING loglevel."""
    _logger.warning(*args, **kwargs)


def error(*args, **kwargs):
    """ERROR loglevel."""
    _logger.error(*args, **kwargs)


def critical(*args, **kwargs):
    """CRITICAL loglevel."""
    _logger.critical(*args, **kwargs)


def set_level(level):
    """Set log level."""
    if level in level_dict:
        _logger.setLevel(level_dict[level])
    else:
        error("level name error")
