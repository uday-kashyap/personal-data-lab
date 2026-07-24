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


@pytest.fixture
def sample_records(sample_record) -> list[dict[str, int | float]]:
    sample_record1 = sample_record
    sample_record2 = {
        "date": "1999/01/02",
        "study_hours": 12.0,
        "workout_minutes": 786,
        "expense": 5000.0,
        "mood": 3,
    }
    sample_record3 = {
        "date": "1999/01/03",
        "study_hours": 1.5,
        "workout_minutes": 0,
        "expense": 1.0,
        "mood": 10,
    }

    return [sample_record1, sample_record2, sample_record3]
