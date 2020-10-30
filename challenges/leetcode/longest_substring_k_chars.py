"""
395. Longest Substring with At Least K Repeating Characters

Find the length of the longest substring T of
a given string (consists of lowercase letters only)
such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output: 3

The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input:
s = "ababbc", k = 2

Output: 5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
import unittest
from collections import defaultdict


def longest_substring_k_chars(s, k):
    return longest_substring_k_chars_aux(s, k, 0, len(s))


def longest_substring_k_chars_aux(s, k, start, end):
    if end < k:
        return 0

    char_map = defaultdict(int)

    for i in range(start, end, 1):
        char_map[s[i]] += 1

    for i in range(start, end, 1):
        if char_map[s[i]] >= k:
            continue

        j = i + 1
        while j < end and char_map[s[j]] < k:
            j += 1
        return max(longest_substring_k_chars_aux(s, k, start, i), longest_substring_k_chars_aux(s, k, j, end))

    return end - start


class TestLongestSubstringKChars(unittest.TestCase):
    def test_longest_substring_k_chars_empty_s(self):
        self.assertEqual(0, longest_substring_k_chars("", 2))

    def test_longest_substring_k_chars_k_0(self):
        self.assertEqual(3, longest_substring_k_chars("abc", 0))

    def test_longest_substring_k_chars_leetcode1(self):
        self.assertEqual(3, longest_substring_k_chars("aaabb", 3))

    def test_longest_substring_k_chars_leetcode2(self):
        self.assertEqual(5, longest_substring_k_chars("ababbc", 2))

    def test_longest_substring_k_chars_leetcode3(self):
        self.assertEqual(3, longest_substring_k_chars("bbaaacbd", 3))
