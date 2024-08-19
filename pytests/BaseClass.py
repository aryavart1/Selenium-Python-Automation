import inspect
import logging


class BaseClass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # captures file name during runtime by default prints root

        # Specified file name will be created and all the logs will be directed in it
        file_handler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        file_handler.setFormatter(formatter)

        # Will take format and the location of file
        logger.addHandler(file_handler)  # filehandler object

        # Logs before INFO will not be printed, all the logs after it will be shown in the log file
        logger.setLevel(logging.INFO)

        return logger
