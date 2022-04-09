#!/usr/bin/python3
"""
    This module computes the pascal triangle
    for a certain number
"""


def pascal_triangle(n):
    """
    This function prints out the pascal triangle
    of the number n
        Args:
            n: this is the number of elements in the triangle array
    """
    finalarray = []
    for i in range(n):
        if i < n:
            length = len(finalarray)
            previous = finalarray[length - 1] if length > 0 else []
            prev_len = len(previous)
            newarray = []
            newarray.append(1)
            for x in range(prev_len):
                if x < prev_len - 1:
                    val = previous[x] + previous[x + 1]
                    newarray.append(val)
                else:
                     newarray.append(1)
            finalarray.append(newarray)
    return finalarray
