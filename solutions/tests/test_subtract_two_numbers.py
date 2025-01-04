# python3
# coding
"""
Test module for subtract_two_numbers
creating on 01 03 2025
@author Geehan Ali + ChatGPT_phind

"""

import unittest

from ..subtract_two_numbers import subtract_two_numbers


class TestSubtractTwoNumbers(unittest.TestCase):
    """Test suit to subtract_two_numbers function"""

    def test_subtract_two_numbers_positive_int(self):
        self.assertEqual(subtract_two_numbers(5, 4), 1)

    def test_Subtract_Two_Numbers_int_float(self):
        self.assertEqual(subtract_two_numbers(10, 2.5), 7.5)

    def test_Subtract_Two_Numbers_negative_int_(self):
        self.assertEqual(subtract_two_numbers(-10, -10), 0)

    def test_Subtract_Two_Numbers_negative_mixed_types(self):
        self.assertEqual(subtract_two_numbers(-12.5, -4), -8.5)

    def test_Subtract_Two_Numbers_Negative_folat_int(self):
        self.assertEqual(subtract_two_numbers(-5.5, 2), -7.5)

    def test_Subtract_Two_Numbers_float_negative(self):
        self.assertEqual(subtract_two_numbers(-5.5, -4.5), -1)

    def test_Subtract_Two_Numbers_large_numbers(self):
        self.assertEqual(subtract_two_numbers(1000000, 500000), 500000)

    def test_Subtract_Two_Numbers_small_numbers(self):
        self.assertEqual(subtract_two_numbers(0.001, 0.0009), 0.00010000000000000005)

    def test_Subtract_Two_Numbers_zero(self):
        self.assertEqual(subtract_two_numbers(10, 0), 10)

    def test_Subtract_Two_Numbers_max_value(self):
        self.assertEqual(subtract_two_numbers(2147483647, 1), 2147483646)

    def test_Subtract_Two_Numbers_min_value(self):
        self.assertEqual(subtract_two_numbers(-2147483648, -1), -2147483647)

    def test_Subtract_Two_Numbers_non_numeric_second(self):
        with self.assertRaises(AssertionError):
            subtract_two_numbers(5, "a")

    def test_Subtract_Two_Numbers_non_numeric_first(self):
        with self.assertRaises(AssertionError):
            subtract_two_numbers("5", 2.5)

    def test_Subtract_Two_Numbers_two_non_numeric_both(self):
        with self.assertRaises(AssertionError):
            subtract_two_numbers("5", "2.5")


if __name__ == "__main__":
    unittest.main()
