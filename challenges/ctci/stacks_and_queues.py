from collections import deque


class MinNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.minValue = None


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MinStack:
    """
    Stack Min: How would you design a stack which,
    in addition to push and pop, has a function min
    which returns the minimum element?
    Push, pop and min should all operate in 0(1) time.
    """

    def min(self):
        pass

    def push(self, data):
        pass

    def peek(self):
        pass

    def pop(self):
        pass


class MinNodeStack(MinStack):
    """
    Implementation with MinNode, where each node holds the min value
    """

    def __init__(self):
        self.last = None

    def peek(self):
        if self.last is None:
            raise Exception("Stack empty")
        return self.last

    def min(self):
        return self.peek().minValue

    def push(self, data):

        new_node = MinNode(data)

        if self.last is None:
            new_node.minValue = new_node.data
            self.last = new_node
            return

        new_node.minValue = self.min() if self.min() < new_node.data else new_node.data
        new_node.next = self.last
        self.last = new_node

    def pop(self):
        if self.last is None:
            raise Exception("Stack empty")

        self.last = self.last.next
        return self.last


class DoubleStackMinStack(MinStack):
    """
    Keep the min values in a separate stack
    """

    def __init__(self):
        self.last = None
        self.min_stack = deque()

    def min(self):
        return self.min_stack[-1]

    def push(self, data):
        node = Node(data)
        if self.last is None:
            self.last = node
            self.min_stack.append(data)
            return

        if self.min() > data:
            self.min_stack.append(data)

        node.next = self.last
        self.last = node

    def peek(self):
        if self.last is None:
            raise Exception("Stack empty")

        return self.last

    def pop(self):
        if self.last is None:
            raise Exception("Stack empty")

        if self.last.data == self.min():
            self.min_stack.pop()

        self.last = self.last.next
        return self.last
