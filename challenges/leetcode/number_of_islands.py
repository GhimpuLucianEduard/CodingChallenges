"""
200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
import unittest


def number_of_islands(grid):
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                clear_cell(grid, i, j)
                islands += 1

    return islands


def clear_cell(matrix, i, j):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == "0":
        return

    matrix[i][j] = "0"
    clear_cell(matrix, i, j + 1)
    clear_cell(matrix, i + 1, j)
    clear_cell(matrix, i - 1, j)
    clear_cell(matrix, i, j - 1)


class TestNumberOfIslands(unittest.TestCase):
    def test_number_of_islands_leetcode1(self):
        self.assertEqual(1, number_of_islands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]))

    def test_number_of_islands_leetcode2(self):
        self.assertEqual(3, number_of_islands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]))

    def test_number_of_islands_leetcode3(self):
        self.assertEqual(1, number_of_islands([
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"]
        ]))
