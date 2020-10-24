"""
213. House Robber II

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing
the amount of money of each house, return the maximum amount
of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [0]
Output: 0

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
import unittest


def house_robber_2(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    return max(house_robber(nums[1:]), house_robber(nums[:-1]))


def house_robber(nums):
    cur_sum = 0
    prev_sum = 0
    for n in nums:
        temp = cur_sum
        cur_sum = max(n + prev_sum, cur_sum)
        prev_sum = temp

    return max(cur_sum, prev_sum)


class TestHouseRobber2(unittest.TestCase):

    def test_house_robber_2_empty(self):
        self.assertEqual(house_robber_2([]), 0)

    def test_house_robber_2_single(self):
        self.assertEqual(house_robber_2([1]), 1)

    def test_house_robber_2_leetcode1(self):
        self.assertEqual(house_robber_2([2, 3, 2]), 3)

    def test_house_robber_2_leetcode2(self):
        self.assertEqual(house_robber_2([1, 2, 3, 1]), 4)
