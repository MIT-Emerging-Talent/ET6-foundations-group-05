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
    if not isinstance(x, int):
        raise TypeError("Input must be an integer.")
    assert -(2**31) <= x <= 2**31 - 1, "Input is outside the valid range."

    # Convert the input to a string and reverse it to handle various types consistently.
    # Return whether the original and reversed strings match
    return str(x) == str(x)[::-1]
