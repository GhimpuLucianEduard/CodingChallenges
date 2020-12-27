import unittest


def quick_sort(array):
    quick_sort_aux(array, 0, len(array) - 1)


def quick_sort_aux(array, start, end):
    if start < end:
        partition_point = partition(array, start, end)
        quick_sort_aux(array, start, partition_point - 1)
        quick_sort_aux(array, partition_point, end)


def partition(array, left, right):
    pivot = array[(left + right) // 2]

    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return left


class TestQuickSort(unittest.TestCase):
    def test_quick_sort_empty(self):
        array = []
        quick_sort(array)
        self.assertEqual([], array)

    def test_quick_sort_single(self):
        array = [1]
        quick_sort(array)
        self.assertEqual([1], array)

    def test_quick_sort_elements(self):
        array = [7, 1]
        quick_sort(array)
        self.assertEqual([1, 7], array)

    def test_quick_sort_normal(self):
        array = [7, 1, 3, 6, 6, 8, 4, 5, 9, 11, 8]
        quick_sort(array)
        self.assertEqual([1, 3, 4, 5, 6, 6, 7, 8, 8, 9, 11], array)

    def test_quick_sort_sorted(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        quick_sort(array)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], array)

    def test_quick_sort_reverse_sorted(self):
        array = [9, 8, 7, 6, 3, 1]
        quick_sort(array)
        self.assertEqual([1, 3, 6, 7, 8, 9], array)

    def test_quick_sort_all_equal(self):
        array = [1, 1, 1, 1, 1, 1, 1, 1]
        quick_sort(array)
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1], array)
