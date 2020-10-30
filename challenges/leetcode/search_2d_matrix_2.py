"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for
 a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
import unittest


def search_2d_matrix_2(matrix, target):
    if len(matrix) <= 0 or len(matrix[0]) <= 0:
        return False

    j = len(matrix[0]) - 1
    i = 0
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == target:
            return True

        if matrix[i][j] < target:
            i += 1
            continue

        if matrix[i][j] > target:
            j -= 1
            continue

    return False


class TestSearch2DMatrix(unittest.TestCase):
    def test_search_2d_matrix_2_empty(self):
        self.assertEqual(False, search_2d_matrix_2([], 2))

    def test_search_2d_matrix_2_leetcode1(self):
        matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        self.assertEqual(True, search_2d_matrix_2(matrix, 5))

    def test_search_2d_matrix_2_leetcode2(self):
        matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        self.assertEqual(False, search_2d_matrix_2(matrix, 20))