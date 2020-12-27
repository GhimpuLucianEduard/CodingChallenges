"""
4.6

Write an algorithm to find the "next" node of a given node in a BST.
You may assume that each node as a link to the parent node
"""
import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def successor(node):
    # base case, single node
    if node is None:
        return None

    # node has a right child
    if node.right:
        child = node.right
        while child.left:
            child = child.left
        return child

    current = node
    parent = node.parent
    if parent:
        while parent.parent and parent.left != current:
            current = parent
            parent = current.parent

    return parent


class TestSuccessor(unittest.TestCase):
    def test_successor(self):
        root = TreeNode(10)
        left1 = TreeNode(8)
        left1.parent = root
        root.left = left1

        left2 = TreeNode(6)
        left2.parent = left1
        left1.left = left2

        right2 = TreeNode(9)
        right2.parent = left1
        left1.right = right2

        self.assertEqual(10, successor(right2).val)
        self.assertEqual(8, successor(left2).val)
        self.assertEqual(None, successor(root))
