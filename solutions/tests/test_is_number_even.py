#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Even Number Checker Tests
=============================
This script contains unit tests for the even number checker function using the unittest module.

Test categories:
    - Standard tests for known even and odd numbers
    - Defensive tests for non-integer values
    - Edge cases for boundary values and unusual inputs

Author: Geehan Ali
Created on: 01 08 2025
"""

import unittest

from ..is_number_even import is_number_even  # type: ignore


class TestStandardCases(unittest.TestCase):
    """
    Standard tests for even and odd numbers
    """

    def test_is_number_even_2(self):
        """Test that 2 is an even number"""
        self.assertTrue(is_number_even(2))

    def test_is_number_even_10(self):
        """Test that 10 is an even number"""
        self.assertTrue(is_number_even(10))

    def test_is_number_even_0(self):
        """Test that 0 is an even number"""
        self.assertTrue(is_number_even(0))

    def test_is_odd_3(self):
        """Test that 3 is not an even number"""
        self.assertFalse(is_number_even(3))

    def test_is_odd_7(self):
        """Test that 7 is not an even number"""
        self.assertFalse(is_number_even(7))

    def test_is_odd_negative_1(self):
        """Test that -1 is not an even number"""
        self.assertFalse(is_number_even(-1))


class TestEdgeCases(unittest.TestCase):
    """
    Edge cases for boundary values and unusual inputs
    """

    def test_large_even_number(self):
        """Test that a very large even number is identified correctly"""
        self.assertTrue(is_number_even(10**6))

    def test_large_odd_number(self):
        """Test that a very large odd number is identified correctly"""
        self.assertFalse(is_number_even(10**6 + 1))

    def test_negative_even_number(self):
        """Test that a negative even number is identified correctly"""
        self.assertTrue(is_number_even(-4))


class TestDefensiveCases(unittest.TestCase):
    """
    Defensive tests for non-integer values
    """

    def test_non_integer_input_float(self):
        """Test that a float raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_number_even(2.5)

    def test_non_integer_input_string(self):
        """Test that a string raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_number_even("string")

    def test_non_integer_input_none(self):
        """Test that None raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_number_even(None)


if __name__ == "__main__":
    unittest.main()
