"""
10.3 Search in rotated array

Given a sorted array on n integers that has been rotated and unknown
numbers of times, write code to find an element in the array. You
may assume that the array was originally sorted in increasing order.
"""
import unittest


def search_rotated_array(array, n):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == n:
            return mid

        if array[start] <= array[mid]:
            if array[start] <= n <= array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if array[mid] <= n <= array[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1

class TestSearchRotatedArray(unittest.TestCase):
    def test_search_rotated_array_empty(self):
        self.assertEqual(-1, search_rotated_array([], 1))

    def test_search_rotated_small_false(self):
        self.assertEqual(-1, search_rotated_array([10, 12, 4, 5, 6], 3))

    def test_search_rotated_big_true(self):
        self.assertEqual(8, search_rotated_array([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5))

    def test_search_rotated_equals_false(self):
        self.assertEqual(-1, search_rotated_array([2, 2, 2, 3, 4, 2], 5))

    def test_search_rotated_equals_true(self):
        self.assertEqual(3, search_rotated_array([2, 2, 2, 3, 4, 2], 3))