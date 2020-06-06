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

if __name__ == '__main__':
    unittest.main()