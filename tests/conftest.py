import pytest
import input_handler
from models import Record


@pytest.fixture
def sample_record() -> Record:
    return {
        "date": "1999/01/01",
        "study_hours": 24.0,
        "workout_minutes": 1440,
        "expense": 10000.0,
        "mood": 5,
    }


@pytest.fixture
def mock_current_date(monkeypatch) -> None:
    monkeypatch.setattr(input_handler, "_get_current_date", lambda: "1999/01/01")
