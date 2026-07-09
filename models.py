from typing import TypedDict


class Record(TypedDict):
    date: str
    study_hours: float
    workout_minutes: int
    expense: float
    mood: int
