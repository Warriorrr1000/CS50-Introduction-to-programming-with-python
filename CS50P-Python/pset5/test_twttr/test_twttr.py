from twttr import shorten

def test_str():
    assert shorten("Harry") == "Hrry"
    assert shorten("Warrior") == "Wrrr"
    assert shorten("CS50") == "CS50"