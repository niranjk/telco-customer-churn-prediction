#logger are used to record events that happen during the execution of a program.
# This module sets up logging configurations and provides functions to log messages at various severity levels (info, debug, warning, error, critical).

import logging
import os
from datetime import datetime

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)   
LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    logging.info("Logger has been set up.")
    logging.debug("This is a debug message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")