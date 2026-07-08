import input_handler
import builtins


def test_collect_record_returns_a_valid_record(monkeypatch, sample_record):
    values = [sample_record[field] for field in input_handler.REQUIRED_FIELDS]
    monkeypatch.setattr(builtins, "input", lambda prompt: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record


def test_collect_record_retries_on_invalid_input_type(monkeypatch, sample_record):
    values = ["abc", 24.0, 1440, 10000.0, 5]
    monkeypatch.setattr(builtins, "input", lambda prompt: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record


def test_collect_record_retries_when_input_violates_field_range(
    monkeypatch, sample_record
):
    values = [-24, 24.0, 1441, 1440, -500, 10000.0, 0, 5]
    monkeypatch.setattr(builtins, "input", lambda prompt: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record
