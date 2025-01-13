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

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        O(n): The function traverses the list once, where n is the length of the list.

    Space Complexity:
        O(1): The function uses a constant amount of extra space.

    Example:
        >>> single_number([2, 2, 1])
        1
        >>> single_number([4, 1, 2, 1, 2])
        4
        >>> single_number([1])
        1
    """
    if not nums:
        raise ValueError("Input list cannot be empty")

    uniq_num = 0
    for idx in nums:
        uniq_num ^= idx

    return uniq_num
