"""
62. Unique Paths

A robot is located at the top-left corner
of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of
the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6

Constraints

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
"""
import unittest
from collections import defaultdict


def unique_paths(m, n):
    visited = defaultdict(int)

    for i in range(1, m + 1, 1):
        for j in range(1, n + 1, 1):
            if i == 1 or j == 1:
                visited[(i, j)] = 1
                continue

            if not visited[(i, j)]:
                visited[(i, j)] = visited[(i, j - 1)] + visited[(i - 1, j)]

    return visited[(m, n)]


class TestUniquePaths(unittest.TestCase):
    def test_unique_paths_leetcode1(self):
        self.assertEqual(28, unique_paths(3, 7))

    def test_unique_paths_leetcode2(self):
        self.assertEqual(6, unique_paths(3, 3))
