"""
202. Happy Number

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat
the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
import unittest
from collections import defaultdict


def happy_number(n):
    visited = defaultdict(bool)
    return happy_number_aux(n, visited)


def happy_number_aux(n, visited):
    if n == 1:
        return True

    if visited[n]:
        return False

    n_aux = n
    n_sum = 0
    while n_aux != 0:
        digit = n_aux % 10
        n_aux = n_aux // 10
        n_sum = n_sum + pow(digit, 2)

    visited[n] = True
    return happy_number_aux(n_sum, visited)


class TestHappyNumber(unittest.TestCase):
    def test_happy_number_0(self):
        self.assertEqual(happy_number(0), False)

    def test_happy_number_1(self):
        self.assertEqual(happy_number(1), True)

    def test_happy_number_19(self):
        self.assertEqual(happy_number(19), True)

    def test_happy_number_1221(self):
        self.assertEqual(happy_number(1221), True)
