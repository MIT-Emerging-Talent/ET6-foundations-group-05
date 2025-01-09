#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a utility function for basic arithmetic operations.

Functions:
    adding_two_integers(num1: int, num2: int) -> int:
        Calculates the adding_two_integers of two integers.

Example:
    To use the `adding_two_integers` function:

    >>> result = adding_two_integers(5, 7)
    >>> print(result)
    12
"""


def adding_two_integers(num1: int, num2: int) -> int:
    """
    Calculates the sum of two integers.

    Args:
        num1 (int): The first integer to be added.
        num2 (int): The second integer to be added.

    Returns:
        int: The sum of num1 and num2.

    Raises:
        TypeError: If either of the inputs is not an integer.
    """
    # Check if inputs are integers
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Inputs must be integers.")

    # Return the sum
    return num1 + num2
