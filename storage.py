import os
import json
from models import Record


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


def load_records(storage_location: str) -> list[Record]:
    """
    Return saved JSON records.
    """

    with open(storage_location, "r") as file:
        saved_records = json.load(file)

    return saved_records


def save_records(modified_records: list[Record], storage_location: str) -> None:
    """
    Append the newly added record in the records file.
    """

    with open(storage_location, "w") as file:
        json.dump(modified_records, file, indent=4)


def has_record_for_date(stored_records: list[Record], target_date: str) -> bool:
    """
    Return True if a record with target date already exists in records. Otherwise, return False.
    """

    record_idx = _get_record_index_by_date(stored_records, target_date)
    return record_idx != -1


def get_record_by_date(stored_records: list[Record], target_date: str) -> Record | None:
    """
    Fetch record of a specific date and return it.
    """

    record_idx = _get_record_index_by_date(stored_records, target_date)

    if record_idx == -1:
        return None

    return stored_records[record_idx]


def _get_record_index_by_date(stored_records: list[Record], target_date: str) -> int:
    """
    Find a record with specific date and return its index.
    """

    for record_idx in range(len(stored_records)):

        if stored_records[record_idx]["date"] == target_date:
            return record_idx

    return -1


def get_updated_records(
    stored_records: list[Record], target_date: str, new_entries: dict[str, int | float]
) -> list[Record]:
    """
    Update the existing user record with the new entries and return the updated list of records.
    """

    record_idx = _get_record_index_by_date(stored_records, target_date)

    for field, new_entry in new_entries.items():
        stored_records[record_idx][field] = new_entry

    return stored_records
