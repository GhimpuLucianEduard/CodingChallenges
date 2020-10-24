"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers_linked_list(l1, l2):
    if l1 is None and l2 is None:
        return None

    if l2 is None:
        return l1
    if l1 is None:
        return l2

    l1_node = l1
    l2_node = l2

    l3 = None
    l3_first = None

    reminder = 0

    while l1_node is not None or l2_node is not None:
        if l1_node is None:
            l1_value = 0
            l1_next = None
        else:
            l1_value = l1_node.val
            l1_next = l1_node.next

        if l2_node is None:
            l2_value = 0
            l2_next = None
        else:
            l2_value = l2_node.val
            l2_next = l2_node.next

        l3_value = (reminder + l1_value + l2_value) % 10
        reminder = (reminder + l1_value + l2_value) // 10

        if l3 is None:
            l3 = ListNode(l3_value, None)
            l3_first = l3
        else:
            l3.next = ListNode(l3_value, None)
            l3 = l3.next

        l1_node = l1_next
        l2_node = l2_next

    if reminder is not 0:
        l3.next = ListNode(reminder, None)

    return l3_first


class TestAddTwoNumbersLinkedList(unittest.TestCase):

    def test_add_two_numbers_linked_list_both_none(self):
        self.assertEqual(add_two_numbers_linked_list(None, None), None)

    def test_add_two_numbers_linked_list_l2_none(self):
        l1 = ListNode
        self.assertEqual(add_two_numbers_linked_list(l1, None), l1)

    def test_add_two_numbers_linked_list_l1_none(self):
        l2 = ListNode
        self.assertEqual(add_two_numbers_linked_list(None, l2), l2)

    def test_add_two_numbers_linked_list_leetcode1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3, None)))
        l2 = ListNode(5, ListNode(6, ListNode(4, None)))
        l3 = add_two_numbers_linked_list(l1, l2)
        self.assertEqual(l3.val, 7)
        self.assertEqual(l3.next.val, 0)
        self.assertEqual(l3.next.next.val, 8)
        self.assertEqual(l3.next.next.next, None)

    def test_add_two_numbers_linked_list_leetcode2(self):
        l1 = ListNode(0, None)
        l2 = ListNode(0, None)
        l3 = add_two_numbers_linked_list(l1, l2)
        self.assertEqual(l3.val, 0)
        self.assertEqual(l3.next, None)

    def test_add_two_numbers_linked_list_leetcode3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
        l3 = add_two_numbers_linked_list(l1, l2)
        Output: [8, 9, 9, 9, 0, 0, 0, 1]

        self.assertEqual(l3.val, 8)
        self.assertEqual(l3.next.val, 9)
        self.assertEqual(l3.next.next.val, 9)
        self.assertEqual(l3.next.next.next.val, 9)
        self.assertEqual(l3.next.next.next.next.val, 0)
        self.assertEqual(l3.next.next.next.next.next.val, 0)
        self.assertEqual(l3.next.next.next.next.next.next.val, 0)
        self.assertEqual(l3.next.next.next.next.next.next.next.val, 1)
        self.assertEqual(l3.next.next.next.next.next.next.next.next, None)
