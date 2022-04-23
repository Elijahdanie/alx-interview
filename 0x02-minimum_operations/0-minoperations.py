#!/usr/bin/python3

"""
This module computes the minum operation
takes to paste letter H with a limitation
of taking action COPY ALL and PASTE
"""


def minOperations(n):
    """
    This returns the minimum operation to copy
    and paste n number of letters
    """
    if n <= 0:
        return 0
    arr = []
    iterator = int(n/2) if n > 10 else n
    for i in range(iterator):
        for j in range(iterator):
            if (i * j) == n:
                arr.append(i + j)
    if len(arr) != 0:
        arr.sort()
        return arr[0]
    else:
        return n
