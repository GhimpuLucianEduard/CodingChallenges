"""
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory
 is limited such that you cannot load all elements into the memory at once?
"""
import unittest
from collections import defaultdict


def intersection_of_two_arrays_2(nums1, nums2):
    intersection = []

    # validate the data
    if len(nums1) <= 0 or len(nums2) <= 0:
        return intersection

    freq = defaultdict(int)

    for num in nums1:
        freq[num] += 1

    for num in nums2:
        if freq[num] > 0:
            intersection.append(num)
            freq[num] -= 1

    return intersection


class TestIntersectionOfTwoArrays2(unittest.TestCase):
    def test_intersection_of_two_arrays_2_empty(self):
        self.assertEqual([], intersection_of_two_arrays_2([], [2, 3]))

    def test_intersection_of_two_arrays_2_leetcode1(self):
        self.assertEqual([2, 2], intersection_of_two_arrays_2([1, 2, 2, 1], [2, 2]))

    def test_intersection_of_two_arrays_2_leetcode2(self):
        self.assertEqual([9, 4], intersection_of_two_arrays_2([4, 9, 5], [9, 4, 9, 8, 4]))
