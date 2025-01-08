#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_palindrome function.

This module tests the `is_palindrome` function with standard, edge, and defensive cases.

Created on 12 31 2024
"""

import unittest

from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """
    Test suite for the is_palindrome function.

    Ensures the function handles valid, edge, and invalid inputs correctly.
    """

    # Standard Cases
    def test_positive_palindrome(self):
        """Return True for numeric palindromes."""
        self.assertTrue(is_palindrome(121))

    def test_non_palindrome(self):
        """Return False for non-palindromic numbers."""
        self.assertFalse(is_palindrome(123))

    def test_single_digit(self):
        """Return True for single-digit numbers."""
        self.assertTrue(is_palindrome(5))

    # Edge Cases
    def test_negative_number(self):
        """Return False for negative numbers."""
        self.assertFalse(is_palindrome(-121))

    def test_zero(self):
        """Return True for zero."""
        self.assertTrue(is_palindrome(0))

    # Defensive Cases - Each `AssertionError` gets its own test
    def test_raise_for_string(self):
        """Raise AssertionError for string input."""
        with self.assertRaises(AssertionError):
            is_palindrome("123")

    def test_raise_for_float(self):
        """Raise AssertionError for float input."""
        with self.assertRaises(AssertionError):
            is_palindrome(121.0)

    def test_raise_for_none(self):
        """Raise AssertionError for None input."""
        with self.assertRaises(AssertionError):
            is_palindrome(None)

    def test_raise_for_out_of_range_positive(self):
        """Raise AssertionError for out-of-range positive integer."""
        with self.assertRaises(AssertionError):
            is_palindrome(2**31)

    def test_raise_for_out_of_range_negative(self):
        """Raise AssertionError for out-of-range negative integer."""
        with self.assertRaises(AssertionError):
            is_palindrome(-(2**31) - 1)


if __name__ == "__main__":
    unittest.main()
