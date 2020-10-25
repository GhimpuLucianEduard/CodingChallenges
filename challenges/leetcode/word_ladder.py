"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
import unittest
from collections import deque, defaultdict


def word_ladder(begin_word, end_word, word_list):
    if len(word_list) == 0:
        return 0

    if begin_word not in word_list:
        word_list.append(begin_word)

    graph = build_graph(word_list)
    visited = defaultdict(bool)
    queue = deque()
    queue.append([begin_word, 1])
    visited[begin_word] = True

    while len(queue) != 0:
        current = queue.popleft()

        if current[0] == end_word:
            return current[1]

        for i in range(len(current[0])):
            s = current[0][:i] + "*" + current[0][i + 1:]
            for neigh in graph[s]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append([neigh, current[1] + 1])

    return 0


def build_graph(words):
    graph = defaultdict()
    for word in words:
        for i in range(len(word)):
            s = word[:i] + "*" + word[i + 1:]
            graph[s] = graph.get(s, []) + [word]
    return graph


class TestWordLadder(unittest.TestCase):

    def test_word_ladder_empty_dict(self):
        self.assertEqual(word_ladder("hot", "hit", []), 0)

    def test_word_ladder_leetcode1(self):
        self.assertEqual(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)

    def test_word_ladder_leetcode2(self):
        self.assertEqual(word_ladder("a", "c", ["a", "b", "c"]), 2)

    def test_word_ladder_leetcode3(self):
        self.assertEqual(word_ladder("hot", "dog", ["hot", "dog", "dot"]), 3)

    def test_word_ladder_leetcode4(self):
        self.assertEqual(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
