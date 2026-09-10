import logging

class LoggerManager:
    """Manage application logging."""

    @staticmethod
    def get_logger():
        """Create and return the application logger."""

        logging.basicConfig(
            filename="logs/application.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger("application")