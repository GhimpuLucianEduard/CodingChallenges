"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

"""
import unittest


def max_subarray(array):
    if len(array) == 1:
        return array[0]

    max_sum = array[0]
    cur_sum = array[0]

    for n in array[1:]:
        cur_sum = max(cur_sum + n, n)
        max_sum = max(cur_sum, max_sum)

    return max_sum


class TestMaxSubArray(unittest.TestCase):

    def test_max_subarray_single(self):
        self.assertEqual(max_subarray([1]), 1)

    def test_max_subarray_leetcode1(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_max_subarray_leetcode2(self):
        self.assertEqual(max_subarray([0]), 0)

    def test_max_subarray_leetcode3(self):
        self.assertEqual(max_subarray([-1]), -1)

    def test_max_subarray_leetcode4(self):
        self.assertEqual(max_subarray([-2147483647]), -2147483647)

    def test_max_subarray_leetcode5(self):
        self.assertEqual(max_subarray([1, 2]), 3)

