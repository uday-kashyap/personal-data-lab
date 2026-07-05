import storage
import json


def test_ensure_records_file_exists_creates_missing_storage_directory(tmp_path):
    storage_location = tmp_path / "data" / "examples_records.json"
    storage_directory = storage_location.parent
    assert not storage_directory.exists()
    storage.ensure_records_file_exists(storage_location)
    assert storage_directory.exists()


def test_ensure_records_file_exists_creates_missing_file(tmp_path):
    storage_location = tmp_path / "data" / "example_records.json"
    storage.ensure_records_file_exists(storage_location)
    assert storage_location.exists()


def test_ensure_records_file_exists_inserts_empty_square_brackets(tmp_path):
    storage_location = tmp_path / "data" / "example_records.json"
    storage.ensure_records_file_exists(storage_location)

    with open(storage_location, "r") as file:
        records = json.load(file)

    assert records == []


def test_load_records_returns_existing_record(tmp_path, sample_record):
    storage_location = tmp_path / "data" / "example_records.json"
    storage_location.parent.mkdir()

    with open(storage_location, "w") as file:
        json.dump([sample_record], file)

    records = storage.load_records(storage_location)
    assert records == [sample_record]


def test_save_records_adds_new_record(tmp_path, sample_record):
    storage_location = tmp_path / "data" / "example_records.json"
    storage_location.parent.mkdir()
    sample_records = [sample_record]
    storage.save_records(sample_records, storage_location)

    with open(storage_location, "r") as file:
        records = json.load(file)

    assert records == sample_records
