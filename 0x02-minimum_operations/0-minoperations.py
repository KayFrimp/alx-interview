#!/usr/bin/python3
"""minOperations Module"""


def minOperations(n):
    """Kep track of and return the number of operations performed"""
    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
