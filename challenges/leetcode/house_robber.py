"""
198. House Robber

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
import unittest


def house_robber(nums):
    cur_sum = 0
    prev_sum = 0
    for n in nums:
        temp = cur_sum
        cur_sum = max(n + prev_sum, cur_sum)
        prev_sum = temp

    return max(cur_sum, prev_sum)


class TestHouseRobber(unittest.TestCase):

    def test_house_robber_empty(self):
        self.assertEqual(house_robber([]), 0)

    def test_house_robber_single(self):
        self.assertEqual(house_robber([5]), 5)

    def test_house_robber_two_elements(self):
        self.assertEqual(house_robber([5, 10]), 10)

    def test_house_robber_leetcode1(self):
        self.assertEqual(house_robber([1, 2, 3, 1]), 4)

    def test_house_robber_leetcode2(self):
        self.assertEqual(house_robber([2, 7, 9, 3, 1]), 12)

    def test_house_robber_leetcode1(self):
        self.assertEqual(house_robber([2, 1, 1, 2]), 4)
