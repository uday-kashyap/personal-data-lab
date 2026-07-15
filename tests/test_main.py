import main
import input_handler
import storage
import date_utils
import presentation


def test_add_record_adds_record_to_the_records(monkeypatch, sample_record):

    def fake_save_records(modified_records, storage_location):
        saved["records"] = modified_records
        saved["location"] = storage_location

    monkeypatch.setattr(input_handler, "collect_record", lambda: sample_record)
    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(
        storage, "has_record_for_date", lambda stored_records, target_date: False
    )
    monkeypatch.setattr(storage, "save_records", fake_save_records)
    saved = {}
    main.add_record()
    assert saved["records"] == [sample_record]


def test_add_record_does_not_save_duplicate_record(monkeypatch, sample_record):
    monkeypatch.setattr(input_handler, "collect_record", lambda: sample_record)
    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(
        storage, "has_record_for_date", lambda stored_records, target_date: True
    )
    saved = {}
    main.add_record()
    assert saved == {}


def test_view_record_displays_queried_record(monkeypatch, sample_record):

    def fake_present_record(record):
        presented["record"] = record

    monkeypatch.setattr(
        input_handler, "get_date_attributes_from_user", lambda: (1, 1, 1999)
    )
    monkeypatch.setattr(date_utils, "build_date", lambda day, month, year: "1999/01/01")
    monkeypatch.setattr(
        storage, "load_records", lambda storage_location: [sample_record]
    )
    monkeypatch.setattr(
        storage, "get_record_by_date", lambda stored_records, target_date: sample_record
    )
    monkeypatch.setattr(presentation, "present_record", fake_present_record)
    presented = {}
    main.view_record()
    assert presented["record"] == sample_record


def test_view_record_could_not_fetch_missing_record(monkeypatch, sample_record):

    def fake_present_record(record):
        presented["record"] = record

    monkeypatch.setattr(
        input_handler, "get_date_attributes_from_user", lambda: (1, 1, 1999)
    )
    monkeypatch.setattr(date_utils, "build_date", lambda day, month, year: "1999/01/01")
    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(
        storage, "get_record_by_date", lambda stored_records, target_date: None
    )
    monkeypatch.setattr(presentation, "present_record", fake_present_record)
    presented = {}
    main.view_record()
    assert presented == {}
