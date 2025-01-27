from plates import is_valid
import pytest

def main():
    test_min_max_chars()
    test_start_with_two_letters()
    test_middle_chars()
    test_start_for_zero()
    test_punctuation()

def test_min_max_chars():
   assert is_valid('XX') == True
   assert is_valid('XXXXXX') == True
   assert is_valid('X') == False
   assert is_valid('XXXXXXX') == False


def test_start_with_two_letters():
    assert is_valid('XX') == True
    assert is_valid('X2') == False
    assert is_valid('2X') == False
    assert is_valid('22') == False

def test_middle_chars():
    assert is_valid('XXX222') == True
    assert is_valid('XXX22X') == False
    assert is_valid('XXX22X') == False

def test_start_for_zero():
    assert is_valid('CS05') == False
    assert is_valid('CS50') == True

def test_punctuation():
    assert is_valid ('PI3.14') == False
    assert is_valid ('PI3!14') == False
    assert is_valid ('PI3 14') == False


if __name__ == "__main__":
    main()
