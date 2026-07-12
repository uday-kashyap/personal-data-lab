import storage
import input_handler
import sys

STORAGE_LOCATION = "data/records.json"

FEATURES = {1: "Add Record", 2: "Exit"}


def display_menu() -> None:
    """
    Display all the available features.
    """

    for option_no, feature in FEATURES.items():
        print(f"{option_no}. {feature}")


def add_record() -> None:
    """
    Add a user record to a valid JSON file.
    """

    record = input_handler.collect_record()
    stored_records = storage.load_records(STORAGE_LOCATION)

    if storage.has_record_for_date(stored_records, record["date"]):
        print("Record already exists for today's date!")
        sys.exit()

    stored_records.append(record)
    storage.save_records(stored_records, STORAGE_LOCATION)
    print("Your record has been saved successfully.")


def main() -> None:

    actions = {1: add_record, 2: sys.exit}

    storage.ensure_records_file_exists(STORAGE_LOCATION)
    display_menu()
    user_choice = input_handler.get_user_choice(FEATURES)
    actions[user_choice]()


if __name__ == "__main__":
    main()
