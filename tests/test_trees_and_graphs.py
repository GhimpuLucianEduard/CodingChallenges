import unittest


from challenges.ctci.trees_and_graphs import *


class TestRouteBetweenNodes(unittest.TestCase):

    def setUp(self):
        node1 = GraphNode(1)
        node2 = GraphNode(2)
        node3 = GraphNode(3)
        node4 = GraphNode(4)
        node5 = GraphNode(5)
        node6 = GraphNode(6)
        node7 = GraphNode(7)

        node1.neighbors.extend([node3, node4, node5])
        node2.neighbors.extend([node1, node3])
        node3.neighbors.append(node6)
        node4.neighbors.append(node7)
        node5.neighbors.append(node4)
        node7.neighbors.append(node1)

        self.graph = Graph()
        self.graph.nodes.extend([node1, node2, node3, node4, node5, node6, node7])

    def test_route_between_nodes_dfs(self):
        self.assertTrue(route_between_nodes_dfs(self.graph.nodes[0], self.graph.nodes[6]))

    def test_route_between_nodes_dfs_no_route(self):
        self.assertFalse(route_between_nodes_dfs(self.graph.nodes[5], self.graph.nodes[6]))

    def test_route_between_nodes_dfs_same_node(self):
        self.assertTrue(route_between_nodes_dfs(self.graph.nodes[0], self.graph.nodes[0]))

    def test_route_between_nodes_bfs(self):
        self.assertTrue(route_between_nodes_bfs(self.graph.nodes[0], self.graph.nodes[6]))

    def test_route_between_nodes_bfs_no_route(self):
        self.assertFalse(route_between_nodes_bfs(self.graph.nodes[5], self.graph.nodes[6]))

    def test_route_between_nodes_bfs_same_node(self):
        self.assertTrue(route_between_nodes_bfs(self.graph.nodes[0], self.graph.nodes[0]))


class TestMinimalTree(unittest.TestCase):

    def test_minimal_tree_empty(self):
        self.assertEqual(minimal_tree([]), None)

    def test_minimal_tree_single(self):
        root = minimal_tree([1])
        self.assertEqual(height(root), 0)

    def test_minimal_tree_multiples(self):
        root = minimal_tree([1, 2, 3, 7, 100, 2010, 100000])
        self.assertEqual(height(root), 2)

    def test_minimal_tree_multiples_large(self):
        array = range(0, 1024)
        root = minimal_tree(array)
        self.assertEqual(height(root), 10)


class TestListOfDepths(unittest.TestCase):

    def test_list_of_depths_empty(self):
        self.assertEqual(list_of_depths(None), {})

    def test_list_of_depths_one_node(self):
        lists = list_of_depths(TreeNode(10))
        self.assertEqual(len(lists[0]), 1)

    def test_list_of_depths_full_tree(self):
        root = create_bt_from_array([1, 2, 3, 4, 5, 6, 7, 8]).root
        lists = list_of_depths(root)
        self.assertEqual(len(lists[0]), 1)
        self.assertEqual(len(lists[1]), 2)
        self.assertEqual(len(lists[2]), 4)
        self.assertEqual(len(lists[3]), 1)


class TestCheckBalanced(unittest.TestCase):

    def test_check_balanced_empty(self):
        self.assertEqual(check_balanced(None), True)

    def test_check_balanced_single(self):
        self.assertEqual(check_balanced(TreeNode(2)), True)

    def test_check_balanced_multiples(self):
        root = TreeNode(1)
        left1 = TreeNode(2)
        left2 = TreeNode(3)
        left3 = TreeNode(4)
        left1.left = left2
        left2.left = left3
        root.left = left1
        self.assertEqual(check_balanced(root), False)

    def test_check_balanced_multiples_mixed(self):
        root = TreeNode(1)
        left1 = TreeNode(2)
        right1 = TreeNode(21)
        right2 = TreeNode(22)
        left2 = TreeNode(3)
        left3 = TreeNode(4)
        left1.left = left2
        left2.left = left3
        root.left = left1
        root.right = right1
        right1.right = right2
        left2.right = TreeNode(9)
        left1.right = TreeNode(10)

        self.assertEqual(check_balanced(root), True)


class TestValidateBST(unittest.TestCase):

    def test_validate_bst_empty(self):
        self.assertEqual(validate_bst(None), True)

    def test_validate_bst_single(self):
        self.assertEqual(validate_bst(TreeNode(1)), True)

    def test_validate_bst_multiples(self):
        root = create_bt_from_array([10, 8, 12, 6, 9, 11, 15]).root
        self.assertEqual(validate_bst(root), True)

    def test_validate_bst_multiples_false(self):
        root = create_bt_from_array([10, 8, 12, 6, 9, 11, 15, 23]).root
        self.assertEqual(validate_bst(root), False)


class TestSuccessor(unittest.TestCase):

    def test_successor_empty(self):
        self.assertEqual(successor(None), None)

    def test_successor_single(self):
        self.assertEqual(successor(TreeNodeWithParent(1)), None)

    def test_successor_multiples(self):
        root = TreeNodeWithParent(10)
        left1 = TreeNodeWithParent(8)
        left1.parent = root
        root.left = left1

        left2 = TreeNodeWithParent(6)
        left2.parent = left1
        left1.left = left2

        right2 = TreeNodeWithParent(9)
        right2.parent = left1
        left1.right = right2

        self.assertEqual(successor(right2).value, 10)
        self.assertEqual(successor(left2).value, 8)

    def test_successor_multiples_right_child(self):
        root = TreeNodeWithParent(10)
        right1 = TreeNodeWithParent(13, root)
        root.right = right1

        right1.right = TreeNodeWithParent(24, right1)
        right2 = TreeNodeWithParent(12, right1)
        right2.left = TreeNodeWithParent(11, right2)
        right1.left = right2

        self.assertEqual(successor(root).value, 11)
        self.assertEqual(successor(right1).value, 24)
        self.assertEqual(successor(right2).value, 13)


if __name__ == '__main__':
    unittest.main()
