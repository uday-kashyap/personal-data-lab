from datetime import date

REQUIRED_FIELDS = ("study_hours", "workout_minutes", "expense", "mood")

FIELD_TYPES = {
    "study_hours": float,
    "workout_minutes": int,
    "expense": float,
    "mood": int,
}

FIELD_RANGES = {
    "study_hours": (0, 24),
    "workout_minutes": (0, 1440),
    "expense": (0, float("inf")),
    "mood": (1, 10),
}


def collect_record() -> dict[str, int | float]:
    """
    Collect a record from the user and return it.
    """

    record = {}

    # Embed current date in the record
    record["date"] = _get_current_date()

    for field in REQUIRED_FIELDS:
        cleaned_field = field.replace("_", " ")

        while True:

            try:
                field_val = FIELD_TYPES[field](
                    input(f"Enter your {cleaned_field} for today: ")
                )

                # Verify range
                min_range_val, max_range_val = FIELD_RANGES[field]

                if not (min_range_val <= field_val <= max_range_val):
                    print(
                        f"Input must be on the scale ({min_range_val}-{max_range_val})!"
                    )
                    continue

                record[field] = field_val
                break

            except ValueError:
                print(f'Please enter valid numeric value for "{cleaned_field}"!')
                continue

    return record


def _get_current_date() -> str:
    """
    Return today's date in YYYY/MM/DD format.
    """

    today = date.today()
    formatted_date = today.strftime("%Y/%m/%d")
    return formatted_date
