#!/usr/bin/env python3

"""
This module rotates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    This function rotates a 2d matrix
    """
    rotated_matrix = []
    len_matrix = len(matrix)
    column_step = 0
    while column_step < len_matrix:
        c_mat = []
        for row in matrix:
            c_mat.append(row[column_step])
            continue
        rotated_matrix.append(c_mat)
        column_step += 1
    for i in range(len_matrix):
        matrix[i] = rotated_matrix[i]
