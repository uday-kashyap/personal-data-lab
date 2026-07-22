from datetime import date


def build_date(day: int, month: int, year: int):
    """
    Convert day, month and year into YYYY/MM/DD format and return it.
    """

    return f"{year:04d}/{month:02d}/{day:02d}"


def get_current_date() -> str:
    """
    Return today's date in YYYY/MM/DD format.
    """

    today = date.today()
    formatted_date = today.strftime("%Y/%m/%d")
    return formatted_date
