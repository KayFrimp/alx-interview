#!/usr/bin/python3
"""Making change Module"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            min_coins[x] = min(min_coins[x], min_coins[x - coin] + 1)

    return -1 if min_coins[total] == float('inf') else min_coins[total]
