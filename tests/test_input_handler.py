import input_handler
import builtins


def test_collect_record_returns_record(monkeypatch, sample_raw_record, sample_record):
    values = [sample_raw_record[field] for field in input_handler.REQUIRED_FIELDS]
    monkeypatch.setattr(builtins, "input", lambda prompt: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record
