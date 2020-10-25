"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""
import unittest
from collections import defaultdict


def climbing_stairs(n):
    visited = defaultdict(int)
    visited[1] = 1
    visited[2] = 2
    return climbing_stairs_aux(n, visited)


def climbing_stairs_aux(n, visited):
    if n in visited.keys():
        return visited[n]

    visited[n] = climbing_stairs_aux(n - 1, visited) + climbing_stairs_aux(n - 2, visited)
    return visited[n]


class TestClimbingStairs(unittest.TestCase):
    def test_climbing_stairs_1(self):
        self.assertEqual(climbing_stairs(1), 1)

    def test_climbing_stairs_2(self):
        self.assertEqual(climbing_stairs(2), 2)

    def test_climbing_stairs_3(self):
        self.assertEqual(climbing_stairs(3), 3)

    def test_climbing_stairs_4(self):
        self.assertEqual(climbing_stairs(4), 5)

    def test_climbing_stairs_3(self):
        self.assertEqual(climbing_stairs(5), 8)
