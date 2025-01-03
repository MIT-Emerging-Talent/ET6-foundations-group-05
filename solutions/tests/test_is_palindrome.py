#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_palindrome function.

Created on 12 31 2024
@author: Muhammet Isik
"""

import unittest

from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Tests for the is_palindrome function"""

    def test_positive_palindrome(self):
        """It should return True for a positive palindrome."""
        self.assertTrue(is_palindrome(121))

    def test_negative_number(self):
        """It should return False for a negative number."""
        self.assertFalse(is_palindrome(-121))

    def test_non_palindrome(self):
        """It should return False for a non-palindrome."""
        self.assertFalse(is_palindrome(123))

    def test_single_digit(self):
        """It should return True for single-digit numbers."""
        self.assertTrue(is_palindrome(5))

    def test_zero(self):
        """It should return True for zero."""
        self.assertTrue(is_palindrome(0))

    def test_none_input(self):
        """It should return False for None input."""
        self.assertFalse(is_palindrome(None))

    def test_special_characters(self):
        """It should return False for special character input."""
        self.assertFalse(is_palindrome("#$%"))

    def test_string_input(self):
        """It should return False for string input."""
        self.assertFalse(is_palindrome("abc"))

    def test_float_input(self):
        """It should return False for float input."""
        self.assertFalse(is_palindrome(121.0))

    def test_empty_string(self):
        """It should return False for an empty string."""
        self.assertFalse(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
