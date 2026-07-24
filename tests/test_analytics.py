import src.analytics as analytics
import pytest


def test_generate_summary_returns_None_for_missing_records():
    summarized_data = analytics.generate_summary([])
    assert summarized_data is None


def test_generate_summary_returns_summarized_data_for_existing_records(sample_records):
    stored_records = sample_records
    summarized_data = analytics.generate_summary(stored_records)
    expected = {
        "total_records": 3,
        "avg_study_hours": 12.50,
        "avg_workout_minutes": 742.00,
        "avg_mood": 6.00,
        "avg_expense": 5000.33,
    }
    assert summarized_data == expected


def test_get_number_of_records_returns_total_records_count(sample_records):
    total_records = analytics.get_number_of_records(sample_records)
    assert total_records == len(sample_records)


def test_get_average_for_a_day_returns_None_for_missing_records():
    avg = analytics.get_average_for_a_day([], "some_field")
    assert avg is None


@pytest.mark.parametrize(
    "field_name, expected",
    [
        ("study_hours", 12.50),
        ("workout_minutes", 742.00),
        ("mood", 6.00),
        ("expense", 5000.33),
    ],
)
def test_get_average_for_a_day_returns_average_values_for_existing_records(
    sample_records, field_name, expected
):
    avg = analytics.get_average_for_a_day(sample_records, field_name)
    assert avg == expected
