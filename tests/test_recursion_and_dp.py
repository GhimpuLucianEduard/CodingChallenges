import unittest

from challenges.ctci.recursion_and_dp import *


class TestTripleStep(unittest.TestCase):
    def test_triple_step_f0(self):
        self.assertEqual(triple_step(0), 1)

    def test_triple_step_f1(self):
        self.assertEqual(triple_step(1), 1)

    def test_triple_step_f2(self):
        self.assertEqual(triple_step(2), 2)

    def test_triple_step_f3(self):
        self.assertEqual(triple_step(3), 4)

    def test_triple_step_f5(self):
        self.assertEqual(triple_step(5), 13)


class TestRobotInAGrid(unittest.TestCase):

    def test_robot_in_a_grid_n0(self):
        self.assertEqual(robot_in_a_grid([[]]), [])

    def test_robot_in_a_grid_n1(self):
        self.assertEqual(robot_in_a_grid([[0]]), [(0, 0)])

    def test_robot_in_a_grid_n2(self):
        self.assertEqual(robot_in_a_grid([[0, 0], [0, 0]]), [(0, 0), (1, 0), (1, 1)])

    def test_robot_in_a_grid_n5(self):
        grid_4n = [[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]
        self.assertEqual(robot_in_a_grid(grid_4n),
                         [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                          (4, 1), (4, 2), (4, 3), (4, 4)])

    def test_robot_in_a_grid_n5_obstacles(self):
        grid_4n = [[0, 0, 0, 0, 0],
                   [None, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, None, 0]]

        self.assertEqual(robot_in_a_grid(grid_4n),
                         [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1),
                          (3, 2), (3, 3), (3, 4), (4, 4)])


class TestMagicIndex(unittest.TestCase):

    def test_magic_index_empty(self):
        self.assertEqual(magic_index([]), -1)

    def test_magic_index_one_element_false(self):
        self.assertEqual(magic_index([2]), -1)

    def test_magic_index_one_element_true(self):
        self.assertEqual(magic_index([0]), 0)

    def test_magic_index_multiples_elements_true(self):
        self.assertEqual(magic_index([-2, -1, 0, 3, 7, 9]), 3)

    def test_magic_index_multiples_elements_false(self):
        self.assertEqual(magic_index([-2, -1, 0, 2, 7, 9]), -1)


class TestMagicIndexFollowup(unittest.TestCase):

    def test_magic_followup_index_empty(self):
        self.assertEqual(magic_index_followup([]), -1)

    def test_magic_index_followup_one_element_false(self):
        self.assertEqual(magic_index_followup([2]), -1)

    def test_magic_index_followup_one_element_true(self):
        self.assertEqual(magic_index_followup([0]), 0)

    def test_magic_index_followup_elements_true(self):
        self.assertEqual(magic_index_followup([-13, -12, 1, 1, 1, 1, 6, 7, 10, 29, 30]), 6)

    def test_magic_index_followup_elements_false(self):
        self.assertEqual(magic_index_followup([-2, -1, 0, 2, 7, 9]), -1)


class TestPowerSet(unittest.TestCase):
    def test_power_set_empty(self):
        self.assertEqual(power_set([]), [])

    def test_power_set_single(self):
        self.assertEqual(power_set([1]), [[], [1]])

    def test_power_set_4(self):
        print(power_set([1, 2, 3, 4]))
        self.assertEqual(len(power_set([1, 2, 3, 4])), 16)

if __name__ == '__main__':
    unittest.main()
