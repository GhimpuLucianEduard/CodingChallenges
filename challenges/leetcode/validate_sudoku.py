"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled
cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner
being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
import unittest
from collections import defaultdict


def valid_sudoku(board):
    visited = defaultdict(bool)

    for row in board:
        if not validate_array(row, visited):
            return False

    for col in range(9):
        if not validate_col(col, board, visited):
            return False

    square = []
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square.clear()
            for k in (0, 1, 2):
                for q in (0, 1, 2):
                    square.append(board[i + k][j + q])
            if not validate_array(square, visited):
                return False
    return True


def validate_array(array, visited):
    visited.clear()
    for num in array:
        if visited[num] and num != '.':
            return False

        visited[num] = True

    return True


def validate_col(col, board, visited):
    visited.clear()
    for row in range(9):
        if visited[board[row][col]] and board[row][col] != '.':
            return False

        visited[board[row][col]] = True

    return True


class TestValidateSudoku(unittest.TestCase):
    def test_valid_sudoku_leetcode1(self):
        self.assertEqual(True, valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    def test_valid_sudoku_leetcode2(self):
        self.assertEqual(False, valid_sudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                                 , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                                 , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                                 , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                                 , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                                 , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                                 , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                                 , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                                 , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
