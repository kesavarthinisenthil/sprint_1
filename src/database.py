import mysql.connector

class DatabaseConnector:
    """Manage database connections"""

    def __init__(self, host: str, user: str, password: str, database: str):
        """Initialize database connection details."""

        self.host = host
        self.user = user
        self.password = password
        self.database = database