# python3
# coding
"""creating on 01 03 2025
@author Geehan Ali + ChatGPT(phind)"""

from typing import Union


def subtract_two_numbers(
    num1: Union[int, float], num2: Union[int, float]
) -> Union[int, float]:
    """
    Module for subtract two numbers and return the difference.

    Args:
        num1 (Union[int, float]): The first number to subtract.
        num2 (Union[int, float]): The second number to subtract.

    Returns:
        Union[int, float]: The difference between num1 and num2.

    Examples:
        >>> subtract_two_numbers(5, 4)
        1
        >>> subtract_two_numbers(10, 2.5)
        7.5
        >>> subtract_two_numbers(-10, 10)
        -20
        >>> subtract_two_numbers(-12.5, -4)
        -8.5
        >>> subtract_two_numbers(-5.5, 2)
        -7.5
        >>> subtract_two_numbers(-5.5, -4.5)
        -1

    Raises:
        TypeError: If either num1 or num2 is not a number (int or float).

    """
    assert isinstance(
        num1, (int, float)
    ), "First argument must be a number (int or float)"
    assert isinstance(
        num2, (int, float)
    ), "Second argument must be a number (int or float)"

    return num1 - num2
