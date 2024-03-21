#!/usr/bin/python3
"""method that calculates the fewest number of operations """


def minOperatons(n):
    """method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return n
