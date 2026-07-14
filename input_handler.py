import date_utils
from models import Record
from typing import cast

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


def collect_record() -> Record:
    """
    Collect a record from the user and return it.
    """

    record = {}

    # Embed current date in the record
    record["date"] = date_utils.get_current_date()

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

    return cast(Record, record)


def get_user_choice(features_dict: dict) -> int:
    """
    Ask user to choose valid option number for given dictionary of features and return it after validation.
    """

    while True:

        try:
            choice = int(input("Enter your choice: "))

            if choice not in features_dict:
                print("Please enter a valid option number!")
                continue

            return choice

        except ValueError:
            print("The option number must be an integer only!")


def get_date_attributes_from_user() -> tuple[int, int, int]:
    """
    Take day, month, year from the user and return them.
    """

    while True:

        try:
            day = int(input("Enter day: "))
            month = int(input("Enter month: "))
            year = int(input("Enter year: "))

            return day, month, year

        except ValueError:
            print("Please enter a valid input!")
