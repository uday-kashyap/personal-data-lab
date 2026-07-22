import src.records as records
import src.date_utils as date_utils


def test_create_record_returns_a_valid_record(
    monkeypatch, sample_record, sample_user_entries
):
    monkeypatch.setattr(date_utils, "get_current_date", lambda: "1999/01/01")
    record = records.create_record(sample_user_entries)
    assert record == sample_record
