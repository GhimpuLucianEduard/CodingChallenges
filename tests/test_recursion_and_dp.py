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

if __name__ == '__main__':
    unittest.main()
