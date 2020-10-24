import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bt_max_path_sum(root):
    """
    Given a non-empty binary tree, find the maximum path sum.
    For this problem, a path is defined as any sequence of nodes
    from some starting node to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need to go through the root.

    Examples:

    Input: [1,2,3]
    Output: 6

    Input: [-10,9,20,null,null,15,7]
    Output: 42

    :param root: input tree
    :return: the max sum
    """
    max_path = float("-inf")

    def bt_max_path_sum_aux(node):
        nonlocal max_path
        if node is None:
            return float("-inf")

        left_sum = max(bt_max_path_sum_aux(node.left), 0)
        right_sum = max(bt_max_path_sum_aux(node.right), 0)

        max_path = max(max_path, right_sum + left_sum + node.val)
        return node.val + max(left_sum, right_sum)

    bt_max_path_sum_aux(root)
    return max_path


class TestBtMaxPathSum(unittest.TestCase):

    def test_bt_max_path_sum_empty(self):
        self.assertEqual(bt_max_path_sum(None), float("-inf"))

    def test_bt_max_path_sum_single(self):
        self.assertEqual(bt_max_path_sum(TreeNode(-3)), -3)

    def test_bt_max_path_sum_leetcode_1(self):
        self.assertEqual(bt_max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))), 6)

    def test_bt_max_path_sum_leetcode_2(self):
        tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(bt_max_path_sum(tree), 42)

    def test_bt_max_path_sum_leetcode_3(self):
        tree = TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))
        self.assertEqual(bt_max_path_sum(tree), 3)
