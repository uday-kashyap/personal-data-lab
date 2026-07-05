import storage

STORAGE_LOCATION = "data/records.json"

if __name__ == "__main__":
    storage.ensure_records_file_exists(STORAGE_LOCATION)

    # Rough Input logic
    record = {"study_hours": 0, "workout_minutes": 0, "expense": 0, "mood": 5}

    for field_name in record:

        field_val = int(input(f"Enter {field_name} of today: "))
        record[field_name] = field_val

    user_records = storage.load_records(STORAGE_LOCATION)
    user_records.append(record)
    storage.save_records(user_records, STORAGE_LOCATION)
