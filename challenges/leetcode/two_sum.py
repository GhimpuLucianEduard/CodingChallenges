"""
1. Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one
solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

import unittest
from collections import defaultdict


def two_sum(array, target):
    # use a map to keep track of the indexes
    element_dict = defaultdict(int)

    if len(array) < 2:
        return -1, -1

    for i in range(0, len(array)):
        # check for complement
        if target - array[i] in element_dict:
            return element_dict[target - array[i]], i

        element_dict[array[i]] = i

    return -1, -1


class TestTwoSum(unittest.TestCase):

    def test_two_sum_empty(self):
        self.assertEqual((-1, -1), two_sum([], 10))

    def test_two_sum_one_element(self):
        self.assertEqual((-1, -1), two_sum([2], 10))

    def test_two_sum_one_multiple_elements(self):
        self.assertEqual((0, 1), two_sum([2, 7, 15, 11], 9))

    def test_two_sum_one_multiple_duplicate(self):
        self.assertEqual((0, 2), two_sum([5, 7, 5, 11], 10))
