#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for subtracting two integers.

Module contents:
    - subtract_two_numbers: Subtracts two integers and returns their difference.

Created on 2025-01-01
Author: Geehan Ali
"""


def subtract_two_numbers(a: int, b: int) -> int:
    """
    Subtracts two integers and returns their difference.

    Parameters:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The difference between a and b.

    Raises:
        TypeError: If either a or b is not an integer.

    Examples:
        >>> subtract_two_numbers(10, 3)
        7
        >>> subtract_two_numbers(-5, 5)
        -10
        >>> subtract_two_numbers(0, -5)
        5
        >>> subtract_two_numbers(100, 0)
        100
        >>> subtract_two_numbers(-10, -20)
        10
    """
    # Ensure inputs are integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

    # Return the subtraction result
    return a - b
