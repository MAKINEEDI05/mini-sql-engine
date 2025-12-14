import csv

def load_csv(file_path):
    """
    Load a CSV file into memory as a list of dictionaries.
    Each row is represented as a dictionary.
    """
    try:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise Exception(f"CSV file not found: {file_path}")
