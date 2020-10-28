"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1)
extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are
in the range [0,2]. 2 is the missing number in the range
since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers
 are in the range [0,9]. 8 is the missing number
 in the range since it does not appear in nums.
Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all
numbers are in the range [0,1]. 1 is the missing number
in the range since it does not appear in nums.
"""
import unittest


def missing_number(nums):
    n_sum = len(nums) * (len(nums) + 1) // 2
    for num in nums:
        n_sum -= num

    return n_sum


def missing_number_xor(nums):
    n = len(nums)
    for i in range(len(nums)):
        n ^= i
        n ^= nums[i]
    return n


class TestMissingNumber(unittest.TestCase):
    def test_missing_number_leetcode1(self):
        self.assertEqual(2, missing_number([3, 0, 1]))

    def test_missing_number_leetcode2(self):
        self.assertEqual(2, missing_number([0, 1]))

    def test_missing_number_leetcode3(self):
        self.assertEqual(8, missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))

    def test_missing_number_leetcode4(self):
        self.assertEqual(1, missing_number([0]))


class TestMissingNumberXOR(unittest.TestCase):
    def test_missing_number_xor_leetcode1(self):
        self.assertEqual(2, missing_number_xor([3, 0, 1]))

    def test_missing_number_xor_leetcode2(self):
        self.assertEqual(2, missing_number_xor([0, 1]))

    def test_missing_number_xor_leetcode3(self):
        self.assertEqual(8, missing_number_xor([9, 6, 4, 2, 3, 5, 7, 0, 1]))

    def test_missing_number_xor_leetcode4(self):
        self.assertEqual(1, missing_number_xor([0]))
