from helper.custom_exceptions import *
import re

def transforming_part(part):
    if sum(int(digit) ** 3 for digit in part) % 2 == 0:
        return part[::-1]
    else:
        return part[1:] + part[0]


def transform_string(str, n):
    if n <= 0:
        raise NonPositiveIntegerException()
    elif n > len(str):
        raise StringBufferOverflowException()

    parts = [str[i:i+n] for i in range(0, len(str), n) if len(str[i:i+n]) == n]
    return ''.join(transforming_part(part) for part in parts)
