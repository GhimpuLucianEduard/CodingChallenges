"""
139. Word Break

Given a non-empty string s and a dictionary wordDict
containing a list of non-empty words, determine if s
can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
import unittest
from collections import defaultdict


class Trie:
    def __init__(self, children=None, is_word=False):
        if children is None:
            children = defaultdict(Trie)
        self.children = children
        self.is_word = is_word

    def insert(self, word):
        root = self
        for c in word:
            if c not in root.children:
                root.children[c] = Trie()
            root = root.children[c]
        root.is_word = True

    def search(self, word):
        root = self
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.is_word


def word_break(s, word_dict):
    if len(word_dict) == 0:
        return False

    trie = Trie()
    visited = defaultdict(bool)

    for word in word_dict:
        trie.insert(word)

    visited[0] = True
    for i in range(len(s) + 1):
        for j in range(i):
            if visited[j] and trie.search(s[j:i]):
                visited[i] = True
                break
    return visited[len(s)]


class TestWordBreak(unittest.TestCase):
    def test_word_break_leetcode1(self):
        self.assertEqual(True, word_break("leetcode", ["leet", "code"]))

    def test_word_break_leetcode2(self):
        self.assertEqual(True, word_break("applepenapple", ["apple", "pen"]))

    def test_word_break_leetcode3(self):
        self.assertEqual(False, word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_word_break_leetcode4(self):
        self.assertEqual(True, word_break("goalspecial", ["go", "goal", "goals", "special"]))