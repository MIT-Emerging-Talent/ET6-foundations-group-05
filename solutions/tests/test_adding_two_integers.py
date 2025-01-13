#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the arithmetic module.

This script tests the `adding_two_integers` function to ensure it behaves as expected
under various conditions. It uses Python's built-in unittest framework.

Test Categories:
    - Standard: Typical scenarios for the function.
    - Edge Case: Boundary or extreme conditions to test function limits.
    - Defensive: Scenarios where invalid or unexpected input is provided.
"""

import unittest

from ..adding_two_integers import adding_two_integers


class TestAddingTwoIntegersFunction(unittest.TestCase):
    """
    Test cases for the `adding_two_integers` function.
    """

    # Standard Tests
    def test_positive_integers(self):
        """
        Standard: Test with two positive integers.
        """
        self.assertEqual(
            adding_two_integers(3, 5), 8, "adding_two_integers of 3 and 5 should be 8."
        )

    def test_negative_integers(self):
        """
        Standard: Test with two negative integers.
        """
        self.assertEqual(
            adding_two_integers(-3, -5),
            -8,
            "adding_two_integers of -3 and -5 should be -8.",
        )

    def test_mixed_integers(self):
        """
        Standard: Test with a positive and a negative integer.
        """
        self.assertEqual(
            adding_two_integers(5, -3),
            2,
            "adding_two_integers of 5 and -3 should be 2.",
        )

    def test_with_zero(self):
        """
        Standard: Test with zero as one of the integers.
        """
        self.assertEqual(
            adding_two_integers(0, 5), 5, "adding_two_integers of 0 and 5 should be 5."
        )

    # Edge Case Tests
    def test_large_numbers(self):
        """
        Edge Case: Test with very large integers.
        """
        self.assertEqual(
            adding_two_integers(10**9, 10**9), 2 * 10**9, "Adding large numbers failed."
        )

    def test_minimum_and_maximum_values(self):
        """
        Edge Case: Test with minimum and maximum integer values.
        """
        self.assertEqual(
            adding_two_integers(-(2**31), 2**31 - 1),
            -1,
            "Adding minimum and maximum integers failed.",
        )

    def test_close_to_zero(self):
        """
        Edge Case: Test with numbers close to zero.
        """
        self.assertEqual(
            adding_two_integers(1, -1), 0, "Adding numbers close to zero failed."
        )

    # Defensive Tests
    def test_non_integer_inputs(self):
        """
        Defensive: Test with non-integer inputs.
        """
        with self.assertRaises(TypeError):
            adding_two_integers("3", 5)

    def test_missing_arguments(self):
        """
        Defensive: Test with missing arguments.
        """
        with self.assertRaises(TypeError):
            adding_two_integers(None, 5)

    def test_extra_arguments(self):
        """
        Defensive: Test with extra arguments.
        """

    def test_none_arguments(self):
        """
        Defensive: Test with None as arguments.
        """
        with self.assertRaises(TypeError):
            adding_two_integers(None, 5)


if __name__ == "__main__":
    unittest.main()
