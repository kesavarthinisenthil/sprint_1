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

from src.loader import DataLoader
from src.writer import DataWriter


loader = DataLoader()
writer = DataWriter()

data = loader.load("data/sample.json")
writer.write("outputs/result.json", data)

print("Data processing completed.")