from bank import value

def test_str():
    assert value("Hello kiddo how are you?") == 0
    assert value("Hi CS50 is a good course imo :) ") == 20
    assert value("I'm Warrior..") == 100

def test_lowercase():
    assert value("hello") == 0
    assert value("hey r u good?") == 20
    assert value("iDk") == 100