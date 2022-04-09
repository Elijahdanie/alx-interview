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
    if n == 1:
        finalarray.append([1])
        return finalarray
    if n == 2:
        finalarray.append([1])
        finalarray.append([1,1])
        return finalarray
    if n > 2:
        finalarray.append([1])
        finalarray.append([1,1])
    for j in range(n):
        i = j + 2
        if i < n:
            length = len(finalarray)
            previous = finalarray[length - 1]
            prev_len = len(previous)
            newarray = []
            newarray.append(1)
            for x in range(prev_len):
                if x < prev_len - 1:
                    val = previous[x] + previous[x + 1]
                    newarray.append(val)
            newarray.append(1)
            finalarray.append(newarray)
    return finalarray
