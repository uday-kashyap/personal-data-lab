from src.models import Record


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
