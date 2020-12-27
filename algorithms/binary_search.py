import unittest


def binary_search(array, n):
    return binary_search_aux(array, n, 0, len(array) - 1)


def binary_search_aux(array, n, start, end):
    if start > end:
        return False

    mid = (start + end) // 2
    if array[mid] == n:
        return True
    if array[mid] > n:
        return binary_search_aux(array, n, start, mid - 1)
    if array[mid] < n:
        return binary_search_aux(array, n, mid + 1, end)


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_empty(self):
        self.assertEqual(False, binary_search([], 1))

    def test_binary_search_single(self):
        self.assertEqual(True, binary_search([1], 1))

    def test_binary_search_normal_true(self):
        self.assertEqual(True, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))

    def test_binary_search_normal_false(self):
        self.assertEqual(False, binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 12))

    def test_binary_search_even_false(self):
        self.assertEqual(False, binary_search([1, 2, 3], 4))
