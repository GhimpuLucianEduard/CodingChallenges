"""
207. Course Schedule

There are a total of numCourses courses you
have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to
take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of
prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Constraints:

The input prerequisites is a graph represented
by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
import unittest
from collections import defaultdict


def course_schedule(no_courses, prerequisites):
    if len(prerequisites) == 0:
        return True

    # build list of adjacency matrix
    adj_matrix = defaultdict(list)
    for pre in prerequisites:
        adj_matrix[pre[0]].append(pre[1])

    visited = defaultdict(int)
    for node in list(adj_matrix.keys()):
        if not dfs(node, adj_matrix, visited):
            return False

    return len(visited.keys()) <= no_courses


# -1 -> being visited, 0 -> not visited, 1 -> visited
def dfs(root, adj_matrix, visited):
    if visited[root] == -1:
        return False

    if visited[root] == 1:
        return True

    visited[root] = -1
    for neigh in adj_matrix[root]:
        if not dfs(neigh, adj_matrix, visited):
            return False

    visited[root] = 1
    return True


class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule_empty(self):
        self.assertEqual(True, course_schedule(1, []))

    def test_course_schedule_leetcode1(self):
        self.assertEqual(True, course_schedule(2, [[1, 0]]))

    def test_course_schedule_leetcode2(self):
        self.assertEqual(True, course_schedule(3, [[1, 0]]))

    def test_course_schedule_leetcode3(self):
        self.assertEqual(False, course_schedule(3, [[1, 0], [0, 2], [2, 1]]))

    def test_course_schedule_leetcode4(self):
        self.assertEqual(True, course_schedule(3, [[2, 1], [1, 0]]))
