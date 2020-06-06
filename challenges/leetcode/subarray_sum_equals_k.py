import unittest
from collections import defaultdict


def subarray_sum_equals_k(array, k):
    """
    560. Subarray Sum Equals K

    Given an array of integers and an integer k,
    you need to find the total number of continuous subarrays whose sum equals to k.

    Example:

    Input: nums = [1,1,1], k = 2
    Output: 2

    Constraints:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

    :param array: input array
    :param k: input k
    :return: total numbers of subarrays with sum equal to k
    """

    sums = defaultdict(int)
    sums[0] = 1
    total_sum = 0
    count = 0

    for element in array:
        total_sum += element
        if total_sum - k in sums:
            count += sums[total_sum - k]

        sums[total_sum] += 1

    return count


class TestSubarraySumEqualsK(unittest.TestCase):

    def test_subarray_sum_equals_k_empty(self):
        self.assertEqual(subarray_sum_equals_k([], 10), 0)

    def test_subarray_sum_equals_k_single(self):
        self.assertEqual(subarray_sum_equals_k([5], 10), 0)

    def test_subarray_sum_equals_k_single_good(self):
        self.assertEqual(subarray_sum_equals_k([5], 5), 1)

    def test_subarray_sum_equals_k_leetcode_test(self):
        self.assertEqual(subarray_sum_equals_k([1, 1, 1], 2), 2)

    def test_subarray_sum_equals_k_overlapping(self):
        self.assertEqual(subarray_sum_equals_k([1, 1, 2, 3, 4, 3, 7], 7), 4)

    def test_subarray_sum_equals_k_negatives(self):
        self.assertEqual(subarray_sum_equals_k([5, -3, 4, 2, 8, -2], 6), 3)

    def test_subarray_sum_equals_2(self):
        self.assertEqual(subarray_sum_equals_k([1, 7, 12], 13), 0)


def subarray_sum_equals_k_bad(array, k):
    """
    Same as subarray_sum_equals_k but in O(n^2)
    """
    if len(array) == 0:
        return 0

    if len(array) == 1 and array[0] == k:
        return 1

    total_sums = 0
    for i in range(0, len(array)):
        current_sum = array[i]
        # also check single elements
        if current_sum == k:
            total_sums += 1

        # loop other elements and build the sum
        for j in range(i + 1, len(array)):
            current_sum += array[j]
            if current_sum == k:
                total_sums += 1

    return total_sums
