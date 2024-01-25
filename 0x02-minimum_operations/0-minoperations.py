#!/usr/bin/python3
"""minOperations Module"""


def minOperations(n):
    """Keep track of and return the number of operations performed"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
