"""
Longest Substring Without Repeating Characters


Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
import unittest
from collections import defaultdict


def longest_substring_no_dup(input):
    char_dict = defaultdict(str)
    result = 0
    anchor = 0

    for i in range(0, len(input)):
        if input[i] in char_dict.keys():
            if char_dict[input[i]] >= anchor:
                anchor = char_dict[input[i]] + 1
        result = max(result, i - anchor + 1)
        char_dict[input[i]] = i

    return result


class TestLongestSubstringNoDup(unittest.TestCase):

    def test_longest_substring_no_dup_empty(self):
        self.assertEqual(longest_substring_no_dup(""), 0)

    def test_longest_substring_no_dup_one_element(self):
        self.assertEqual(longest_substring_no_dup("a"), 1)

    def test_longest_substring_no_dup_two_elements(self):
        self.assertEqual(longest_substring_no_dup("ab"), 2)

    def test_longest_substring_no_dup_two_elements_same(self):
        self.assertEqual(longest_substring_no_dup("aa"), 1)

    def test_longest_substring_no_dup_two_elements_leetcode1(self):
        self.assertEqual(longest_substring_no_dup("abcabcbb"), 3)

    def test_longest_substring_no_dup_two_elements_leetcode2(self):
        self.assertEqual(longest_substring_no_dup("bbbbb"), 1)

    def test_longest_substring_no_dup_two_elements_leetcode3(self):
        self.assertEqual(longest_substring_no_dup("pwwkew"), 3)

    def test_longest_substring_no_dup_two_elements_leetcode4(self):
        self.assertEqual(longest_substring_no_dup("abba"), 2)
