import math
from collections import *
from datastructures.linked_list import *


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


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)

        current_node = self.root
        if current_node is None:
            self.root = new_node
            return self.root

        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return new_node

            if current.right is None:
                current.right = new_node
                return new_node

            queue.append(current.left)
            queue.append(current.right)


def create_bt_from_array(array):
    """
    Not in the book, used for testing
    :param array: input array
    :return: root node of the tree
    """
    tree = BinaryTree()

    for element in array:
        tree.insert(element)

    return tree


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
    right_child = minimal_tree(array[root_index + 1:])
    node = TreeNode(array[root_index])
    node.left = left_child
    node.right = right_child
    return node


def list_of_depths_aux(node, lists, level):
    lists[level].append_to_end(node.value)
    if node.left:
        list_of_depths_aux(node.left, lists, level + 1)
    if node.right:
        list_of_depths_aux(node.right, lists, level + 1)


def list_of_depths(root):
    """
    List of Depths: Given a binary tree, design an algorithm which
    creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
    :param root: input tree
    :return: list of lists for each level
    """

    if root is None:
        return {}

    lists = defaultdict(LinkedList)
    list_of_depths_aux(root, lists, 0)
    return lists


def check_balanced_aux(root):
    if root is None:
        return -1

    left_height = check_balanced_aux(root.left)
    if left_height is float('-inf'):
        return float('-inf')

    right_height = check_balanced_aux(root.right)
    if right_height is float('-inf'):
        return float('-inf')

    diff = left_height - right_height
    if abs(diff) > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1


def check_balanced(root):
    """
    Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that
    the heights of the two subtrees of any node never differ by more than one.
    :param root: input tree
    :return: True if the tree is balanced, false otherwise
    """
    return check_balanced_aux(root) != float('-inf')


def validate_bst_aux(root, min, max):
    if root is None:
        return True

    if (min is not None and root.value <= min) or (max is not None and root.value > max):
        return False

    if not validate_bst_aux(root.left, min, root.value) or not validate_bst_aux(root.right, root.value, max):
        return False

    return True


def validate_bst(root):
    """
    Implement a function to check if a binary tree is a binary search tree.
    :param root: input tree
    :return: True if tree is bst, false otherwise
    """
    return validate_bst_aux(root, None, None)


class TreeNodeWithParent(TreeNode):
    def __init__(self, value, parent=None):
        super().__init__(value)
        self.parent = parent


def successor(node):
    """
    Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent.
    :param node: input node
    :return: next successor for input node
    """

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
