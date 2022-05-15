#!/usr/bin/env python3

import sys
from typing import List

data = sys.argv[1]

diagAxis = set()
negDiag = set()
columns = set()
board = []

def validateCell(cell):
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
    for i in range(n):
        if rowindex == 0:
            validateCell(row[startPos])
            return row[startPos]
        if validateCell(row[i]):
            return row[i]


def solve(n: int, solutions: List[List[int]], startPos: int):
    result = []
    for i in range(n):
        t = placeQueen(board[i], n, i, startPos)
        if t is not None:
            result.append([t[1], t[0]])
    if len(result) == n:
        solutions.append(result)
    negDiag.clear()
    diagAxis.clear()
    columns.clear()
    if startPos < n - 1:
        return solve(n, solutions, startPos + 1)
    else:
        return solutions

if __name__ == '__main__':
    n = int(data)
    if type(n) is not int:
        print('Error: Input must be an integer')
        exit(1)
    if n < 4:
        print('Error: Input must be at least 4')
        exit(1)
    for r in range(n):
        row = []
        for c in range(n):
            row.append([r, c])
        board.append(row)
    final = solve(n, [], 0)
    [print(i) for i in final]