import storage
import input_handler

STORAGE_LOCATION = "data/records.json"

if __name__ == "__main__":
    storage.ensure_records_file_exists(STORAGE_LOCATION)
    record = input_handler.collect_record()
    user_records = storage.load_records(STORAGE_LOCATION)
    user_records.append(record)
    storage.save_records(user_records, STORAGE_LOCATION)
