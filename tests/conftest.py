import pytest
import input_handler


@pytest.fixture
def sample_record():
    return {
        "date": "1999/01/01",
        "study_hours": 24.0,
        "workout_minutes": 1440,
        "expense": 10000.0,
        "mood": 5,
    }


@pytest.fixture
def mock_current_date(monkeypatch):
    monkeypatch.setattr(input_handler, "_get_current_date", lambda: "1999/01/01")
