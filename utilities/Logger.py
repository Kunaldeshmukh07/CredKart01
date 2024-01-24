import logging

class Logging_class:
    @staticmethod
    def log_generator():
        logger = logging.getLogger(__name__)
        logfile = logging.FileHandler("C:\\Users\\KUNAL\\Desktop\\CT#10\\NEW REVISION 2023\\Scripts\\PytestFramework\\Logs\\Credkart_logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s ")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.DEBUG)
        return logger