import unittest

from datastructures.trees import *


class TestTopView(unittest.TestCase):
    def test_top_view(self):
        test_value = create_bst_from_array([1, 2, 5, 3, 6, 4])
        level_order(test_value.root)


if __name__ == '__main__':
    unittest.main()
