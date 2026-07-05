import os
import json


def ensure_records_file_exists(storage_location: str) -> None:
    """
    Ensure the records file to exist for storing record.
    """

    storage_directory = os.path.dirname(storage_location)

    if not os.path.exists(storage_directory):
        os.mkdir(storage_directory)

    if not os.path.exists(storage_location):

        with open(storage_location, "w") as file:
            json.dump([], file)


def load_records(storage_location: str) -> list[dict]:
    """
    Return saved JSON records.
    """

    with open(storage_location, "r") as file:
        saved_records = json.load(file)

    return saved_records


def save_records(modified_records: list[dict], storage_location: str) -> None:
    """
    Append the newly added record in the records file.
    """

    with open(storage_location, "w") as file:
        json.dump(modified_records, file, indent=4)
