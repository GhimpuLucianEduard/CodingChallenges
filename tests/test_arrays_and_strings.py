import unittest

from challenges.ctci.arrays_and_strings import *


class TestUniqueCharacters(unittest.TestCase):

    def test_unique_characters_empty(self):
        assert unique_characters('') == True

    def test_unique_characters_true(self):
        assert unique_characters('normal') == True

    def test_unique_characters_false(self):
        assert unique_characters('aaaflase') == False

    def test_unique_characters_no_data_structure_empty(self):
        assert unique_characters_no_data_structure('') == True

    def test_unique_characters_no_data_structure_true(self):
        assert unique_characters_no_data_structure('normal') == True

    def test_unique_characters_no_data_structure_false(self):
        assert unique_characters_no_data_structure('aaaflase') == False


class TestCheckPermutations(unittest.TestCase):

    def test_check_permutation_empty(self):
        assert check_permutation('', '') == True

    def test_check_permutation_empty_one(self):
        assert check_permutation('', 'dasda') == False

    def test_check_permutation_true(self):
        assert check_permutation('qwertyuiop', 'poiuytrewq') == True

    def test_check_permutation_false(self):
        assert check_permutation('asddasdasf', 'asdasdasef') == False


class TestUrlify(unittest.TestCase):

    def test_urlify_empty(self):
        assert urlify('') == ''

    def test_urlify_true(self):
        assert urlify('Mr 3ohn Smith   ') == 'Mr%203ohn%20Smith%20%20%20'

    def test_urlify_true_spaces(self):
        assert urlify('     ') == '%20%20%20%20%20'


class TestPalindromePermutation(unittest.TestCase):

    def test_palindrome_permutation_empty(self):
        assert palindrome_permutation('') == True

    def test_palindrome_permutation_true(self):
        assert palindrome_permutation('Tac t Coa') == True

    def test_palindrome_permutation_false(self):
        assert palindrome_permutation('Tac t Coaa') == False


class TestOneWay(unittest.TestCase):

    def test_one_way_remove(self):
        assert one_way('pale', 'ple') == True

    def test_one_way_insert(self):
        assert one_way('pale', 'pales') == True

    def test_one_way_replace(self):
        assert one_way('pale', 'bale') == True

    def test_one_way_false(self):
        assert one_way('pale', 'bake') == False

    def test_one_way_one_char(self):
        assert one_way('a', 'ab') == True

    def test_one_way_two_char(self):
        assert one_way('a', 'abc') == False

    def test_one_way_empty(self):
        assert one_way('', '') == True


class TestOneWayV2(unittest.TestCase):

    def test_one_way_remove(self):
        assert one_way_v2('pale', 'ple') == True

    def test_one_way_insert(self):
        assert one_way_v2('pale', 'pales') == True

    def test_one_way_replace(self):
        assert one_way_v2('pale', 'bale') == True

    def test_one_way_false(self):
        assert one_way_v2('pale', 'bake') == False

    def test_one_way_one_char(self):
        assert one_way_v2('a', 'ab') == True

    def test_one_way_two_char(self):
        assert one_way_v2('a', 'abc') == False

    def test_one_way_two_empty(self):
        assert one_way_v2('', '') == True


class TestStringCompression(unittest.TestCase):

    def test_string_compression_true(self):
        assert string_compression('aabcccccaaa') == 'a2b1c5a3'

    def test_string_compression_single(self):
        assert string_compression('aaaaaaaaaa') == 'a10'

    def test_string_compression_different(self):
        assert string_compression('abcdefg') == 'a1b1c1d1e1f1g1'

    def test_string_compression_one(self):
        assert string_compression('a') == 'a1'

    def test_string_compression_empty(self):
        assert string_compression('') == ''


class TestRotateMatrix(unittest.TestCase):

    def test_rotate_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert rotate_matrix(matrix) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_rotate_matrix_small(self):
        matrix = [[1, 2], [3, 4]]
        assert rotate_matrix(matrix) == [[3, 1], [4, 2]]

    def test_rotate_matrix_single(self):
        matrix = [[1]]
        assert rotate_matrix(matrix) == [[1]]


class TestZeroMatrix(unittest.TestCase):

    def test_zero_matrix(self):
        matrix = [[1, 0, 3], [4, 5, 0], [7, 8, 9]]
        assert zero_matrix(matrix) == [[0, 0, 0], [0, 0, 0], [7, 0, 0]]

    def test_zero_matrix_mn(self):
        matrix = [[1, 0, 3, 4], [4, 5, 0, 9], [7, 8, 9, 12]]
        assert zero_matrix(matrix) == [[0, 0, 0, 0], [0, 0, 0, 0], [7, 0, 0, 12]]

    def test_zero_matrix_one_col(self):
        matrix = [[1], [0], [2], [4], [4]]
        assert zero_matrix(matrix) == [[0], [0], [0], [0], [0]]

    def test_zero_matrix_one_row(self):
        matrix = [[1, 2, 3, 0]]
        assert zero_matrix(matrix) == [[0, 0, 0, 0]]

    def test_zero_matrix_no_zero(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert zero_matrix(matrix) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class TestZeroMatrixO1Space(unittest.TestCase):

    def test_zero_o1_space_matrix(self):
        matrix = [[1, 0, 3], [4, 5, 0], [7, 8, 9]]
        assert zero_matrix_o1_space(matrix) == [[0, 0, 0], [0, 0, 0], [7, 0, 0]]

    def test_zero_matrix_o1_space_mn(self):
        matrix = [[1, 0, 3, 4], [4, 5, 0, 9], [7, 8, 9, 12]]
        assert zero_matrix_o1_space(matrix) == [[0, 0, 0, 0], [0, 0, 0, 0], [7, 0, 0, 12]]

    def test_zero_matrix_o1_space_one_col(self):
        matrix = [[1], [0], [2], [4], [4]]
        assert zero_matrix_o1_space(matrix) == [[0], [0], [0], [0], [0]]

    def test_zero_matrix_o1_space_one_row(self):
        matrix = [[1, 2, 3, 0]]
        assert zero_matrix_o1_space(matrix) == [[0, 0, 0, 0]]

    def test_zero_matrix_o1_space_no_zero(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        assert zero_matrix_o1_space(matrix) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class TestStringRotation(unittest.TestCase):

    def test_string_rotation_true(self):
        assert string_rotation('waterbottle', 'erbottlewat') == True

    def test_string_rotation_false(self):
        assert string_rotation('waterbottle', 'erbottletaw') == False

    def test_string_rotation_empty(self):
        assert string_rotation('', '') == True

    def test_string_rotation_single(self):
        assert string_rotation('a', 'a') == True


if __name__ == '__main__':
    unittest.main()
