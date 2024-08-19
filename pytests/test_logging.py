""" Building reusable Utility for Logging to inject into framework """

import logging
def test_logging():
    logger = logging.getLogger(__name__)  # captures file name during runtime by default prints root

    # Specified file name will be created and all the logs will be directed in it
    file_handler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

    file_handler.setFormatter(format)

    # Will take format and the location of file
    logger.addHandler(file_handler)  # filehandler object

    # Logs before INFO will not be printed, all the logs after it will be shown in the log file
    logger.setLevel(logging.INFO)


    logger.debug("A debug statement is executed") # Instead of console will print in a file
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("An error occurred")
    logger.critical("Fatal error occurred")