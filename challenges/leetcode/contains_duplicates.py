"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears a
t least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
import unittest
from collections import defaultdict


def contains_duplicates(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False

    visited = defaultdict(bool)

    for num in nums:
        if visited[num]:
            return True
        visited[num] = True

    return False


class TestContaisDuplicates(unittest.TestCase):
    def test_contains_duplicates_empty(self):
        self.assertEqual(False, contains_duplicates([]))

    def test_contains_duplicates_leetcode1(self):
        self.assertEqual(True, contains_duplicates([1, 2, 3, 1]))

    def test_contains_duplicates_leetcode2(self):
        self.assertEqual(False, contains_duplicates([1, 2, 3, 4]))

    def test_contains_duplicates_leetcode3(self):
        self.assertEqual(True, contains_duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
