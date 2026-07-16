import storage
import input_handler
import date_utils
import presentation
import sys
import records

STORAGE_LOCATION = "data/records.json"

FEATURES = {1: "Add Record", 2: "View Record", 3: "Exit"}


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

    user_entries = input_handler.collect_user_entries()
    record = records.create_record(user_entries)
    stored_records = storage.load_records(STORAGE_LOCATION)

    if storage.has_record_for_date(stored_records, record["date"]):
        print("Record already exists for today's date!")
        return

    stored_records.append(record)
    storage.save_records(stored_records, STORAGE_LOCATION)
    print("Your record has been saved successfully.")


def view_record() -> None:
    """
    Display an overview of the user record.
    """

    day, month, year = input_handler.get_date_attributes_from_user()
    target_date = date_utils.build_date(day, month, year)
    stored_records = storage.load_records(STORAGE_LOCATION)
    record = storage.get_record_by_date(stored_records, target_date)

    if not record:
        print("No record found for the given date!")
        return

    presentation.present_record(record)


def main() -> None:

    actions = {1: add_record, 2: view_record, 3: sys.exit}

    storage.ensure_records_file_exists(STORAGE_LOCATION)
    display_menu()
    user_choice = input_handler.get_user_choice(FEATURES)
    actions[user_choice]()


if __name__ == "__main__":
    main()
