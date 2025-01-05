#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prime Number Checker Tests
=============================
This script contains unit tests for the prime number checker function using the unittest module.

Test categories:
    - Standard tests for known prime and non-prime numbers
    - Edge cases for smallest primes, non-primes, and large primes
    - Defensive tests for non-integer values and negative numbers

Author: Banu Ozyilmaz
Created on: 12-29-2024
"""

import unittest
from solutions.is_prime import is_prime


class TestPrimeNumberChecker(unittest.TestCase):
    """
    Unit tests for the prime number checker function
    """

    def test_is_prime_2(self):
        """Test that 2 is a prime number"""
        self.assertTrue(is_prime(2))

    def test_is_prime_3(self):
        """Test that 3 is a prime number"""
        self.assertTrue(is_prime(3))

    def test_is_not_prime_4(self):
        """Test that 4 is not a prime number"""
        self.assertFalse(is_prime(4))

    def test_is_not_prime_9(self):
        """Test that 9 is not a prime number"""
        self.assertFalse(is_prime(9))

    def test_is_prime_11(self):
        """Test that 11 is a prime number"""
        self.assertTrue(is_prime(11))

    # Edge cases
    def test_is_not_prime_0(self):
        """Test that 0 is not a prime number"""
        self.assertFalse(is_prime(0))

    def test_is_not_prime_1(self):
        """Test that 1 is not a prime number"""
        self.assertFalse(is_prime(1))

    def test_is_prime_7919(self):
        """Test that 7919 is a prime number"""
        self.assertTrue(is_prime(7919))

    def test_is_prime_104729(self):
        """Test that 104729 is a prime number"""
        self.assertTrue(is_prime(104729))

    # Defensive tests
    def test_non_integer_input_float(self):
        """Test that a float raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_prime(2.5)

    def test_non_integer_input_string(self):
        """Test that a string raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_prime("string")

    def test_none_input(self):
        """Test that None raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_prime(None)

    def test_negative_number(self):
        """Test that a negative number raises an AssertionError"""
        with self.assertRaises(AssertionError):
            is_prime(-10)


if __name__ == "__main__":
    unittest.main()
