from jar import Jar
import pytest

def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    #Check default value
    jar1 = Jar()
    assert jar1.capacity == 12
    jar2 = Jar(25)
    assert jar2.capacity == 25
    #Check That on negative integer it throws ValueError
    with pytest.raises(ValueError):
        jar3 = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(15)
    jar.deposit(9)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8
    jar.withdraw(6)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(5)