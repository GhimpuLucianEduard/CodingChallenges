"""
101. Symmetric Tree

Given a binary tree, check whether
it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def symmetric_tree_rec(root):
    if not root:
        return True

    return symmetric_tree_rec_aux(root.left, root.right)


def symmetric_tree_rec_aux(left, right):
    if not left and not right:
        return True

    if not left or not right:
        return False

    left_right_check = symmetric_tree_rec_aux(left.left, right.right)
    right_left_check = symmetric_tree_rec_aux(left.right, right.left)

    return left.val == right.val and left_right_check and right_left_check


def symmetric_tree_iter(root):
    if not root:
        return True

    queue = [root, root]
    while len(queue) > 0:
        left = queue.pop()
        right = queue.pop()
        if not left and not right:
            continue
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)

    return True


class TestSymmetricTreeRec(unittest.TestCase):
    def test_symmetric_tree_empty(self):
        self.assertEqual(symmetric_tree_rec(None), True)

    def test_symmetric_tree_leetcode1(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        self.assertEqual(symmetric_tree_rec(tree), True)

    def test_symmetric_tree_leetcode2(self):
        tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        self.assertEqual(symmetric_tree_rec(tree), False)

    def test_symmetric_tree_leetcode3(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))
        self.assertEqual(symmetric_tree_rec(tree), False)

class TestSymmetricTreeIter(unittest.TestCase):
    def test_symmetric_tree_empty(self):
        self.assertEqual(symmetric_tree_iter(None), True)

    def test_symmetric_tree_leetcode1(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        self.assertEqual(symmetric_tree_iter(tree), True)

    def test_symmetric_tree_leetcode2(self):
        tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        self.assertEqual(symmetric_tree_iter(tree), False)

    def test_symmetric_tree_leetcode3(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2)))
        self.assertEqual(symmetric_tree_iter(tree), False)