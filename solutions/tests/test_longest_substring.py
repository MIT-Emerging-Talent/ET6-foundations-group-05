#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the longest_substring function.

Test categories:
    - Standard cases: Validates typical inputs with varying patterns of repeating and unique characters.
    - Performance tests: Verifies that the function handles large inputs efficiently and performs within acceptable time limits.
    - Edge cases: Covers unusual scenarios, including boundary cases.
    - Defensive tests: Ensures the function raises appropriate errors for invalid input types and out-of-range values.

Created on 2025-01-07
@author: Gennadii Ershov
"""

import unittest

from ..longest_substring import longest_substring


class TestLongestSubstring(unittest.TestCase):
    """Test the longest_substring function"""

    # Standard test cases
    def test_case_1(self):
        """Test with input 'abcabcbb', expecting output 3."""
        self.assertEqual(longest_substring("abcabcbb"), 3)

    def test_case_2(self):
        """Test with input 'bbbbb', expecting output 1."""
        self.assertEqual(longest_substring("bbbbb"), 1)

    def test_case_3(self):
        """Test with input 'pwwkew', expecting output 3."""
        self.assertEqual(longest_substring("pwwkew"), 3)

    def test_all_unique_characters(self):
        """Test with all unique characters, expecting output equal to string length."""
        self.assertEqual(longest_substring("abcdef"), 6)

    def test_long_repeating_sequence(self):
        """Test with a long repeating sequence, expecting output 3."""
        self.assertEqual(longest_substring("aabcc"), 3)

    # Performance test
    def test_large_input(self):
        """Test with a long input string, expecting output equal to unique characters."""
        large_input = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
            * 10  # Repeating the pattern to make the string longer
        )
        expected_output = len(set(large_input))  # Unique characters in the input
        self.assertEqual(longest_substring(large_input), expected_output)

    # Edge cases
    def test_empty_string(self):
        """Test with an empty string, expecting output 0."""
        self.assertEqual(longest_substring(""), 0)

    def test_single_character(self):
        """Test with a single character string, expecting output 1."""
        self.assertEqual(longest_substring("a"), 1)

    def test_repeating_pattern(self):
        """Test with a long string that repeats a pattern, expecting output equal to pattern length."""
        repeating_pattern = (
            "abc" * 16666
        )  # Adjusted to keep length within 50,000 characters
        self.assertEqual(longest_substring(repeating_pattern), 3)

    def test_maximum_input_length_all_repeating(self):
        """Boundary test with the maximum input length (50,000 repeating characters), expecting output 1."""
        max_repeating_input = (
            "a" * 50000
        )  # Generate a string with 50,000 'a' characters
        self.assertEqual(longest_substring(max_repeating_input), 1)

    # Defensive tests
    def test_invalid_type_int(self):
        """Test if a int raises an AssertionError."""
        with self.assertRaises(AssertionError):
            longest_substring(12)

    def test_invalid_type_list(self):
        """Test if a list raises an AssertionError."""
        with self.assertRaises(AssertionError):
            longest_substring(["bjkbkj", "bjbj"])

    def test_invalid_type_none(self):
        """Test if a None raises an AssertionError."""
        with self.assertRaises(AssertionError):
            longest_substring(None)

    def test_out_of_range_input(self):
        """Test if a string exceeding the maximum allowed length raises an AssertionError."""
        long_input = "a" * (5 * 10**4 + 1)
        with self.assertRaises(AssertionError):
            longest_substring(long_input)
