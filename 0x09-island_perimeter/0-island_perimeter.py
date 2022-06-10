#!/usr/bin/python3

"""
This module computes the perimeter
of an island in a grid
"""


def island_perimeter(grid):
    """
    This function computes the perimeter
    of an island in a grid
    """
    if(grid == None):
        return
    c_p = 0
    len_grid = len(grid)
    for i in range(len_grid):
        row = grid[i]
        row_len = len(row)
        for cell in range(row_len):
            if row[cell] == 1:
                bool_map = []
                bool_map.append(cell - 1 < 0 or row[cell - 1] == 0)
                bool_map.append(cell + 1 > row_len - 1 or row[cell + 1] == 0)
                bool_map.append(i - 1 < 0 or grid[i - 1][cell] == 0)
                bool_map.append(i + 1 > len_grid - 1 or grid[i + 1][cell] == 0)
                for i in bool_map:
                    if i:
                        c_p += 1
    return c_p
