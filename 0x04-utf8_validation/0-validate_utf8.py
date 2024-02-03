#!/usr/bin/python3
"""validUTF8 Module"""


def validUTF8(data):
    """Determines if a given data set represents
    a valid UTF-8 Encoding"""
    i = 0

    while i < len(data):
        leading_bits = bin(data[i])[2:].zfill(8)[:4]
        if leading_bits == '1110':
            if i + 2 >= len(data) or any(bin(byte)[2:3] != '10'
                                         for byte in data[i + 1:i + 3]):
                return False
            i += 3
        elif leading_bits == '110':
            if i + 1 >= len(data) or bin(data[i + 1])[2:3] != '10':
                return False
            i += 2
        elif leading_bits == '10':
            return False
        else:
            i += 1
    return True
