"""
Longest Increasing Subsequence

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

from collections import defaultdict
import unittest


def longest_inc_sub(array):
    if len(array) == 0:
        return 0

    sizes = defaultdict(int)

    for i in range(0, len(array)):
        sizes[i] = 1
        for j in range(0, i):
            if array[j] < array[i]:
                sizes[i] = max(sizes[j] + 1, sizes[i])

    return max(sizes.values())


class TestLongestIncSub(unittest.TestCase):

    def test_longest_inc_sub_empty(self):
        self.assertEqual(longest_inc_sub([]), 0)

    def test_longest_inc_sub_single(self):
        self.assertEqual(longest_inc_sub([1]), 1)

    def test_longest_inc_sub_leetcode_1(self):
        self.assertEqual(longest_inc_sub([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_longest_inc_sub_leetcode_2(self):
        self.assertEqual(longest_inc_sub([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6)
