"""
179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:

Input: nums = [1]
Output: "1"

Example 4:

Input: nums = [10]
Output: "10"

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
import unittest


def largest_number(nums):
    if len(nums) == 0:
        return ""

    nums = quick_sort(nums)
    nums.reverse()
    rez = ""
    for n in nums:
        rez += str(n)

    if rez[0] == "0":
        return "0"
    else:
        return rez


def compare(n1, n2):
    new_n1 = str(n1) + str(n2)
    new_n2 = str(n2) + str(n1)
    if new_n1 > new_n2:
        return n1
    elif new_n1 < new_n2:
        return n2
    else:
        return -1


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            compare_result = compare(x, pivot)
            if compare_result == pivot:
                less.append(x)
            elif compare_result == -1:
                equal.append(x)
            elif compare_result == x:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


class TestLargestNumber(unittest.TestCase):
    def test_largest_number_empty(self):
        self.assertEqual(largest_number([]), "")

    def test_largest_number_leetcode1(self):
        self.assertEqual(largest_number([10, 2]), "210")

    def test_largest_number_leetcode2(self):
        self.assertEqual(largest_number([3, 30, 34, 5, 9]), "9534330")

    def test_largest_number_leetcode3(self):
        self.assertEqual(largest_number([0, 4, 51, 9]), "95140")

    def test_largest_number_leetcode4(self):
        self.assertEqual(largest_number([0, 0]), "0")
