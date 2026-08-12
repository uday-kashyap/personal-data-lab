import src.features_info as features_info


def collect_user_entries() -> dict[str, int | float]:
    """
    Collect required fields from the user and return them.
    """

    user_entries = {}

    for field in features_info.REQUIRED_FIELDS:
        cleaned_field = field.replace("_", " ")

        while True:

            try:
                field_val = features_info.FIELD_TYPES[field](
                    input(f"Enter your {cleaned_field} for today: ")
                )

                # Verify range
                min_range_val, max_range_val = features_info.FIELD_RANGES[field]

                if not (min_range_val <= field_val <= max_range_val):
                    print(
                        f"Input must be on the scale ({min_range_val}-{max_range_val})!"
                    )
                    continue

                user_entries[field] = field_val
                break

            except ValueError:
                print(f'Please enter valid numeric value for "{cleaned_field}"!')
                continue

    return user_entries


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
