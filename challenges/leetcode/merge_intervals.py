"""
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
import unittest


def merge_intervals(intervals):
    rez = []
    if len(intervals) == 0:
        return rez

    intervals.sort(key=lambda interval: interval[0])

    cur_int = intervals[0]

    for interval in intervals:
        if interval[0] <= cur_int[1]:
            cur_int[1] = max(cur_int[1], interval[1])
        else:
            rez.append(cur_int)
            cur_int = interval

    rez.append(cur_int)
    return rez


class TestMergeIntervals(unittest.TestCase):

    def test_merge_intervals_empty(self):
        self.assertEqual(merge_intervals([]), [])

    def test_merge_intervals_leetcode1(self):
        self.assertEqual(merge_intervals(
            [[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]])

    def test_merge_intervals_leetcode2(self):
        self.assertEqual(merge_intervals(
            [[1, 4], [4, 5]]), [[1, 5]])

    def test_merge_intervals_leetcode3(self):
        self.assertEqual(merge_intervals(
            [[1, 4], [1, 4]]), [[1, 4]])

    def test_merge_intervals_leetcode4(self):
        self.assertEqual(merge_intervals(
            [[1, 4], [0, 4]]), [[0, 4]])

    def test_merge_intervals_leetcode5(self):
        self.assertEqual(merge_intervals(
            [[1, 4], [2, 3]]), [[1, 4]])
