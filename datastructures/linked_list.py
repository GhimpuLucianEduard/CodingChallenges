class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_start(self, data):
        aux = Node(data)
        aux.next = self.head
        self.head = aux

    def append_to_end(self, data):
        aux = Node(data)

        if self.head is None:
            self.head = aux
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = aux

    def __len__(self):
        if self.head is None:
            return 0

        current = self.head
        size = 0
        while current is not None:
            current = current.next
            size += 1

        return size

    def remove(self, item):

        if self.head is None:
            raise Exception("Empty List")

        # remove head case
        if self.head.data == item:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None and current.next.data != item:
            current = current.next

        # we found the node
        if current is not None:
            current.next = current.next.next
