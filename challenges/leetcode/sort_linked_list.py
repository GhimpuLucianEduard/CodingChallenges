"""
148. Sort List

Given the head of a linked list,
return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn)
time and O(1) memory (i.e. constant space)?

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_linked_list(head):
    if not head or not head.next:
        return head

    mid_node = find_mid_node(head)
    right = sort_linked_list(mid_node.next)
    mid_node.next = None
    left = sort_linked_list(head)

    return merge(left, right)


def merge(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    new_list = ListNode
    new_head = new_list
    while head1 and head2:
        if head1.val <= head2.val:
            head1_next = head1.next
            new_list.next = head1
            head1 = head1_next
        else:
            head2_next = head2.next
            new_list.next = head2
            head2 = head2_next

        new_list = new_list.next

    new_list.next = head1 or head2

    new_head = new_head.next
    return new_head


def find_mid_node(head):
    # find list length
    list_len = 0

    cur = head
    while cur:
        list_len += 1
        cur = cur.next

    cur = head
    cur_len = 1
    while cur and cur_len < list_len // 2:
        cur = cur.next
        cur_len += 1

    return cur

class TestSortLinkedList(unittest.TestCase):
    def test_sort_linked_list(self):
        input_list = ListNode(4, ListNode(2, ListNode(1, ListNode(7))))
        sorted_list = sort_linked_list(input_list)
        self.assertEqual(1, sorted_list.val)
        self.assertEqual(2, sorted_list.next.val)
        self.assertEqual(4, sorted_list.next.next.val)
        self.assertEqual(7, sorted_list.next.next.next.val)

    def test_sort_linked_list_empty(self):
        input_list = None
        sorted_list = sort_linked_list(input_list)
        self.assertEqual(None, sorted_list)

    def test_sort_linked_list_single(self):
        input_list = ListNode(1)
        sorted_list = sort_linked_list(input_list)
        self.assertEqual(1, sorted_list.val)

    def test_sort_linked_list_leetcode1(self):
        input_list = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        sorted_list = sort_linked_list(input_list)
        self.assertEqual(1, sorted_list.val)
        self.assertEqual(2, sorted_list.next.val)
        self.assertEqual(3, sorted_list.next.next.val)
        self.assertEqual(4, sorted_list.next.next.next.val)
