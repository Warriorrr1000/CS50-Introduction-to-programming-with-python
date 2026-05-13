from seasons import validate_date,calc_minutes,minutes_to_words
import pytest
from datetime import date

def test_valid_dates():
    assert validate_date("2010-04-25") == date(2010,4,25)
    assert validate_date("2011-08-13") == date(2011,8,13)
    assert validate_date("2026-01-15") == date(2026,1,15)
    assert validate_date("2024-02-29") == date(2024,2,29)
    assert validate_date("2000-02-29") == date(2000,2,29)
    assert validate_date("1999-12-31") == date(1999,12,31)

def test_invalid_dates():
    with pytest.raises(SystemExit):
        validate_date("2010-13-25")
    with pytest.raises(SystemExit):
        validate_date("2010-04-32")
    with pytest.raises(SystemExit):
        validate_date("2023-02-29")
    with pytest.raises(SystemExit):
        validate_date("abcd-ef-gh")
    with pytest.raises(SystemExit):
        validate_date("10-04-2020")
    with pytest.raises(SystemExit):
        validate_date("2020/04/10")
    with pytest.raises(SystemExit):
        validate_date("2010-13-08")

def test_minutes_conversion():
    assert calc_minutes(date(2025, 1, 2), date(2025, 1, 1)) == 1440
    assert calc_minutes(date(2025, 1, 10), date(2025, 1, 1)) == 12960
    assert calc_minutes(date(2024, 3, 1), date(2024, 2, 29)) == 1440
    assert calc_minutes(date(2025, 1, 1), date(2025, 1, 1)) == 0
    assert calc_minutes(date(2021, 1, 1), date(2020, 1, 1)) == 527040

def test_number_to_words():
    assert minutes_to_words(0) == "Zero minute"
    assert minutes_to_words(1) == "One minute"
    assert minutes_to_words(15) == "Fifteen minutes"
    assert minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_words(1000000) == "One million minutes"
