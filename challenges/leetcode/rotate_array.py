"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""
import unittest


# N.B. leetcode asks to change it in place and not return an array, simply remove all return array

def rotate_array(array, k):
    if len(array) == 0:
        return array

    # normalize k
    k = k % len(array)

    if k == len(array):
        return array

    new_array = [None] * len(array)
    for i in range(0, len(array)):
        new_array[(i + k) % len(array)] = array[i]

    return new_array


def rotate_array_o1_space(array, k):
    if len(array) == 0:
        return array

    # normalize k
    k = k % len(array)

    if k == len(array):
        return array

    array.reverse()
    first_half = array[:k]
    first_half.reverse()
    second_half = array[k:]
    second_half.reverse()

    return first_half + second_half


class TestRotateArray(unittest.TestCase):

    def test_rotate_array_empty(self):
        self.assertEqual(rotate_array([], 10), [])

    def test_rotate_array_leetcode1(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_array_leetcode2(self):
        self.assertEqual(rotate_array([-1, -100, 3, 99], 2), [3, 99, -1, -100])

    def test_rotate_array_o1_space_empty(self):
        self.assertEqual(rotate_array_o1_space([], 10), [])

    def test_rotate_array_o1_space_leetcode1(self):
        self.assertEqual(rotate_array_o1_space([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_array_o1_space_leetcode2(self):
        self.assertEqual(rotate_array_o1_space([-1, -100, 3, 99], 2), [3, 99, -1, -100])
