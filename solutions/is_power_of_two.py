#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a given integer is a power of two.

Module contents:
    - is_power_of_two(n): Function to determine if `n` is a power of two.

Created on 2024-12-31
@author: Gennadii Ershov
"""


def is_power_of_two(n: int) -> bool:
    """
    Determines whether a given integer is a power of two.

    Parameters:
        n: int
            An integer to check if it is a power of two.
            Must satisfy the constraint: -2^31 <= n <= 2^31 - 1.

    Returns -> bool:
        True if the input is a power of two, False otherwise.

    Raises:
        AssertionError: if the input is not an integer or a float.
        AssertionError: If the input number is not within the valid range (-2^31 <= n <= 2^31 - 1).

    >>> is_power_of_two(1)
    True

    >>> is_power_of_two(16)
    True

    >>> is_power_of_two(3)
    False
    """

    # The input number should be an integer
    assert isinstance(n, (int, float)), "Given number must be an integer or a float"

    # The input number should be within the valid range constraint: -2^31 <= n <= 2^31 - 1
    assert (
        -(2**31) <= n <= 2**31 - 1
    ), f"Input must satisfy -2^31 <= n <= 2^31 - 1, but got {n}"

    # Negative numbers and 0 cannot be powers of two
    if n <= 0:
        return False

    # Odd numbers (except 1) are not powers of two
    if n % 2 != 0 and n != 1:
        return False

    # Use a loop to check for powers of two
    power = 1
    while power < n:
        power *= 2
    return power == n
