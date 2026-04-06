from plates import is_valid

def test_rule_1():
    assert is_valid("C1") == False
    assert is_valid("cf") == True

def test_rule_2():
    assert is_valid("C") == False
    assert is_valid("Cs50isgood") == False
    assert is_valid("CS50") == True

def test_rule_3():
    assert is_valid("CSS500") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False

def test_rule_4():
    assert is_valid("Cs50!!") == False