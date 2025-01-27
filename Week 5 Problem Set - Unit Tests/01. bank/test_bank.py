from bank import value
import pytest

def main():
    # test_numbers()
    test_upper_lower_cases()
    test_whole_phrase()

def test_return_zero():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('hello madafaka') == 0
    assert value('Hello Madafaka') == 0

def test_return_twenty():
    assert value("hey") == 20
    assert value("Hi") == 20

def test_return_hundred():
    assert value("What's up?") == 100
    assert value('good morning') == 100

if __name__ == '__main__':
    main()
