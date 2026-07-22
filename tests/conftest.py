import pytest
from src.models import Record


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
def sample_user_entries() -> dict[str, int | float]:
    return {
        "study_hours": 24.0,
        "workout_minutes": 1440,
        "expense": 10000.0,
        "mood": 5,
    }
