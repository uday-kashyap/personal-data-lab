REQUIRED_FIELDS = ("study_hours", "workout_minutes", "expense", "mood")
FIELD_TYPES = {
    "study_hours": float,
    "workout_minutes": int,
    "expense": float,
    "mood": int,
}


def collect_record() -> dict[str, int | float]:
    """
    Collect a record from the user and return it.
    """

    record = {}

    for field in REQUIRED_FIELDS:
        cleaned_field = field.replace("_", " ")

        while True:

            try:
                field_val = FIELD_TYPES[field](
                    input(f"Enter your {cleaned_field} for today: ")
                )
                record[field] = field_val
                break

            except ValueError:
                print(f'Please enter valid numeric value for "{cleaned_field}"!')
                continue

    return record
