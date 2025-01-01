#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for checking if an integer is a palindrome.

Module contents:
    - is_palindrome: determines whether a given integer is a palindrome.

Created on XX XX XX
@author: Muhammet Isik
"""


def is_palindrome(x: int) -> bool:
    """Determines if an integer is a palindrome.

    An integer is a palindrome if it reads the same backward as forward.

    Parameters:
        x (int): An integer within the range [-2**31, 2**31 - 1].

    Returns:
        bool: True if the integer is a palindrome, False otherwise.

    Raises:
        AssertionError: if the argument is not an integer.
        AssertionError: if the argument is outside the valid range.

    >>> is_palindrome(121)
    True.

    >>> is_palindrome(-121)
    False

    >>> is_palindrome(10)
    False
    >>> is_palindrome(0)s
    True
    """
    # Defensive assertions
    assert isinstance(x, int), "Input must be an integer."
    assert -(2**31) <= x <= 2**31 - 1, "Input is outside the valid range."

    # Use string reversal to check palindrome status
    rev = str(x)[::-1]
    return str(x) == rev
