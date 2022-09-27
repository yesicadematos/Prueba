from config import LOGS_PATH
import logging

from utils import create_folder




def create_logger(name_logger, log_path):
    """Create log file.
    Args:
        name_logger (str): Name log.
        log_path (str): Path to save the log file.
    Returns:
        Logger with custom configuration.
    """
    # Create logger folder.
    create_folder(LOGS_PATH)
    # Create logger and set name.
    logger = logging.getLogger(name_logger)
    # Set log level.
    logger.setLevel(logging.INFO)
    # Create formatter.
    formatter = logging.Formatter(
        # %Y-%m-%d - nombre_logger - mensaje
        fmt='%(asctime)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d')

    # Stream Handler (for console)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File Handler (for .log)
    fh = logging.FileHandler(
        filename="{0}/{1}.log".format(log_path, name_logger),
        mode='a')  # 'a' continue, 'w' truncate.
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger