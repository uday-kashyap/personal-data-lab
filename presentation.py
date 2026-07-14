from models import Record


def present_record(record: Record) -> None:
    """
    Display given record into a user-readable manner.
    """

    print("----Your Record----")
    for field, field_val in record.items():
        cleaned_field = field.replace("_", " ")

        print(f"{cleaned_field.title()}: {field_val}")
