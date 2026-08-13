import src.storage as storage
import src.input_handler as input_handler
import src.date_utils as date_utils
import src.presentation as presentation
import sys
import src.records as records
import src.analytics as analytics
import src.features_info as features_info

STORAGE_LOCATION = "data/records.json"


def add_record() -> None:
    """
    Add a user record to a valid JSON file.
    """

    user_entries = input_handler.collect_user_entries()
    print()
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
    print()
    target_date = date_utils.build_date(day, month, year)
    stored_records = storage.load_records(STORAGE_LOCATION)
    record = storage.get_record_by_date(stored_records, target_date)

    if not record:
        print("No record found for the given date!")
        return

    presentation.present_record(record)


def edit_record() -> None:
    """
    Edit the existing user record with the new entries.
    """

    day, month, year = input_handler.get_date_attributes_from_user()
    print()
    target_date = date_utils.build_date(day, month, year)
    stored_records = storage.load_records(STORAGE_LOCATION)

    if not storage.has_record_for_date(stored_records, target_date):
        print("No record found for the given date!")
        return

    print("Please enter your new entries below!")
    print()
    new_entries = input_handler.collect_user_entries()
    print()
    updated_records = storage.get_updated_records(
        stored_records, target_date, new_entries
    )
    storage.save_records(updated_records, STORAGE_LOCATION)
    print("Your record has been updated.")


def summarize_records_data() -> None:
    """
    Summarize the available data of the records.
    """

    stored_records = storage.load_records(STORAGE_LOCATION)
    summarized_data = analytics.generate_summary(stored_records)

    if not summarized_data:
        print("No record present for forming summary!")
        return

    presentation.present_summary(summarized_data)


def highest_in_a_day() -> None:
    """
    Provide the highest values of all the fields along with their corresponding dates.
    """

    stored_records = storage.load_records(STORAGE_LOCATION)
    highest_val_and_date_data = analytics.get_highest_val_and_corresponding_dates(
        stored_records
    )

    if not highest_val_and_date_data:
        print("No records are present!")
        return

    presentation.present_highest_in_a_day(highest_val_and_date_data)


def run_exploration_menu() -> None:
    """
    Exhibit available features for data exploration.
    """

    actions = {1: summarize_records_data, 2: highest_in_a_day, 3: sys.exit}

    presentation.display_menu(features_info.EXPLORATION_FEATURES)
    user_choice = input_handler.get_user_choice(features_info.EXPLORATION_FEATURES)
    print()
    actions[user_choice]()


def main() -> None:

    actions = {
        1: add_record,
        2: view_record,
        3: edit_record,
        4: run_exploration_menu,
        5: sys.exit,
    }

    storage.ensure_records_file_exists(STORAGE_LOCATION)
    presentation.display_menu(features_info.FEATURES)
    user_choice = input_handler.get_user_choice(features_info.FEATURES)
    print()
    actions[user_choice]()


if __name__ == "__main__":
    main()
