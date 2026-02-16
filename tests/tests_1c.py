"""
tests_1c.py

This module contains unit tests for the simple_calculator function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(nums) == 6

def test_empty_max_subarray_sum():
    nums = []
    assert max_subarray_sum(nums) == 0

if __name__ == "__main__":
    pytest.main()