import unittest

from ..subtract_two_numbers import subtract_two_numbers


class TestSubtractTwoNumbers(unittest.TestCase):
    def test_normal_subtraction(self):
        """Test normal subtraction of two numbers."""
        result = subtract_two_numbers(5, 3)
        self.assertEqual(result, 2)

    def test_subtraction_with_zero(self):
        """Test subtraction when zero is one of the operands."""
        result = subtract_two_numbers(10, 0)
        self.assertEqual(result, 10)

    def test_subtraction_with_max_integer(self):
        """Test subtraction with the maximum integer value."""
        result = subtract_two_numbers(2147483647, 1)
        self.assertEqual(result, 2147483646)

    def test_subtraction_with_min_integer(self):
        """Test subtraction with the minimum integer value."""
        result = subtract_two_numbers(-2147483648, -1)
        self.assertEqual(result, -2147483647)

    def test_subtraction_with_floats(self):
        """Test subtraction with floating-point numbers."""
        result = subtract_two_numbers(0.001, 0.0009)
        self.assertAlmostEqual(result, 0.0001)

    def test_non_numeric_input(self):
        """Test handling of non-numeric input."""
        with self.assertRaises(TypeError):
            subtract_two_numbers("a", 5)

    def test_none_input(self):
        """Test handling of None input."""
        with self.assertRaises(TypeError):
            subtract_two_numbers(None, 5)


if __name__ == "__main__":
    unittest.main()
