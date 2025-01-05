#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prime Number Checker
=============================
This script provides a function to check if a number is a prime number or not.

Module contents:
    - is_prime: Checks if a given number is a prime number.

Author: Banu Ozyilmaz
Created on: 12-29-2024
"""


def is_prime(n: int) -> bool:
    """
    Check if a number is a prime number.

    Arguments:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.

    Raises:
        AssertionError: If n is not an integer.
        AssertionError: If n is a negative number.

    Examples:
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(18005)
        False
        >>> is_prime(-6)
        Traceback (most recent call last):
            ...
        AssertionError: Input must be a non-negative integer.
        >>> is_prime(5.5)
        Traceback (most recent call last):
            ...
        AssertionError: Input must be an integer.
    """
    # Input validation
    assert isinstance(n, int), "Input must be an integer."
    assert n >= 0, "Input must be a non-negative integer."

    # Prime numbers are greater than 1
    if n <= 1:
        return False

    # Check for factors from 2 up to the square root of n
    # If n has a factor smaller than its square root,
    # it must also have a larger one,therefore n can't be prime.
    sqrt_limit = int(n**0.5) + 1
    for i in range(2, sqrt_limit):
        if n % i == 0:
            # If n is divisible by any number in this range, it is not prime
            return False
    # If no factors are found, n is prime
    return True
