# python3
# coding
"""creating on 01 03 2025
@author Geehan Ali + ChatGPT(phind)"""

from typing import Union


def subtract_two_numbers(
    a: Union[int, float], b: Union[int, float]
) -> Union[int, float]:
    """
    Subtract two numbers and return the difference.

    Args:
        a (Union[int, float]): The first number to subtract.
        b (Union[int, float]): The second number to subtract.

    Returns:
        Union[int, float]: The difference between a and b.

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
        TypeError: If either a or b is not a number (int or float).

    """
    assert isinstance(a, (int, float)), "First argument must be a number (int or float)"
    assert isinstance(
        b, (int, float)
    ), "Second argument must be a number (int or float)"

    return a - b
