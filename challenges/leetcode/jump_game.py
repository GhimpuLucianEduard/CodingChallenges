"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
"""

from collections import defaultdict
import unittest


def can_jump_dp(array):
    if len(array) == 0:
        return False

    visited = defaultdict(bool)
    visited[0] = True

    for i in range(1, len(array)):
        for j in range(0, i):
            if visited[i]:
                break
            if visited[j] and j + array[j] >= i:
                visited[i] = True

    return visited[len(array) - 1]


def can_jump_greedy(array):
    if len(array) == 0:
        return False

    max_index = 0

    for i in range(0, len(array) - 1):
        if i > max_index:
            break
        max_index = max(max_index, i + array[i])

    return max_index >= len(array) - 1


class TestJumpGame(unittest.TestCase):
    def test_jump_dp_game_empty(self):
        self.assertFalse(can_jump_dp([]))

    def test_jump_dp_game_single_false(self):
        self.assertTrue(can_jump_dp([4]))

    def test_jump_dp_game_single_true(self):
        self.assertTrue(can_jump_dp([0]))

    def test_jump_dp_game_single_leetcode1(self):
        self.assertTrue(can_jump_dp([2, 3, 1, 1, 4]))

    def test_jump_dp_game_single_leetcode2(self):
        self.assertFalse(can_jump_dp([3, 2, 1, 0, 4]))

    def test_jump_greedy_game_empty(self):
        self.assertFalse(can_jump_greedy([]))

    def test_jump_greedy_game_single_false(self):
        self.assertTrue(can_jump_greedy([4]))

    def test_jump_greedy_game_single_true(self):
        self.assertTrue(can_jump_greedy([0]))

    def test_jump_greedy_game_single_leetcode1(self):
        self.assertTrue(can_jump_greedy([2, 3, 1, 1, 4]))

    def test_jump_greedy_game_single_leetcode2(self):
        self.assertFalse(can_jump_greedy([3, 2, 1, 0, 4]))
