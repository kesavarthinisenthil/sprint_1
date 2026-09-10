import mysql.connector
from mysql.connector import Error
from src.logger import LoggerManager
from src.exceptions import DatabaseConnectionException

class DatabaseConnector:
    """Manage database connections"""

    def __init__(self, host: str, user: str, password: str, database: str):
        """Initialize database connection details."""
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self) -> mysql.connector.MySQLConnection:
        """Establish a connection to the database."""

        logger = LoggerManager.get_logger()
        logger.info("Attempting to connect to the database.")
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
    )

            logger.info("Database connection established successfully.")
            return connection

        except Error as error:
            logger.error(f"Database connection failed: {error}")
            raise DatabaseConnectionException("Unable to connect to the database.") from error

    def close(self, connection: mysql.connector.MySQLConnection) -> None:
        """Close the database connection."""
        logger = LoggerManager.get_logger()
        connection.close()
        logger.info("Database connection closed.")