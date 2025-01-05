#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Factorial Calculation Script
=============================
This script contains a function to calculate the factorial of a non-negative integer
using recursion.

Module contents:
    - factorial: Calculates the factorial of a given non-negative integer.

Author: Banu Ozyilmaz
Created on: 12-28-2024
"""


def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer using recursion.

    Arguments:
        n (int): A non-negative integer whose factorial is to be calculated.
                 Recommended to use values no more than 100 to avoid recursion limit
                 and memory issues.

    Returns:
        int: The factorial of the given number.

    Raises:
        AssertionError: If `n` is not an integer.
        AssertionError: If `n` is negative.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(4)
        24
        >>> factorial(5)
        120
        >>> factorial(6)
        720
        >>> factorial(-1)
        Traceback (most recent call last):
        ...
        AssertionError: The argument must be a non-negative integer.
        >>> factorial(3.5)
        Traceback (most recent call last):
        ...
        AssertionError: The argument should be an integer.

    """
    # Input validation
    assert isinstance(n, int), "The argument should be an integer."
    assert n >= 0, "The argument must be a non-negative integer."

    # Base Case
    if n == 0:
        result = 1

    else:
        # Break Down: Reduce the problem size by one
        smaller_factorial = factorial(n - 1)
        # Recursive Case: Use the result of the smaller problem
        # Build Up: Combine the current value with the smaller problem result
        result = n * smaller_factorial

    return result
