import input_handler
import builtins
from main import FEATURES
import pytest


def test_collect_record_returns_a_valid_record(
    monkeypatch, sample_record, mock_current_date
):
    values = [sample_record[field] for field in input_handler.REQUIRED_FIELDS]
    monkeypatch.setattr(builtins, "input", lambda _: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record


def test_collect_record_retries_on_invalid_input_type(
    monkeypatch, sample_record, mock_current_date
):
    values = ["abc", 24.0, 1440, 10000.0, 5]
    monkeypatch.setattr(builtins, "input", lambda _: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record


def test_collect_record_retries_when_input_violates_field_range(
    monkeypatch, sample_record, mock_current_date
):
    values = [-24, 24.0, 1441, 1440, -500, 10000.0, 0, 5]
    monkeypatch.setattr(builtins, "input", lambda _: values.pop(0))
    record = input_handler.collect_record()
    assert record == sample_record


@pytest.mark.parametrize("choice", FEATURES.keys())
def test_get_user_choice_returns_a_valid_choice(monkeypatch, choice):
    monkeypatch.setattr(builtins, "input", lambda _: choice)
    returned_choice = input_handler.get_user_choice(FEATURES)
    assert returned_choice == choice


def test_get_user_choice_retries_on_invalid_choice(monkeypatch):
    choices = [10000, -1, 0, 1]
    valid_value = 1
    monkeypatch.setattr(builtins, "input", lambda _: choices.pop(0))
    returned_choice = input_handler.get_user_choice(FEATURES)
    assert returned_choice == valid_value


def test_get_user_choice_retries_on_invalid_choice_type(monkeypatch):
    choices = ["abc", "-1.5", "0", ".", "1"]
    valid_value = 1
    monkeypatch.setattr(builtins, "input", lambda _: choices.pop(0))
    returned_choice = input_handler.get_user_choice(FEATURES)
    assert returned_choice == valid_value


def test_get_date_attributes_from_user_returns_date_attributes(monkeypatch):
    date_attributes = [1, 7, 2000]
    monkeypatch.setattr(builtins, "input", lambda _: date_attributes.pop(0))
    returned_date_attributes = input_handler.get_date_attributes_from_user()
    assert returned_date_attributes == (1, 7, 2000)


def test_get_date_attributes_from_user_retries_on_invalid_type(monkeypatch):
    date_attributes = ["abc", "1.5", "k", 1, 7, 2000]
    monkeypatch.setattr(builtins, "input", lambda _: date_attributes.pop(0))
    returned_date_attributes = input_handler.get_date_attributes_from_user()
    assert returned_date_attributes == (1, 7, 2000)
