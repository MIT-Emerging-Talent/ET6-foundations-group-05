#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the length of the longest substring without repeating characters.

Module contents:
    - longest_substring(s): Function to determine the length of the longest substring without repeating characters.

Created on 2025-01-07
@author: Gennadii Ershov
"""


def longest_substring(s: str) -> int:
    """
    Determines the length of the longest substring without repeating characters.

    Args:
        s (str): The input string to be evaluated. Must have a length between 0 and 5 * 10^4.
                 The string consists of English letters, digits, symbols, and spaces.

    Returns:
        int: The length of the longest substring without repeating characters. Returns 0 if the input string is empty.

    Raises:
        AssertionError: If the input is not a string.
        AssertionError: If the input string length is not within the valid range (0 <= len(s) <= 5 * 10^4).


    >>> longest_substring("abcabcbb")
    3
    >>> longest_substring("bbbbb")
    1
    >>> longest_substring("pwwkew")
    3
    >>> longest_substring("")
    0
    """

    # Assert that the input is a string
    assert isinstance(s, str), "Given input must be a string."

    # Assert that the string length is within the allowed limit
    assert (
        0 <= len(s) <= 5 * 10**4
    ), "Input string length must be between 0 and 50,000 characters."

    # Use a sliding window strategy to track unique characters in the current substring
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If a duplicate character is found, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set and update the maximum length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
