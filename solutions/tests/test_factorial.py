#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Banu Ozyilmaz
Created on: 12-28-2024

This script contains unit tests for the factorial function using the unittest module.

Test categories:
    - Standard test cases for base, small, medium, and large numbers
    - Edge cases for very large numbers (Due to recursion limits,
    the maximum value used here is 100)
    - Defensive test cases for invalid inputs (negative numbers, non-integer values)

"""

import math
import unittest
from solutions.factorial import factorial


class TestFactorial(unittest.TestCase):
    """Unit tests for the factorial function"""

    # Standard test cases
    def test_base_case_0(self):
        """Test the base case: factorial(0) should return 1"""
        self.assertEqual(factorial(0), 1)

    def test_small_number_1(self):
        """Test small positive number: factorial(1) should return 1"""
        self.assertEqual(factorial(1), 1)

    def test_small_number_3(self):
        """Test small positive number: factorial(3) should return 6"""
        self.assertEqual(factorial(3), 6)

    def test_medium_number_8(self):
        """Test medium positive number: factorial(8) should return 40320"""
        self.assertEqual(factorial(8), 40320)

    def test_medium_number_10(self):
        """Test medium positive number: factorial(10) should return 3628800"""
        self.assertEqual(factorial(10), 3628800)

    def test_large_number_15(self):
        """Test large positive number: factorial(15) should return 1307674368000"""
        self.assertEqual(factorial(15), 1307674368000)

    def test_large_number_20(self):
        """Test large positive number: factorial(20) should return 2432902008176640000"""
        self.assertEqual(factorial(20), 2432902008176640000)

    # Edge cases
    def test_edge_case_50(self):
        """Test edge case for very large positive number: factorial(50)"""
        self.assertEqual(
            factorial(50),
            30414093201713378043612608166064768844377641568960512000000000000,
        )

    def test_edge_case_100(self):
        """Test edge case for very large positive number: factorial(100)"""
        # Due to the line length limitation in Python, manually writing the expected result
        # for factorial(100) leads to a 'line too long' error. Therefore, I had to use
        # math.factorial(100) to dynamically calculate the expected result for comparison.
        expected_result = math.factorial(100)
        self.assertEqual(factorial(100), expected_result)

    # Defensive test cases
    def test_negative_number(self):
        """Test negative number input: should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            factorial(-2)

    def test_non_integer_input_float(self):
        """Test non-integer input (float): should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            factorial(2.5)

    def test_non_integer_input_string(self):
        """Test non-integer input (string): should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            factorial("string")

    def test_none_input(self):
        """Test None input: should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            factorial(None)


if __name__ == "__main__":
    unittest.main()
