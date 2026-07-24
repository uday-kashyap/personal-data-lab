from src.models import Record


def present_record(record: Record) -> None:
    """
    Display given record into a user-readable manner.
    """

    print("----Your Record----")
    for field, field_val in record.items():
        cleaned_field = field.replace("_", " ")

        print(f"{cleaned_field.title()}: {field_val}")


def display_menu(menu_options: dict[int, str]) -> None:
    """
    Display option numbers along with the option name.
    """

    for option_no, feature in menu_options.items():
        print(f"{option_no}. {feature}")


def present_summary(summarized_data: dict[str, int | float]) -> None:
    """
    Display the stats with their values as a summary.
    """

    field_units = {
        "avg_study_hours": "hrs/day",
        "avg_workout_minutes": "mins/day",
        "avg_mood": "/10",
        "avg_expense": "Rupees/day",
    }

    print("========== Summary ==========")

    for stat, stat_val in summarized_data.items():
        cleaned_stat = stat.replace("_", " ")
        stat_unit = field_units.get(stat, "")

        print(f"{cleaned_stat.title()}: {stat_val} {stat_unit}")

    print("=============================")
