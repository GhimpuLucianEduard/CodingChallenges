import unittest

from challenges.ms.ms_practice import equal_digit_sum, jafar_checkers


class TestEqualDigitSum(unittest.TestCase):
    def test_equal_digit_sum(self):
        assert equal_digit_sum([51, 71, 17, 42]) == 93
        assert equal_digit_sum([42, 33, 60]) == 102
        assert equal_digit_sum([51, 32, 43]) == -1

    def test_equal_digit_sum_no_pair(self):
        assert equal_digit_sum([51, 32, 43]) == -1

    def test_equal_digit_sum_empty(self):
        assert equal_digit_sum([]) == -1


class TestJafarCheckers(unittest.TestCase):

    def test_jafar_checkers(self):
        assert jafar_checkers([
            ['.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'X', '.'],
            ['.', 'X', '.', '.', '.', '.'],
            ['.', '.', 'X', '.', 'X', '.'],
            ['.', '.', '.', 'O', '.', '.'],
        ]) == 2

    def test_jafar_checkers_zero(self):
        assert jafar_checkers([
            ['X', '.', '.', '.', '.'],
            ['.', 'X', '.', '.', '.'],
            ['.', '.', 'O', '.', '.'],
            ['.', '.', '.', 'X', '.'],
            ['.', '.', '.', '.', '.']
        ]) == 0

    def test_jafar_checkers_n10(self):
        assert jafar_checkers([
            ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'X', '.', '.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['X', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', 'X', '.', 'X', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'O', '.', '.', '.', '.', '.', '.'],
        ]) == 4

    def test_jafar_checkers_n2(self):
        assert jafar_checkers([
            ['.', 'X'],
            ['0', 'X']
        ]) == 0

    def test_jafar_checkers_n3(self):
        assert jafar_checkers([
            ['.', 'X', '.'],
            ['.', 'X', '.'],
            ['.', 'X', 'O']
        ]) == 1


if __name__ == '__main__':
    unittest.main()
