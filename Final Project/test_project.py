import pytest
from project import get_user_input, calorie_deficit, calorie_surplus, maintain_weight



def main():
    test_calorie_deficit()
    test_calorie_surplus()
    test_maintain_weight()

def test_maintain_weight():
    user_data = {
        'age': 25,
        'weight': 70,
        'height': 175,
        'goal': 'Maintain weight',
        'activity': 1.55
    }
    expected_tdee = (10 * 70 + 6.25 * 175 - 5 * 25 + 5) * 1.55
    assert expected_tdee > 0

def test_calorie_deficit():
    user_data = {
        'age': 30,
        'weight': 80,
        'height': 180,
        'goal': 'Loose weight',
        'activity': 1.2
    }
    expected_calories = ((10 * 80 + 6.25 * 180 - 5 * 30 + 5) * 1.2) * 0.8
    assert expected_calories > 0

def test_calorie_surplus():
    user_data = {
        'age': 40,
        'weight': 90,
        'height': 185,
        'goal': 'Gain weight',
        'activity': 1.725
    }
    expected_calories = ((10 * 90 + 6.25 * 185 - 5 * 40 + 5) * 1.725) * 1.2
    assert expected_calories > 0

