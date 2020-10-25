"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:

Input: digits = [0]
Output: [1]

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
import unittest


def plus_one(digits):
    if len(digits) == 0:
        return digits

    digits.reverse()

    rem = 1
    for i in range(len(digits)):
        aux = digits[i]
        digits[i] = (rem + digits[i]) % 10
        rem = (rem + aux) // 10

    if rem == 1:
        digits.append(1)

    digits.reverse()
    return digits


class TestPlusOne(unittest.TestCase):
    def test_plus_one_empty(self):
        self.assertEqual(plus_one([]), [])

    def test_plus_one_leetcode1(self):
        self.assertEqual(plus_one([1, 2, 3]), [1, 2, 4])

    def test_plus_one_leetcode1(self):
        self.assertEqual(plus_one([1, 9]), [2, 0])

    def test_plus_one_leetcode1(self):
        self.assertEqual(plus_one([9]), [1, 0])