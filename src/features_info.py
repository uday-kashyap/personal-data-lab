FEATURES = {
    1: "Add Record",
    2: "View Record",
    3: "Edit Record",
    4: "Explore Data",
    5: "Exit",
}

EXPLORATION_FEATURES = {1: "Get Summary", 2: "Highest In A Day", 3: "Exit"}

REQUIRED_FIELDS = ("study_hours", "workout_minutes", "expense", "mood")

FIELD_TYPES = {
    "study_hours": float,
    "workout_minutes": int,
    "expense": float,
    "mood": int,
}

FIELD_RANGES = {
    "study_hours": (0, 24),
    "workout_minutes": (0, 1440),
    "expense": (0, float("inf")),
    "mood": (1, 10),
}
