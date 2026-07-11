import storage
import input_handler
import sys

STORAGE_LOCATION = "data/records.json"

if __name__ == "__main__":
    storage.ensure_records_file_exists(STORAGE_LOCATION)
    record = input_handler.collect_record()
    stored_records = storage.load_records(STORAGE_LOCATION)

    if storage.has_record_for_date(stored_records, record["date"]):
        print("Record already exists for today's date!")
        sys.exit()

    stored_records.append(record)
    storage.save_records(stored_records, STORAGE_LOCATION)
    print("Your record has been saved successfully.")
