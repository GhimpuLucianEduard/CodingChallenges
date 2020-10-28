"""
118. Pascal's Triangle

Given a non-negative integer numRows,
generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the
sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
import unittest


def pascal_triangle(n):
    rez_array = []

    for i in range(1, n + 1, 1):
        new_row = [1] * i
        for j in range(i):
            if j != 0 and j != i - 1:
                new_row[j] = rez_array[i - 2][j] + rez_array[i - 2][j - 1]
        rez_array.append(new_row)

    return rez_array


class TestPascalTriangle(unittest.TestCase):
    def test_pascal_triangle_0(self):
        self.assertEqual([], pascal_triangle(0))

    def test_pascal_triangle_1(self):
        self.assertEqual([[1]], pascal_triangle(1))

    def test_pascal_triangle_2(self):
        self.assertEqual([[1], [1, 1]], pascal_triangle(2))

    def test_pascal_triangle_4(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]], pascal_triangle(4))

    def test_pascal_triangle_5(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], pascal_triangle(5))

    def test_pascal_triangle_6(self):
        self.assertEqual([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]], pascal_triangle(6))
