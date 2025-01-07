import unittest
from solutions import subtract_two_numbers

class TestSubtractTwoNumbers(unittest.TestCase):
    def test_normal_subtraction(self):
        """
        Test normal subtraction of two numbers.

        Verifies that subtracting 3 from 5 returns 2.
        """
        result = subtract_two_numbers(5, 3)
        self.assertEqual(result, 2)

    def test_subtraction_with_zero(self):
        """
        Test subtraction when zero is one of the operands.

        Verifies that subtracting 0 from 10 returns 10.
        """
        result = subtract_two_numbers(10, 0)
        self.assertEqual(result, 10)

    def test_subtraction_with_max_integer(self):
        """
        Test subtraction with the maximum integer value.

        Verifies that subtracting 1 from the maximum integer value works correctly.
        """
        result = subtract_two_numbers(2147483647, 1)
        self.assertEqual(result, 2147483646)

    def test_subtraction_with_min_integer(self):
        """
        Test subtraction with the minimum integer value.

        Verifies that subtracting -1 from the minimum integer value works correctly.
        """
        result = subtract_two_numbers(-2147483648, -1)
        self.assertEqual(result, -2147483647)

    def test_subtraction_with_floats(self):
        """
        Test subtraction with floating-point numbers.

        Verifies that subtracting 0.0009 from 0.001 returns the expected result.
        """
        result = subtract_two_numbers(0.001, 0.0009)
        self.assertAlmostEqual(result, 0.0001)

    def test_large_number_subtraction(self):
        """
        Test subtraction with very large numbers.

        Verifies that the function correctly handles subtraction involving large integers.
        """
        result = subtract_two_numbers(10**15, 10**14)
        self.assertEqual(result, 9 * 10**14)

    def test_non_numeric_input(self):
        """
        Test handling of non-numeric input.

        Verifies that the function raises a TypeError when given non-numeric input.
        """
        with self.assertRaises(TypeError):
            subtract_two_numbers("a", 5)

    def test_none_input(self):
        """
        Test handling of None input.

        Verifies that the function raises a TypeError when one of the inputs is None.
        """
        with self.assertRaises(TypeError):
            subtract_two_numbers(None, 5)

if __name__ == '__main__':
    unittest.main()
