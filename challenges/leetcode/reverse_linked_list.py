"""
206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list_rec(head):
    if head is None:
        return None

    if head.next is None:
        return head

    return reverse_linked_list_rec_aux(head, None)


def reverse_linked_list_rec_aux(head, prev):
    if head is None:
        return prev

    tmp = head.next
    head.next = prev
    return reverse_linked_list_rec_aux(tmp, head)


def reverse_linked_list_iter(head):
    if head is None:
        return None

    if head.next is None:
        return head

    prev = None
    while head is not None:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp

    return prev

class TestReverseLinkedListRec(unittest.TestCase):

    def test_reverse_linked_list_rec_empty(self):
        self.assertEqual(reverse_linked_list_rec(None), None)

    def test_reverse_linked_list_rec_single(self):
        l1 = ListNode(1, None)
        l2 = reverse_linked_list_rec(l1)
        self.assertEqual(l2.val, 1)
        self.assertEqual(l2.next, None)

    def test_reverse_linked_list_rec_leetcode(self):
        l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        l2 = reverse_linked_list_rec(l1)
        self.assertEqual(l2.val, 5)
        self.assertEqual(l2.next.val, 4)
        self.assertEqual(l2.next.next.val, 3)
        self.assertEqual(l2.next.next.next.val, 2)
        self.assertEqual(l2.next.next.next.next.val, 1)
        self.assertEqual(l2.next.next.next.next.next, None)

class TestReverseLinkedListIter(unittest.TestCase):

    def test_reverse_linked_list_iter_empty(self):
        self.assertEqual(reverse_linked_list_iter(None), None)

    def test_reverse_linked_list_iter_single(self):
        l1 = ListNode(1, None)
        l2 = reverse_linked_list_iter(l1)
        self.assertEqual(l2.val, 1)
        self.assertEqual(l2.next, None)

    def test_reverse_linked_list_iter_leetcode(self):
        l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
        l2 = reverse_linked_list_iter(l1)
        self.assertEqual(l2.val, 5)
        self.assertEqual(l2.next.val, 4)
        self.assertEqual(l2.next.next.val, 3)
        self.assertEqual(l2.next.next.next.val, 2)
        self.assertEqual(l2.next.next.next.next.val, 1)
        self.assertEqual(l2.next.next.next.next.next, None)