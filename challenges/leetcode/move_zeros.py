"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the
end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
import unittest


def move_zeros(nums):
    zeros_count = 0
    for i in range(len(nums)):
        if nums[i] != 0 and zeros_count > 0:
            nums[i - zeros_count] = nums[i]
            nums[i] = 0
        elif nums[i] == 0:
            zeros_count += 1
    return nums


class TestMoveZeros(unittest.TestCase):
    def test_move_zeros_empty(self):
        self.assertEqual([], move_zeros([]))

    def test_move_zeros_leetcode1(self):
        self.assertEqual([1, 3, 12, 0, 0], move_zeros([0, 1, 0, 3, 12]))

    def test_move_zeros_leetcode2(self):
        self.assertEqual([1], move_zeros([1]))

    def test_move_zeros_leetcode3(self):
        self.assertEqual([1, 0], move_zeros([1, 0]))

    def test_move_zeros_leetcode4(self):
        self.assertEqual([2, 1], move_zeros([2, 1]))
