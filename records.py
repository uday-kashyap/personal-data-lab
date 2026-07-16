from models import Record
import date_utils
from typing import cast


def create_record(user_entries: dict[str, int | float]) -> Record:
    """
    Return a complete record with all the required fields.
    """

    record = {}
    current_date = date_utils.get_current_date()
    record["date"] = current_date
    record.update(user_entries)
    return cast(Record, record)
