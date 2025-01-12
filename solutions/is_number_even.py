#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Even Number Checker
=============================
This script provides a function to check if a number is even or not.

Module contents:
is_number_even: Checks if a given number is an even number or not.

@author Geehan Ali
Created on: 01-08-2025
"""


def is_number_even(number: int) -> bool:
    """
    Check if a number is even.

    Arguments:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.

    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    # Input validation
    assert isinstance(number, int), "Input must be an integer."

    # Return the result of the check
    # Is the remainder of dividing the number by 2 equal to 0?"
    return number % 2 == 0
