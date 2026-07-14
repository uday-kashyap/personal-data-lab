import date_utils


def test_build_date_builds_date_from_date_attributes():
    result = date_utils.build_date(1, 1, 1999)
    assert result == "1999/01/01"
