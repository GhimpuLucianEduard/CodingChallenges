"""
10.11 Peaks and Valleys

In an array of integers, a "peak" is an element which is greater than or equal
to the adjacent integers and "valley" is an element which is less than or equal to the adjacent integers.
For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys.
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

Example:
    Input: {5, 3, 1, 2, 3}
    Output: {5, 1, 3, 2, 3}
"""
import unittest


def peaks_and_valleys(array):
    if len(array) <= 0:
        return array

    for i in range(1, len(array), 2):
        max_ind = max_index(array, i)
        if max_ind != i:
            array[i], array[max_ind] = array[max_ind], array[i]


def max_index(array, index):
    size = len(array)
    a_value = array[index] if index < size else -1
    b_value = array[index - 1] if index - 1 < size else -1
    c_value = array[index + 1] if index + 1 < size else -1

    max_value = max(a_value, max(b_value, c_value))

    if max_value == a_value:
        return index
    elif max_value == b_value:
        return index - 1
    else:
        return index + 1


def peaks_and_valleys_slow(array):
    if len(array) <= 1:
        return array

    quick_sort(array, 0, len(array) - 1)
    start = 0
    end = len(array) - 1
    mid = (start + end) // 2
    aux = [0] * len(array)
    for i in range(0, len(array), 2):
        if start == end:
            aux[i] = array[mid]
        else:
            if start < mid:
                aux[i + 1] = array[start]
                start += 1
            if end > mid:
                aux[i] = array[end]
                end -= 1

    for i in range(len(aux)):
        array[i] = aux[i]


def quick_sort(array, start, end):
    if start < end:
        partition_point = partition(array, start, end)
        quick_sort(array, start, partition_point - 1)
        quick_sort(array, partition_point, end)


def partition(array, start, end):
    pivot = array[(start + end) // 2]

    while start <= end:
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1

        if start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    return start


class TestPeaksAndValleys(unittest.TestCase):
    def test_peaks_and_valleys_empty(self):
        array = []
        peaks_and_valleys(array)
        self.assertEqual([], array)

    def test_peaks_and_valleys_single(self):
        array = [1]
        peaks_and_valleys(array)
        self.assertEqual([1], array)

    def test_peaks_and_valleys_book(self):
        array = [5, 3, 1, 2, 3]
        peaks_and_valleys(array)
        self.assertEqual([3, 5, 1, 3, 2], array)

    def test_peaks_and_valleys_book_changed(self):
        array = [5, 1, 3, 2, 3]
        peaks_and_valleys(array)
        self.assertEqual([1, 5, 2, 3, 3], array)

    def test_peaks_and_valleys_plain(self):
        array = [1, 1, 1]
        peaks_and_valleys(array)
        self.assertEqual([1, 1, 1], array)

    def test_peaks_and_valleys_weird(self):
        array = [7, 1, 1, 1, 7]
        peaks_and_valleys(array)
        self.assertEqual([1, 7, 1, 7, 1], array)

    def test_peaks_and_valleys_sol(self):
        array = [9, 1, 7, 7, 6, 3, 5]
        peaks_and_valleys(array)
        self.assertEqual([1, 9, 7, 7, 3, 6, 5], array)

class TestPeaksAndValleysSlow(unittest.TestCase):
    def test_peaks_and_valleys_empty(self):
        array = []
        peaks_and_valleys_slow(array)
        self.assertEqual([], array)

    def test_peaks_and_valleys_single(self):
        array = [1]
        peaks_and_valleys_slow(array)
        self.assertEqual([1], array)

    def test_peaks_and_valleys_book(self):
        array = [5, 3, 1, 2, 3]
        peaks_and_valleys_slow(array)
        self.assertEqual([5, 1, 3, 2, 3], array)

    def test_peaks_and_valleys_plain(self):
        array = [1, 1, 1]
        peaks_and_valleys_slow(array)
        self.assertEqual([1, 1, 1], array)

    def test_peaks_and_valleys_weird(self):
        array = [7, 1, 1, 1, 7]
        peaks_and_valleys_slow(array)
        self.assertEqual([7, 1, 7, 1, 1], array)
