"""
tests_1d.py

This module contains unit tests for the simple_calculator function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sums():
    nums = [2, 7, 11, 15]
    target = 13
    result = two_sum(nums, target)
    assert result == [0, 2]

def test_zero_two_sum():
    nums = [2, 7, 11, 15]
    target = 29
    result = two_sum(nums, target)
    assert result == []

if __name__ == "__main__":
    pytest.main()