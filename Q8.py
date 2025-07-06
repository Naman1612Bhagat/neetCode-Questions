# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # no. of rows[r] and columns[c] are 9 
        rows = defaultdict(set)
        cols = defaultdict(set)
        # no. of squares are 9 (3x3) in r//3, c//3
        # r//3 is the row index of the square
        # c//3 is the column index of the square
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                # if the number is already in the row, column, or square, return False
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                # if the number is not in the row, column, or square, add it to the row, column, and square
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # the square is a tuple of the row and column divided by 3
                squares[(r//3, c//3)].add(board[r][c])
        return True
    