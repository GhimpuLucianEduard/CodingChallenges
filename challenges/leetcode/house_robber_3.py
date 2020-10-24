"""
337. House Robber III

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place
forms a binary tree". It will automatically contact the police if two
directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9

Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def house_robber_3(root):
    return max(house_robber_3_rec(root))


def house_robber_3_rec(root):
    if root is None:
        return [0, 0]

    left = house_robber_3_rec(root.left)
    right = house_robber_3_rec(root.right)

    return [root.val + left[1] + right[1], max(left) + max(right)]


class TestHouseRobber3(unittest.TestCase):

    def test_house_robber_3_empty(self):
        self.assertEqual(house_robber_3(None), 0)

    def test_house_robber_3_single(self):
        self.assertEqual(house_robber_3(TreeNode(1)), 1)

    def test_house_robber_3_leetcode1(self):
        tree = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
        self.assertEqual(house_robber_3(tree), 7)

    def test_house_robber_3_leetcode2(self):
        tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
        self.assertEqual(house_robber_3(tree), 9)
