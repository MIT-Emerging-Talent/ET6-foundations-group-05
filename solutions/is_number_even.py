#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Even Number Checker
=============================
This module provides functionality to check whether a given number is even.
Features include:

@author Geehan Ali
Created on: 01-08-2025
"""


def is_number_even(number: int) -> bool:
    """
    Check if a given number is an even number or not.

    Arguments:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.

        Raises:
        AssertionError: If the input is not an integer.
        AssertionError: If the input is string.
        AssertionError: If the input is None.
    Examples:
        >>> is_number_even(4)
        True
        >>> is_number_even(7)
        False
        >>> is_number_even(-3)
        False
    """
    # Input validation
    assert isinstance(number, int), "Input must be an integer."

    # Return the result of the check
    # Is the remainder of dividing the number by 2 equal to 0?"
    return number % 2 == 0
