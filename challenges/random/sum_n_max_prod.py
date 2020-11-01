import unittest
from collections import defaultdict


def sum_n_max_prod(n):
    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    if n == 3:
        return [2, 1]

    visited = defaultdict(list)
    visited[2] = [2]
    visited[3] = [3]
    return sum_n_max_prod_aux(n, visited)


def sum_n_max_prod_aux(n, visited):
    if n in visited:
        return visited[n]

    if n % 2 == 0:
        nums = sum_n_max_prod_aux(n // 2, visited) + sum_n_max_prod_aux(n // 2, visited)
    else:
        nums = sum_n_max_prod_aux(n // 2, visited) + sum_n_max_prod_aux((n // 2) + 1, visited)

    visited[n] = nums
    return nums


def main():
    print(sum_n_max_prod(10))


if __name__ == '__main__':
    main()


class TestSumNMaxProd(unittest.TestCase):
    def test_sum_n_max_prod_1(self):
        self.assertEqual([1], sum_n_max_prod(1))

    def test_sum_n_max_prod_2(self):
        self.assertEqual([1, 1], sum_n_max_prod(2))

    def test_sum_n_max_prod_3(self):
        self.assertEqual([2, 1], sum_n_max_prod(3))

    def test_sum_n_max_prod_10(self):
        self.assertEqual([2, 3, 2, 3], sum_n_max_prod(10))
