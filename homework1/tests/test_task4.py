import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task4

def test_calculate_discount_integers():
    # test it with standard integers (100 - 20% = 80)
    assert task4.calculate_discount(100, 20) == 80

def test_calculate_discount_floats():
    # test i with floats (50.0 - 10.0% = 45.0)
    # use the pytest.approx because the floating point math can be tiny bit off (like 44.999999)
    result = task4.calculate_discount(50.0, 10.0)
    assert result == pytest.approx(45.0)

def test_calculate_discount_mixed():
    # test with mixed types (int price, float discount)
    assert task4.calculate_discount(100, 10.5) == 89.5