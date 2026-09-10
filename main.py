# from src.loader import DataLoader

# loader = DataLoader()

# data = loader.load("data/sample.txt")

# print(data)

# from src.logger import LoggerManager


# logger = LoggerManager.get_logger()

# logger.info("Application started")
# logger.warning("This is a warning")
# logger.error("This is an error")

# print("Logging test completed")

# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# writer.write("outputs/test.json", data)

# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# writer.write("outputs/test.csv", data)

# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# writer.write("outputs/test.txt", data)

# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# writer.write("outputs/test.pkl", data)


# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# writer.write("outputs/test.json", data)

# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# writer.write("outputs/test.pdf", data)


# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# output_path = writer.write("outputs/test.json", data)

# print(output_path)

# from src.writer import DataWriter


# writer = DataWriter()

# data = [
#     {"Name": "Kesavarthini", "Age": 22, "City": "Coimbatore"},
#     {"Name": "Arun", "Age": 23, "City": "Chennai"}
# ]

# json_path = writer.write("outputs/test.json", data)
# csv_path = writer.write("outputs/test.csv", data)
# txt_path = writer.write("outputs/test.txt", data)
# pickle_path = writer.write("outputs/test.pkl", data)

# print(json_path)
# print(csv_path)
# print(txt_path)
# print(pickle_path)

# from src.loader import DataLoader
# from src.writer import DataWriter


# loader = DataLoader()
# writer = DataWriter()

# data = loader.load("data/sample.json")
# writer.write("outputs/result.json", data)

# print("Data processing completed.")

from src.database import DatabaseConnector


# db = DatabaseConnector(
#     host="localhost",
#     user="root",
#     password="Akalya@2004",
#     database="sprint1_db"
# )

# connection = db.connect()

# print("Database connected successfully.")

# db.close(connection)

# from src.config import ConfigManager


# config = ConfigManager()

# config.set("database", "sprint1_db")

# print(config.get("database"))


# from src.database import DatabaseConnector


# db = DatabaseConnector(
#     host="localhost",
#     user="root",
#     password="Akalya@2004",
#     database="sprint1_db"
# )

# connection = db.connect()

# print("Database connected successfully.")

# db.close(connection)


# from src.config import ConfigManager


# config = ConfigManager()

# config.set("host", "localhost")
# config.set("database", "sprint1_db")

# print(config.get_config())

# from src.config import ConfigManager


# config = ConfigManager()

# config.set("host", "localhost")
# config.set("database", "sprint1_db")

# print(config.configuration)

# from src.config import ConfigManager


# config = ConfigManager.create_default()

# print(config.configuration)

# from src.config import BaseConfig, ConfigManager


# config = ConfigManager()

# print(isinstance(config, BaseConfig))

# from src.config import ConfigManager

# config = ConfigManager()

# config.set("database", "sprint1_db")

# print(config.get("database"))
# print(config.configuration)


# from src.utils import (
#     get_timestamp,
#     validate_file,
#     validate_path,
#     get_logger,
#     read_config_value,
#     measure_execution_time
# )


# # 1. Test timestamp
# print("Timestamp:", get_timestamp())


# # 2. Test file validation
# print("File exists:", validate_file("data/sample.csv"))


# # 3. Test path validation
# print("Path exists:", validate_path("data/sample.csv"))


# # 4. Test logger helper
# logger = get_logger()
# logger.info("Utility functions tested successfully.")
# print("Logger test completed.")


# # 5. Test configuration reader
# config = {
#     "host": "localhost",
#     "database": "sprint1_db"
# }

# print("Database:", read_config_value(config, "database"))


# # 6. Test execution time decorator
# @measure_execution_time
# def test_function():
#     total = 0

#     for number in range(100000):
#         total += number

#     return total


# result = test_function()

# print("Function result:", result)
# print("Execution time test completed.")


# from src.database import DatabaseConnector
# from src.exceptions import DatabaseConnectionException


# db = DatabaseConnector(
#     host="localhost",
#     user="root",
#     password="Akalya@2004",
#     database="sprint1_db"
# )

# try:
#     connection = db.connect()
#     print("Database connected successfully.")

#     db.close(connection)
#     print("Database connection closed.")

# except DatabaseConnectionException as error:
#     print("Database error:", error)


from src.database import DatabaseConnector
from src.exceptions import DatabaseConnectionException
from src.loader import DataLoader
from src.writer import DataWriter
from src.utils import get_timestamp


def main():
    """Run the Sprint 1 application."""

    print("Sprint 1 Application")
    print("Timestamp:", get_timestamp())

    # Data loading
    loader = DataLoader()
    data = loader.load("data/sample.json")
    print("Data loaded successfully.")

    # Data writing
    writer = DataWriter()
    writer.write("outputs/result.json", data)
    print("Data written successfully.")

    # Database connection
    db = DatabaseConnector(
        host="localhost",
        user="root",
        password="Akalya@2004",
        database="sprint1_db"
    )

    try:
        connection = db.connect()
        print("Database connected successfully.")

        db.close(connection)
        print("Database connection closed.")

    except DatabaseConnectionException as error:
        print("Database error:", error)

    print("Application completed successfully.")


if __name__ == "__main__":
    main()