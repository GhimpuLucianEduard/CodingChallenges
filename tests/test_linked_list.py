import unittest

from datastructures.linked_list import *


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_len_empty(self):
        self.assertEqual(len(self.list), 0)

    def test_len_single(self):
        node = Node(1)
        self.list.head = node
        self.assertEqual(len(self.list), 1)

    def test_len_non_empty(self):
        node3 = Node(3)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        self.list.head = node1
        self.assertEqual(len(self.list), 3)

    def test_append_to_start(self):
        node = Node(1)
        self.list.head = node
        self.list.append_to_start(2)
        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.head.next.data, 1)

    def test_append_to_start_multiple(self):
        node = Node(1)
        self.list.head = node
        self.list.append_to_start(2)
        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.head.next.data, 1)
        self.list.append_to_start(10)
        self.list.append_to_start(11)
        self.list.append_to_start(12)
        self.assertEqual(self.list.head.data, 12)
        self.assertEqual(self.list.head.next.data, 11)

    def test_append_to_end_head(self):
        self.list.append_to_end(2)
        self.assertEqual(self.list.head.data, 2)

    def test_append_to_end(self):
        node = Node(1)
        self.list.head = node
        self.list.append_to_end(2)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 2)

    def test_append_to_end_multiple(self):
        node = Node(1)
        self.list.head = node
        self.list.append_to_end(2)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 2)
        self.list.append_to_end(10)
        self.list.append_to_end(11)
        self.list.append_to_end(12)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.next.data, 2)

    def test_remove_empty(self):
        with self.assertRaises(Exception):
            self.list.remove(2)

    def test_remove_single_element(self):
        node = Node(1)
        self.list.head = node
        self.assertEqual(self.list.head.data, 1)
        self.list.remove(1)
        self.assertEqual(self.list.head, None)

    def test_remove_multiple_elements(self):
        node6 = Node(6, None)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        self.list.head = node1
        self.list.remove(4)
        self.assertEqual(self.list.head.next.next.next.data, 5)

    def test_remove_multiple_elements_last(self):
        node6 = Node(6, None)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        self.list.head = node1
        self.list.remove(6)
        self.assertEqual(self.list.head.next.next.next.next.data, 5)

    def test_integration_len_append_remove(self):
        self.assertEqual(len(self.list), 0)
        with self.assertRaises(Exception):
            self.list.remove(2)

        for i in range(0, 20):
            self.list.append_to_end(i)

        self.assertEqual(len(self.list), 20)

        for i in range(0, 10):
            self.list.remove(i)

        self.assertEqual(len(self.list), 10)

        for i in range(0, 100):
            self.list.append_to_start(i)

        for i in range(0, 50):
            self.list.remove(i)

        self.assertEqual(len(self.list), 60)


if __name__ == '__main__':
    unittest.main()
