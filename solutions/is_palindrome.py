#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if an integer is a palindrome.

Module contents:
    - is_palindrome: Determines whether a given integer is a palindrome.

Created on 12 31 2024
@author: Muhammet Isik
"""


def is_palindrome(x: int) -> bool:
    """
    Checks if an integer is a palindrome.

    An integer is a palindrome if it reads the same backward as forward.

    Parameters:
        x (int): An integer in the range [-2**31, 2**31 - 1].

    Returns:
        bool: True if the integer is a palindrome, False otherwise.

    Raises:
        AssertionError: If the input is not an integer or out of range.

    Examples:
        >>> is_palindrome(121)
        True

        >>> is_palindrome(-121)
        False

        >>> is_palindrome(10)
        False

        >>> is_palindrome(0)
        True

        >>> is_palindrome(12321)
        True
    """
    # Defensive assertions
    assert isinstance(x, int), "Input must be an integer."
    assert -(2**31) <= x <= 2**31 - 1, "Input is outside the valid range."

    # Convert the integer to its string representation
    original_str = str(x)

    # Reverse the string and compare it to the original
    reversed_str = original_str[::-1]

    # Return whether the original and reversed strings match
    return original_str == reversed_str
