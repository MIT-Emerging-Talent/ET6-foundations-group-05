#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the max_profit function.

This module contains unit tests to validate the functionality of the
max_profit function, ensuring it handles various scenarios correctly.

Tests include:
    - Standard test cases for typical stock price patterns.
    - Edge cases, such as a single day or an empty list.
    - Defensive tests to handle invalid inputs.

Created on 12-28-2024
@author: Muhammet Isik
"""

import unittest
from ..max_profit import max_profit


class TestMaxProfit(unittest.TestCase):
    """Test the max_profit function"""

    # Standard test cases
    def test_increasing_prices(self):
        """It should calculate the maximum profit for increasing prices"""
        actual = max_profit([1, 2, 3, 4, 5])
        expected = 4  # Buy at 1, sell at 5
        self.assertEqual(actual, expected)

    def test_decreasing_prices(self):
        """It should return 0 for decreasing prices as no profit is possible"""
        actual = max_profit([5, 4, 3, 2, 1])
        expected = 0  # No profit possible
        self.assertEqual(actual, expected)

    def test_mixed_prices(self):
        """It should calculate the maximum profit for mixed prices"""
        actual = max_profit([7, 1, 5, 3, 6, 4])
        expected = 5  # Buy at 1, sell at 6
        self.assertEqual(actual, expected)

    def test_no_profit(self):
        """It should return 0 if there is no profit to be made"""
        actual = max_profit([7, 7, 7, 7])
        expected = 0  # All prices are the same
        self.assertEqual(actual, expected)

    # Edge cases
    def test_single_day(self):
        """It should return 0 for a single day as no transactions can be made"""
        actual = max_profit([7])
        expected = 0
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """It should return 0 for an empty list as no transactions can be made"""
        actual = max_profit([])
        expected = 0
        self.assertEqual(actual, expected)

    # Defensive tests
    def test_invalid_input_not_a_list(self):
        """It should raise an assertion error if the input is not a list"""
        with self.assertRaises(AssertionError):
            max_profit("not a list")

    def test_invalid_input_non_integer_elements(self):
        """It should raise an assertion error if the list contains non-integer elements"""
        with self.assertRaises(AssertionError):
            max_profit([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
