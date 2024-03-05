#!/usr/bin/python3
"""Making change Module"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    remaining_total = total
    coins_used = 0

    for coin in sorted_coins:
        while remaining_total >= coin:
            remaining_total -= coin
            coins_used += 1

    if remaining_total > 0:
        return -1

    return coins_used
