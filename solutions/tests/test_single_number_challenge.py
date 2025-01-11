#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Tests for single_number Function

This script contains unit tests for the `single_number` function in the
`single_number_solver` module. The function identifies the unique integer
in a list where every other integer appears exactly twice.

Test Categories:
    - Standard: Typical inputs with mixed, positive, or negative integers.
    - Edge Case: Tests with smallest and largest constraints.
    - Defensive: Tests for invalid or unexpected inputs.

Created on 2024-01-11
@author: Abbiihjah Oyeoku
"""

import unittest

from ..function_single_number_challenge import single_number


class TestSingleNumber(unittest.TestCase):
    """
    Unit test class for testing the `single_number` function.
    """

    # Standard Tests
    def test_standard_case(self):
        """
        Standard: Test with typical input.
        """
        self.assertEqual(single_number([2, 2, 1]), 1, "Failed on input [2, 2, 1]")
        self.assertEqual(
            single_number([4, 1, 2, 1, 2]), 4, "Failed on input [4, 1, 2, 1, 2]"
        )

    def test_single_element(self):
        """
        Standard: Test with a single element in the list.
        """
        self.assertEqual(single_number([1]), 1, "Failed on input [1]")

    # Edge Case Tests
    def test_large_numbers(self):
        """
        Edge Case: Test with very large integers.
        """
        self.assertEqual(
            single_number([10**6, 10**6, -(10**6)]), -(10**6), "Failed on large numbers"
        )

    def test_empty_list(self):
        """
        Edge Case: Test with an empty list (invalid input).
        """
        with self.assertRaises(ValueError, msg="Failed on empty input list"):
            single_number([])

    # Defensive Tests
    def test_non_integer_elements(self):
        """
        Defensive: Test with a list containing non-integer elements.
        """
        with self.assertRaises(
            TypeError, msg="Failed on input with non-integer elements"
        ):
            single_number([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
