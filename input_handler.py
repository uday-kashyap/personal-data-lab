REQUIRED_FIELDS = ("study_hours", "workout_minutes", "expense", "mood")
FIELD_TYPES = {
    "study_hours": float,
    "workout_minutes": int,
    "expense": float,
    "mood": int,
}


def collect_record() -> dict[str, int | float]:
    """
    Collect a record from the user and return it with values converted to their expected Python types.
    """

    raw_record = {}

    for field in REQUIRED_FIELDS:
        clean_field = field.replace("_", " ")
        field_val = input(f"Enter your {clean_field} for today: ")
        raw_record[field] = field_val

    record = _convert_record_types(raw_record)
    return record


def _convert_record_types(target_record: dict[str, str]) -> dict[str, int | float]:
    """
    Return a new record with values converted to their expected Python types.
    """

    modified_record = {}

    for field, field_val in target_record.items():
        modified_record[field] = FIELD_TYPES[field](field_val)

    return modified_record
