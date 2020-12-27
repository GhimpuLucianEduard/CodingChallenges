"""
10.1 Sorted Merge
You are given two sorted arrays, A, B where A has a large enough buffer at the end
to hold B. Write a method to merge B into A in sorted order.
"""
import unittest


def sorted_merge(a, b):
    # copy b in after a
    end = len(a) - 1
    end_of_b = len(b) - 1
    end_of_a = len(a) - len(b) - 1

    while end_of_b >= 0 and end_of_a >= 0:
        if a[end_of_a] >= b[end_of_b]:
            a[end] = a[end_of_a]
            end_of_a -= 1
        else:
            a[end] = b[end_of_b]
            end_of_b -= 1
        end -= 1

    while end_of_a >= 0:
        a[end] = a[end_of_a]
        end_of_a -= 1
        end -= 1

    while end_of_b >= 0:
        a[end] = b[end_of_b]
        end_of_b -= 1
        end -= 1
        
class TestSortedMerge(unittest.TestCase):
    def test_sorted_merge(self):
        a = [1, 4, 8, 9, 13, None, None, None, None]
        b = [3, 5, 10, 15]
        sorted_merge(a, b)
        self.assertEqual([1, 3, 4, 5, 8, 9, 10, 13, 15], a)

    def test_sorted_merge_2(self):
        a = [3, 4, 8, 9, 13, None, None, None, None]
        b = [2, 5, 10, 15]
        sorted_merge(a, b)
        self.assertEqual([2, 3, 4, 5, 8, 9, 10, 13, 15], a)


    def test_sorted_merge_3(self):
        a = [1, 2, 3, None, None, None]
        b = [2, 5, 6]
        sorted_merge(a, b)
        self.assertEqual([1, 2, 2, 3, 5, 6], a)