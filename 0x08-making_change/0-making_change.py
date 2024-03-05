#!/usr/bin/python3
"""Making change Module"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet
    a given amount total"""
    if total <= 0:
        return 0

    table = [0] + [float('inf')] * total

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                table[i] = min(table[i], table[i - coin] + 1)

    return table[total] if table[total] != float('inf') else -1
