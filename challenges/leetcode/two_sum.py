import unittest
from collections import defaultdict


def two_sum(array, target):
    """
    1. Two Sum
    Given an array of integers, return indices of the
    two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

    :param array: input array
    :param target: target sum
    :return: tuple with the 2 indexes, (-1, -1) otherwise
    """

    # use a map to keep track of the indexes
    element_dict = defaultdict(int)

    if len(array) < 2:
        return -1, -1

    for i in range(0, len(array)):
        # check for complement
        if target - array[i] in element_dict:
            return element_dict[target - array[i]], i

        element_dict[array[i]] = i

    return -1, -1


class TestTwoSum(unittest.TestCase):

    def test_two_sum_empty(self):
        self.assertEqual(two_sum([], 10), (-1, -1))

    def test_two_sum_one_element(self):
        self.assertEqual(two_sum([2], 10), (-1, -1))

    def test_two_sum_one_multiple_elements(self):
        self.assertEqual(two_sum([2, 7, 15, 11], 9), (0, 1))

    def test_two_sum_one_multiple_duplicate(self):
        self.assertEqual(two_sum([5, 7, 5, 11], 10), (0, 2))
