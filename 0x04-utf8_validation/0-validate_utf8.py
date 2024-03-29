#!/usr/bin/python3
"""validUTF8 Module"""


def validUTF8(data):
    """Determines if a given data set represents
    a valid UTF-8 Encoding"""
    i = 0

    while i < len(data):
        if not (0 <= data[i] <= 255):
            return False
        leading_bits = bin(data[i])[2:].zfill(8)[:4]
        if leading_bits == '1110':
            if i + 2 >= len(data) or any(byte < 128 or byte > 191
                                         for byte in data[i + 1:i + 3]):
                return False
            i += 3
        elif leading_bits == '110':
            if i + 1 >= len(data) or data[i + 1] < 128 or data[i + 1] > 191:
                return False
            i += 2
        elif leading_bits == '10':
            return False  # Unexpected leading byte
        else:
            i += 1
    return True
