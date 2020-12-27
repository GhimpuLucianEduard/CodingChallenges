import unittest


def merge_sort(array):
    merge_sort_aux(array, 0, len(array) - 1, [0] * len(array))


def merge_sort_aux(array, start, end, helper):
    if start < end:
        mid = (start + end) // 2
        merge_sort_aux(array, start, mid, helper)
        merge_sort_aux(array, mid + 1, end, helper)
        merge(array, start, end, helper)

        
def merge(array, left_start, right_end, helper):
    # find left end
    left_end = (left_start + right_end) // 2
    # find right start
    right_start = left_end + 1

    left = left_start
    right = right_start
    helper_index = left_start
    while left <= left_end and right <= right_end:
        if array[left] <= array[right]:
            helper[helper_index] = array[left]
            left += 1
        else:
            helper[helper_index] = array[right]
            right += 1
        helper_index += 1

    while left <= left_end:
        helper[helper_index] = array[left]
        left += 1
        helper_index += 1

    while right <= right_end:
        helper[helper_index] = array[right]
        right += 1
        helper_index += 1

    while left_start <= right_end:
        array[left_start] = helper[left_start]
        left_start += 1


class TestMergeSort(unittest.TestCase):
    def test_merge_sort_empty(self):
        array = []
        merge_sort(array)
        self.assertEqual([], array)

    def test_merge_sort_single(self):
        array = [1]
        merge_sort(array)
        self.assertEqual([1], array)

    def test_merge_sort_two_elements(self):
        array = [7, 1]
        merge_sort(array)
        self.assertEqual([1, 7], array)

    def test_merge_sort_normal(self):
        array = [7, 1, 3, 6, 6, 8, 4, 5, 9, 11, 8]
        merge_sort(array)
        self.assertEqual([1, 3, 4, 5, 6, 6, 7, 8, 8, 9, 11], array)

    def test_merge_sort_sorted(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        merge_sort(array)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], array)

    def test_merge_sort_reverse_sorted(self):
        array = [9, 8, 7, 6, 3, 1]
        merge_sort(array)
        self.assertEqual([1, 3, 6, 7, 8, 9], array)

    def test_merge_sort_all_equal(self):
        array = [1, 1, 1, 1, 1, 1, 1, 1]
        merge_sort(array)
        self.assertEqual([1, 1, 1, 1, 1, 1, 1, 1], array)
