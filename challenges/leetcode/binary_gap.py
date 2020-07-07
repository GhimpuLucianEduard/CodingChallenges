"""
Given a positive integer N, find and return the longest distance between
two consecutive 1's in the binary representation of N.
If there aren't two consecutive 1's, return 0.

Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation:
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0
"""
import unittest


def binary_gap(n):
    binary_n = bin(n)[2:]
    current_gap = 0
    max_gap = 0
    in_gap = False

    for i in range(0, len(binary_n)):
        if binary_n[i] == '1':
            if in_gap:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                current_gap += 1
                in_gap = True
        else:
            if in_gap:
                current_gap += 1

    return max_gap


class TestBinaryGap(unittest.TestCase):

    def test_binary_gap_22(self):
        self.assertEqual(binary_gap(22), 2)

    def test_binary_gap_5(self):
        self.assertEqual(binary_gap(5), 2)

    def test_binary_gap_6(self):
        self.assertEqual(binary_gap(6), 1)

    def test_binary_gap_8(self):
        self.assertEqual(binary_gap(8), 0)

    def test_binary_gap_0(self):
        self.assertEqual(binary_gap(0), 0)
