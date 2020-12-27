"""
10.5 Sparse Search

Given a sorted array of strings that is interspersed with empty strings,
write a method to find the location of a given string.
"""
import unittest


def sparse_search(array, word):
    if len(array) == 0:
        return -1

    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        # case 0, is equal
        if array[mid] == word:
            return mid
        # case 1, is whitespace
        if array[mid] == "":
            # find a word in the left side
            while mid > start and array[mid] == "":
                mid -= 1

            if array[mid] == "" or array[mid] < word:
                # search in (mid + 1, end)
                start = ((start + end) // 2) + 1
            elif array[mid] > word:
                # search in (start, new_mid - 1)
                end = mid - 1
            elif array[mid] == word:
                return mid
        else:
            if array[mid] > word:
                # search in (start, mid - 1)
                end = mid - 1
            elif array[mid] < word:
                # search in (mid + 1, end)
                start = mid - 1

    return -1


class TestSparseSearch(unittest.TestCase):
    def test_sparse_search_empty(self):
        self.assertEqual(-1, sparse_search([], "a"))

    def test_sparse_search_all_whitespaces(self):
        self.assertEqual(-1, sparse_search(["", "", "", "", ""], "ab"))

    def test_sparse_search_all_whitespaces_even(self):
        self.assertEqual(-1, sparse_search(["", "", "", ""], "ab"))

    def test_sparse_search_one_element(self):
        self.assertEqual(-1, sparse_search([""], "ab"))

    def test_sparse_search_one_element(self):
        self.assertEqual(0, sparse_search(["ab"], "ab"))

    def test_sparse_search_book(self):
        self.assertEqual(4, sparse_search(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball"))

    def test_sparse_search_book_2(self):
        self.assertEqual(12, sparse_search(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "ee"], "ee"))

    def test_sparse_search_book_2(self):
        self.assertEqual(12, sparse_search(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "ee"], "ee"))