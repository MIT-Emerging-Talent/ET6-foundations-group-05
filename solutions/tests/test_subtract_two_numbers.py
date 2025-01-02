#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for subtract_two_numbers function.

Test categories:
    - Standard cases: typical integer inputs
    - Edge cases: zero and mixed signs
    - Defensive tests: wrong input types, assertions

Created on 2025-01-01
Author: Geehan Ali
"""

import unittest

from solutions.subtract_two_numbers import (
    subtract_two_numbers,  # Adjust the import as necessary for your project structure
)


class TestSubtractTwoNumbers(unittest.TestCase):
    """Test suite for the subtract_two_numbers function."""

    # Standard test cases
    def test_positive_numbers(self):
        """It should return the difference of two positive integers."""
        self.assertEqual(subtract_two_numbers(10, 3), 7)

    def test_negative_numbers(self):
        """It should return the difference of two negative integers."""
        self.assertEqual(subtract_two_numbers(-5, -10), 5)

    # Edge cases
    def test_zero_subtraction(self):
        """It should handle subtraction involving zero."""
        self.assertEqual(subtract_two_numbers(0, 5), -5)
        self.assertEqual(subtract_two_numbers(5, 0), 5)

    def test_mixed_sign_numbers(self):
        """It should return the correct difference for mixed sign integers."""
        self.assertEqual(subtract_two_numbers(-5, 10), -15)
        self.assertEqual(subtract_two_numbers(10, -5), 15)

    # Defensive tests
    def test_non_integer_inputs(self):
        """It should raise TypeError for non-integer inputs."""
        with self.assertRaises(TypeError):
            subtract_two_numbers(10, "3")
        with self.assertRaises(TypeError):
            subtract_two_numbers("10", 3)
        with self.assertRaises(TypeError):
            subtract_two_numbers(10.5, 3)


if __name__ == "__main__":
    unittest.main()
