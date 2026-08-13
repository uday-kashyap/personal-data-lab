import src.main as main
import src.input_handler as input_handler
import src.storage as storage
import src.date_utils as date_utils
import src.presentation as presentation
import src.records as records
import src.analytics as analytics


def test_add_record_adds_record_to_the_records(
    monkeypatch, sample_record, sample_user_entries
):

    def fake_save_records(modified_records, storage_location):
        saved["records"] = modified_records
        saved["location"] = storage_location

    monkeypatch.setattr(
        input_handler, "collect_user_entries", lambda: sample_user_entries
    )
    monkeypatch.setattr(records, "create_record", lambda user_entries: sample_record)
    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(
        storage, "has_record_for_date", lambda stored_records, target_date: False
    )
    monkeypatch.setattr(storage, "save_records", fake_save_records)
    saved = {}
    main.add_record()
    assert saved["records"] == [sample_record]


def test_add_record_does_not_save_duplicate_record(
    monkeypatch, sample_record, sample_user_entries
):
    monkeypatch.setattr(
        input_handler, "collect_user_entries", lambda: sample_user_entries
    )
    monkeypatch.setattr(records, "create_record", lambda user_entries: sample_record)
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


def test_view_record_could_not_fetch_missing_record(monkeypatch):

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


def test_edit_record_edits_existing_record(monkeypatch, sample_record):

    def fake_save_records(stored_records, storage_location):
        saved["records"] = stored_records
        saved["location"] = storage_location

    monkeypatch.setattr(
        input_handler, "get_date_attributes_from_user", lambda: (1, 1, 1999)
    )
    monkeypatch.setattr(date_utils, "build_date", lambda day, month, year: "1999/01/01")
    monkeypatch.setattr(
        storage, "load_records", lambda storage_location: [sample_record]
    )
    monkeypatch.setattr(
        storage, "has_record_for_date", lambda stored_records, target_date: True
    )

    updated_entries = {
        "study_hours": 12.0,
        "workout_minutes": 720,
        "expense": 5000.0,
        "mood": 1,
    }

    updated_record = {**sample_record, **updated_entries}

    monkeypatch.setattr(input_handler, "collect_user_entries", lambda: updated_entries)
    monkeypatch.setattr(
        storage,
        "get_updated_records",
        lambda stored_records, target_date, new_entries: [updated_record],
    )
    monkeypatch.setattr(storage, "save_records", fake_save_records)
    saved = {}
    main.edit_record()
    assert saved["records"] == [updated_record]


def test_edit_record_could_not_edit_missing_record(monkeypatch, sample_record):

    def fake_save_records(stored_records, storage_location):
        saved["records"] = stored_records
        saved["location"] = storage_location

    monkeypatch.setattr(
        input_handler, "get_date_attributes_from_user", lambda: (1, 1, 1999)
    )
    monkeypatch.setattr(date_utils, "build_date", lambda day, month, year: "1999/01/01")
    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(
        storage, "has_record_for_date", lambda stored_records, target_date: False
    )

    updated_entries = {
        "study_hours": 12.0,
        "workout_minutes": 720,
        "expense": 5000.0,
        "mood": 1,
    }

    updated_record = {**sample_record, **updated_entries}

    monkeypatch.setattr(input_handler, "collect_user_entries", lambda: updated_entries)
    monkeypatch.setattr(
        storage,
        "get_updated_records",
        lambda stored_records, target_date, new_entries: [updated_record],
    )
    monkeypatch.setattr(storage, "save_records", fake_save_records)
    saved = {}
    main.edit_record()
    assert saved == {}


def test_summarize_records_data_could_not_summarize_missing_records(monkeypatch):

    def fake_present_summary(summarized_data):
        presented["summarized_data"] = summarized_data

    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(analytics, "generate_summary", lambda stored_records: None)
    monkeypatch.setattr(presentation, "present_summary", fake_present_summary)
    presented = {}
    main.summarize_records_data()
    assert presented == {}


def test_summarize_records_data_summarizes_existing_records(
    monkeypatch, sample_records
):

    def fake_present_summary(summarized_data):
        presented["summarized_data"] = summarized_data

    monkeypatch.setattr(
        storage, "load_records", lambda storage_location: sample_records
    )
    expected = {
        "total_records": 3,
        "avg_study_hours": 12.50,
        "avg_workout_minutes": 742.00,
        "avg_mood": 6.00,
        "avg_expense": 5000.33,
    }
    monkeypatch.setattr(analytics, "generate_summary", lambda stored_records: expected)
    monkeypatch.setattr(presentation, "present_summary", fake_present_summary)
    presented = {}
    main.summarize_records_data()
    assert presented["summarized_data"] == expected


def test_highest_in_a_day_could_not_fetch_field_stats_for_missing_records(monkeypatch):

    def fake_present_highest_in_a_day(field_data):
        presented["field_data"] = field_data

    monkeypatch.setattr(storage, "load_records", lambda storage_location: [])
    monkeypatch.setattr(
        presentation, "present_highest_in_a_day", fake_present_highest_in_a_day
    )
    presented = {}
    main.highest_in_a_day()
    assert presented == {}


def test_highest_in_a_day_presents_highest_vals_and_dates_for_each_field(
    monkeypatch, sample_records
):

    def fake_present_highest_in_a_day(field_data):
        presented["field_data"] = field_data

    monkeypatch.setattr(
        storage, "load_records", lambda storage_location: sample_records
    )
    monkeypatch.setattr(
        presentation, "present_highest_in_a_day", fake_present_highest_in_a_day
    )
    presented = {}
    expected = {
        "study_hours": {24.0: ["1999/01/01"]},
        "workout_minutes": {1440: ["1999/01/01"]},
        "expense": {10000.0: ["1999/01/01"]},
        "mood": {10: ["1999/01/03"]},
    }
    main.highest_in_a_day()
    assert presented["field_data"] == expected
