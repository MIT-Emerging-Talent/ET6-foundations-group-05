#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module: single_number_solver

This module provides a utility function to solve the problem
of finding a single number
in a list where every element appears exactly twice except for one
element that appears only once.


Created on 2024-01-11
@author: Abbiihjah Oyeoku
"""


def single_number(nums):
    """
    Finds the single number in a list where every element appears twice except for one.

    This function uses the XOR operation to efficiently determine the unique number
    that appears only once in the input list. The XOR operation ensures that numbers
    appearing in pairs cancel each other out, leaving the single number.

    Args:
        nums (List[int]): A list of integers where all elements appear exactly twice
                        except for one element that appears only once.

    Returns:
        int: The integer that appears only once in the input list.

    Example:
        >>> single_number([2, 2, 1])
        1
        >>> single_number([4, 1, 2, 1, 2])
        4
        >>> single_number([1])
        1
    """
    if not nums:  # Check if the list is empty
        raise ValueError("Input list cannot be empty")
    # Initialize the unique number...
    uniq_num = 0
    # TRaverse all elements through the loop...
    for idx in nums:
        # Concept of XOR...
        uniq_num ^= idx
    return uniq_num  # Return the unique number...
