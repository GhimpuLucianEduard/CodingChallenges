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


class TestPalindromePermutation:

    def test_palindrome_permutation_empty(self):
        assert palindrome_permutation('') == True

    def test_palindrome_permutation_true(self):
        assert palindrome_permutation('Tac t Coa') == True

    def test_palindrome_permutation_false(self):
        assert palindrome_permutation('Tac t Coaa') == False


if __name__ == '__main__':
    unittest.main()
