"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
import unittest
from collections import defaultdict
from random import random, shuffle


def kth_largest_element(nums, k):
    # k always valid, no need to check for edge cases

    shuffle(nums)
    partition_index = partition(nums, 0, len(nums) - 1)

    if partition_index > len(nums) - k:
        return kth_largest_element(nums[:partition_index], k - (len(nums) - partition_index))
    elif partition_index < len(nums) - k:
        return kth_largest_element(nums[partition_index + 1:], k)
    else:
        return nums[partition_index]


def partition(nums, left, right):
    pivot = nums[right]

    partition_index = left
    for i in range(right):
        if nums[i] < pivot:
            nums[i], nums[partition_index] = nums[partition_index], nums[i]
            partition_index += 1

    nums[right], nums[partition_index] = nums[partition_index], nums[right]
    return partition_index

class TestKthLargestElement(unittest.TestCase):
    def test_kth_largest_element_leetcode1(self):
        self.assertEqual(5, kth_largest_element([3, 2, 1, 5, 6, 4], 2))
