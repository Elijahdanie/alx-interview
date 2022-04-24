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
    track_operations = 0
    max_operations = 2
    while n > 1:
        while n % max_operations == 0:
            track_operations += max_operations
            n /= max_operations
        max_operations += 1
    return track_operations

print(minOperations(19170307))