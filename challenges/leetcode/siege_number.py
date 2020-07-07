"""
136. Single Number

Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
import unittest
from collections import defaultdict


def siege_number(array):
    num_dict = defaultdict(int)

    for n in array:
        num_dict[n] += 1

    for key, value in num_dict.items():
        if value == 1:
            return key

    return None


class TestSiegeNumber(unittest.TestCase):

    def test_siege_number_empty(self):
        self.assertEqual(siege_number([]), None)

    def test_siege_number_leetcode1(self):
        self.assertEqual(siege_number([2, 2, 1]), 1)

    def test_siege_number_leetcode2(self):
        self.assertEqual(siege_number([4, 1, 2, 1, 2]), 4)
