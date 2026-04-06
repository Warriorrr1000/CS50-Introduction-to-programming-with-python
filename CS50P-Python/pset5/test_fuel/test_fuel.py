from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("2/4") == 50
    assert convert("1/4") == 25

def test_value_error():
    with pytest.raises(ValueError):
        assert convert("5/2")
        assert convert("-1/2")

def test_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"