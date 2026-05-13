from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("8.8.8.8") == True
    assert validate("127.0.0.1") == True

def test_invalid_ips():
    assert validate("256.168.0.1") == False
    assert validate("192.168.0.300") == False
    assert validate("192.168.1") == False
    assert validate("192@168@0@1") == False

def test_alpha():
    assert validate("192.168.1.abc") == False
    assert validate("cs50 is good") == False