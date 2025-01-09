# python3
# coding
"""
Test module for subtract_two_numbers
creating on 01 03 2025
@author Geehan Ali + ChatGPT_phind
"""

import unittest

from ..subtract_two_numbers import subtract_two_numbers  # type: ignore


class TestSubtractTwoNumbers(unittest.TestCase):
    """Test suite for subtract_two_numbers function"""

    def test_normal_subtraction(self):
        """Test normal subtraction of two numbers."""
        self.assertEqual(subtract_two_numbers(5, 3), 2)


def test_different_types(self):
    """Test normal subtraction of two numbers."""
    self.assertEqual(subtract_two_numbers(5.5, 3), 2.5)


def test_edge_case_zero(self):
    """Test subtraction with zero as one operand."""
    self.assertEqual(subtract_two_numbers(10, 0), 10)


def test_edge_case_max_value(self):
    """Test subtraction with maximum integer value."""
    self.assertEqual(subtract_two_numbers(2147483647, 1), 2147483646)


def test_edge_case_min_value(self):
    """Test subtraction with minimum integer value."""
    self.assertEqual(subtract_two_numbers(-2147483648, -1), -2147483647)


def test_float_and_large_numbers(self):
    """Test subtraction with floating-point numbers and large integers."""
    self.assertAlmostEqual(subtract_two_numbers(0.001, 0.0009), 0.00010000000000000005)


def test_defensive_case_non_numeric_input(self):
    """Test handling of non-numeric input."""
    with self.assertRaises(AssertionError):
        subtract_two_numbers("a", 5)


def test_defensive_case_invalid_type_input(self):
    """Test handling of invalid input type."""
    with self.assertRaises(AssertionError):
        subtract_two_numbers([10], 20)


if __name__ == "__main__":
    unittest.main()
