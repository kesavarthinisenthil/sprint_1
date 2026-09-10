import csv
import json
import pickle
from pathlib import Path
from typing import Any
from src.exceptions import InvalidFileException
from src.logger import LoggerManager

class DataWriter:
    """Write data to different file formats"""

    def write(self, file_path: str, data: Any)->Path:
        """Write data to CSV, JSON, Pickle, or TXT format"""
        logger = LoggerManager.get_logger()
        logger.info(f"Writing file: {file_path}")
        path = Path(file_path)
        file_extension = path.suffix.lower()
        if file_extension not in [".csv", ".json", ".pkl", ".txt"]:
            raise InvalidFileException(f"Unsupported file format: {file_extension}")
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            if file_extension == ".json":
                with open(path, "w", encoding="utf-8") as file:
                    json.dump(data, file, indent=4)

            if file_extension == ".txt":
                with open(path, "w", encoding="utf-8") as file:
                    file.write(str(data))

            if file_extension == ".pkl":
                with open(path, "wb") as file:
                    pickle.dump(data, file)

            if file_extension == ".csv":
                with open(path, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)

            logger.info(f"File written successfully: {file_path}")
            return path

        except OSError as error:
            logger.error(f"Error writing file: {file_path} - {error}")
            raise

        finally:
            logger.info("DataWriter operation completed.")