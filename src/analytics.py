from src.models import Record
import src.features_info as features_info
import pandas as pd


def generate_summary(stored_records: list[Record]) -> dict[str, int | float] | None:
    """
    Return a summary of records.
    """

    if not stored_records:
        return None

    summary_data = {
        "total_records": get_number_of_records(stored_records),
        "avg_study_hours": get_average_for_a_day(stored_records, "study_hours"),
        "avg_workout_minutes": get_average_for_a_day(stored_records, "workout_minutes"),
        "avg_mood": get_average_for_a_day(stored_records, "mood"),
        "avg_expense": get_average_for_a_day(stored_records, "expense"),
    }

    return summary_data


def get_number_of_records(stored_records: list[Record]) -> int:
    """
    Return the number of records saved by the user.
    """

    return len(stored_records)


def get_average_for_a_day(
    stored_records: list[Record], field_name: str
) -> float | None:
    """
    Return the average for a day of the given field.
    """

    if not stored_records:
        return None

    total = 0

    for record in stored_records:
        total += record[field_name]

    return round(total / len(stored_records), 2)


def get_highest_val_and_corresponding_dates(
    stored_records: list[Record],
) -> dict[str, dict[int | float, list[str]]] | None:
    """
    Return the highest value for a specific field with its corresponding dates.
    """

    if not stored_records:
        return None

    records_df = pd.DataFrame(stored_records)
    highest_val_and_dates_data = {}

    for field in features_info.REQUIRED_FIELDS:
        highest_val = records_df[field].max()

        # find corresponding dates
        matching_rows = records_df[records_df[field] == highest_val]
        corresponding_dates = matching_rows["date"].tolist()

        highest_val_and_dates_data[field] = {highest_val: corresponding_dates}

    return highest_val_and_dates_data
