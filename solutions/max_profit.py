#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the maximum profit from stock prices.

Module contents:
    - max_profit: calculates the maximum profit from a list of stock prices
    with one buy and one sell transaction. We can not sell before buying.

Created on 12 28 2024
@author: Muhammet Isik
"""


def max_profit(prices: list[int]) -> int:
    """Calculates the maximum profit from a list of stock prices.

    The function determines the maximum profit that can be achieved by buying
    and selling a stock once. It ensures that the selling day is after the
    buying day.

    Parameters:
        prices: list[int], a list of integers representing stock prices on
        different days.

    Returns -> int:
        prices (list[int]): A list of integers representing stock prices on
        different days. Each value corresponds to the price of a stock on a
        specific day, and the list is ordered chronologically (e.g., day 1,
        day 2, day 3, etc.).

        Constraints:
        - The `prices` list must contain only integers.
        - Each integer in the list represents a non-negative stock price (prices
        cannot be negative).
        - The list must have at least two elements to calculate a profit. If the
        list has fewer than two elements, the function assumes no transaction
        is possible.

    Raises:
        AssertionError: if the input is not a list
        AssertionError: if the list contains non-integer elements

    Examples:
    >>> max_profit([7, 2, 5, 3, 7, 4, 1, 10])
    9

    >>> max_profit([10, 9, 8, 7, 6, 5])
    0  # No profit possible as prices decrease every day

    >>> max_profit([3, 3, 3, 3, 3])
    0  # No profit possible as prices stay the same
    """
    # Check input validity, Input must be a integer list
    assert isinstance(prices, list), "Input must be a list"

    for price in prices:
        assert isinstance(price, int), "Every single List element must be an integer"

    buy_day = 0
    sell_day = 1
    max_profit_value = 0  # Initialize maximum profit

    # Loop through the list to calculate profit
    while sell_day < len(prices):
        current_profit = (
            prices[sell_day] - prices[buy_day]
        )  # Current profit calculation
        if prices[buy_day] < prices[sell_day]:
            # Update max profit if better profit found
            max_profit_value = max(current_profit, max_profit_value)
        else:
            buy_day = sell_day  # Update buy day if current price is lower
        sell_day += 1  # Move to the next sell day

    return max_profit_value
