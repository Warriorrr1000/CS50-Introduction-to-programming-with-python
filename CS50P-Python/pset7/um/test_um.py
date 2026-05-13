from um import count

def test_valid_counts():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("How are you?") == 0
    assert count("Um...") == 1

def test_invalid_ums():
    assert count("pneumonoultramicroscopicsilicovalcanoconiosis") == 0
    assert count("The food is very yummy um") == 1
    assert count("ummm the food tastes Supercalifragilisticexpialidocious") == 0
    assert count("Um... I Was thinking if i could get into Harvard or MIT") == 1

def test_numbered_ums():
    assert count("Ummm9") == 0
    assert count("Um0") == 0

def test_case_sensitivity():
    assert count("UM.. I'm very anxious about my 10th boards.") == 1
    assert count("Person 1: How are things going? Person 2: um... things are going pretty well")