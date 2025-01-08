#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_power_of_two function.

Test categories:
    - Standard cases: typical inputs such as small powers of two and non-powers of two.
    - Edge cases: inputs like zero, negative numbers, valid floats (e.g., 16.0), boundary number.
    - Defensive tests: invalid input types such as strings, lists, and other assertions.

Created on 2024-12-31
@author: Gennadii Ershov
"""

import unittest

from ..is_power_of_two import is_power_of_two


class TestIsPowerOfTwo(unittest.TestCase):
    """Test the is_power_of_two function"""

    # Standard test cases
    def test_single_is_power_of_two(self):
        """Test if n = 1 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(1))

    def test_large_power_of_two(self):
        """Test if n = 16 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(16))

    def test_non_power_of_two(self):
        """Test if n = 3 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(3))

    # Edge cases
    def test_zero(self):
        """Test if n = 0 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(0))

    def test_negative_number(self):
        """Test if n = -2 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(-2))

    def test_float_power_of_two(self):
        """Test if n = 16.0 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(16.0))

    def test_float_non_power_of_two(self):
        """Test if n = 3.5 is correctly identified as not a power of two."""
        self.assertFalse(is_power_of_two(3.5))

    def test_large_power_of_two_boundary(self):
        """Test if n = 2^30 is correctly identified as a power of two."""
        self.assertTrue(is_power_of_two(2**30))

    # Defensive tests
    def test_invalid_type_string(self):
        """Test if a string raises an AssertionError."""
        with self.assertRaises(AssertionError):
            is_power_of_two("16")

    def test_invalid_type_list(self):
        """Test if a list raises an AssertionError."""
        with self.assertRaises(AssertionError):
            is_power_of_two([16])

    def test_out_of_range_upper(self):
        """Test if a value greater than 2^31 - 1 raises an AssertionError."""
        with self.assertRaises(AssertionError):
            is_power_of_two(2**31)

    def test_out_of_range_lower(self):
        """Test if a value less than -2^31 raises an AssertionError."""
        with self.assertRaises(AssertionError):
            is_power_of_two(-(2**31) - 1)
