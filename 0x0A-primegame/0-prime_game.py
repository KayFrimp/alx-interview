#!/usr/bin/python3
"""Program that performs prime game"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    prime_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not prime_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            prime_filter[j] = False
    prime_filter[0] = prime_filter[1] = False
    c = 0
    for i in range(len(prime_filter)):
        if prime_filter[i]:
            c += 1
        prime_filter[i] = c
    marias_wins = 0
    for n in nums:
        marias_wins += prime_filter[n] % 2 == 1

    if marias_wins * 2 == len(nums):
        return None
    if marias_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
