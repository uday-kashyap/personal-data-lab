import pytest


@pytest.fixture
def sample_record():
    return {"study_hours": 24, "workout_minutes": 1440, "expense": 10000, "mood": 5}
