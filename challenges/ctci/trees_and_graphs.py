import math
from collections import defaultdict, deque


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


class Graph:
    def __init__(self):
        self.nodes = []


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def route_between_nodes_dfs(node_a, node_b):
    """
    Given a directed graph, design an algorithm to find out
    whether there is a route between two nodes.
    :param node_a: First Node
    :param node_b: Second Node
    :return: True if there is a route between node_a and node_b, false otherwise

    DFS implementation
    """
    # use a map to check if we have visited a node or not
    return route_between_nodes_dfs_aux(node_a, node_b, defaultdict(bool))


def route_between_nodes_dfs_aux(node_a, node_b, visited_dict):
    """
    :param node_a: First Node
    :param node_b: Second Node
    :param visited_dict: Used to check if we have visited a node or not
    :return: True if there is a route between node_a and node_b, false otherwise

    DFS implementation
    """
    # we will do a simple DFS over the graph

    # base case, same node
    if node_a is node_b:
        return True

    # base case, check of there is  direct connection between node_a and node_b
    if node_b in node_a.neighbors:
        return True
    visited_dict[node_a.value] = True

    for node in node_a.neighbors:
        if node_b in node.neighbors:
            return True

        # node not visited
        if visited_dict[node.value] is not True:
            route_between_nodes_dfs_aux(node, node_b, visited_dict)

    return False


def route_between_nodes_bfs(node_a, node_b):
    """
    Given a directed graph, design an algorithm to find out
    whether there is a route between two nodes.
    :param node_a: First Node
    :param node_b: Second Node
    :return: True if there is a route between node_a and node_b, false otherwise

    BFS implementation
    """
    # we will do a simple BFS over the graph
    # use this map to check if we have visited a node or not
    visited_dict = defaultdict(bool)

    # base case, same node
    if node_a is node_b:
        return True

    queue = deque()
    queue.append(node_a)
    visited_dict[node_a.value] = True
    while len(queue) != 0:
        current_node = queue.pop()
        if current_node is node_b:
            return True

        for node in current_node.neighbors:
            if visited_dict[node.value] is False:
                visited_dict[node] = True
                queue.append(node)

    return False


def height(root):
    """
    Calculates the height of a binary tree
    :param root: root node
    :return: The height of the Tree or -1 if the Tree is None
    """
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


def minimal_tree(array):
    """
    Given a sorted (increasing order) array with unique integer elements, write an
    algorithm to create a binary search tree with minimal height.
    :param array: input array
    :return: a TreeNode as the root of the tree
    """

    # given the fact that the list is sorted, the middle element of the list
    # is the best candidate to be the root
    # we than select its left and right children with the same logic,
    # the middle element in the left partition and the middle element in the right partition

    if len(array) == 0:
        return None

    if len(array) == 1:
        return TreeNode(array[0])

    root_index = math.trunc(len(array) / 2)
    left_child = minimal_tree(array[:root_index])
    right_child = minimal_tree(array[root_index+1:])
    node = TreeNode(array[root_index])
    node.left = left_child
    node.right = right_child
    return node
