import csv
import json
from pathlib import Path
from typing import Any
from src.exceptions import InvalidFileException
from src.logger import LoggerManager

class DataLoader:
    """Load data from CSV, JSON, and TXT files."""

    def __init__(self):
        """Initialize DataLoader with a logger."""
        self.logger = LoggerManager.get_logger()

    def load(self,file_path: str)-> Any:
        """Load data from the given path"""
        self.logger.info(f"Loading file: {file_path}")
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not path.is_file():
            raise InvalidFileException(f"Path is not a file: {file_path}")

        file_extension = path.suffix.lower()
        if file_extension not in [".csv",".json",".txt"]:
            raise InvalidFileException(f"Unsupported file format: {file_extension}")

        if file_extension == ".csv":
            try:
                with open(path, "r", newline="", encoding="utf-8") as file:
                    data = list(csv.DictReader(file))

                self.logger.info(f"File loaded successfully: {file_path}")
                return data

            except OSError as error:
                raise InvalidFileException(f"Unable to read file: {file_path}") from error

        if file_extension == ".json":
            try:
                with open(path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                self.logger.info(f"File loaded successfully: {file_path}")
                return data

            except (OSError, json.JSONDecodeError) as error:
                raise InvalidFileException(f"Unable to read JSON file: {file_path}") from error

        if file_extension == ".txt":
            try:
                with open(path, "r", encoding="utf-8") as file:
                    data = file.read()

                self.logger.info(f"File loaded successfully: {file_path}")
                return data

            except OSError as error:
                raise InvalidFileException(f"Unable to read text file: {file_path}") from error

        