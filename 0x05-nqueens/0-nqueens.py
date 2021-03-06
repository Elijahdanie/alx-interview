#!/usr/bin/python3

"""
This module demonstrates
solution to Nqueens problem
"""

import sys

diagAxis = set()
negDiag = set()
columns = set()
board = []


def validateCell(cell):
    """
    This function checks to see
    if cell lies in any of the axis
    """
    if cell[1] in columns:
        return False
    if (cell[0] - cell[1]) in diagAxis:
        return False
    if (cell[1] + cell[0]) in negDiag:
        return False
    negDiag.add(cell[0] + cell[1])
    diagAxis.add(cell[0] - cell[1])
    columns.add(cell[1])
    return True


def placeQueen(row, n, rowindex, startPos):
    """
    This function places a queen at
    a position in a row
    """
    for i in range(n):
        if rowindex == 0:
            validateCell(row[startPos])
            return row[startPos]
        if validateCell(row[i]):
            return row[i]


def solve(n: int, solutions, startPos: int):
    """
    This function solves the Nqueens problem
    by backtracking
    """
    if startPos == n:
        return solutions
    result = []
    for i in range(n):
        t = placeQueen(board[i], n, i, startPos)
        if t is not None:
            result.append(t)
    if len(result) == n:
        solutions.append(result)
    negDiag.clear()
    diagAxis.clear()
    columns.clear()
    if startPos < n:
        return solve(n, solutions, startPos + 1)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        data = sys.argv[1]
        n = int(data)
        if n < 4:
            print('N must be at least 4')
            exit(1)
        for r in range(n):
            row = []
            for c in range(n):
                row.append([r, c])
            board.append(row)
        final = solve(n, [], 0)
        [print(i) for i in final]
    except ValueError:
        print("N must be a number")
        exit(1)
