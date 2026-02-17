import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import task3

def test_check_number():
    assert task3.check_number(10) == "Positive"
    assert task3.check_number(-5) == "Negative"
    assert task3.check_number(0) == "Zero"

def test_primes():
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.get_first_10_primes() == expected_primes

def test_sum():
    # the sum of 1 to 100 = 5050
    assert task3.sum_1_to_100() == 5050