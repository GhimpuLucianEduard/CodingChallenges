import unittest

from challenges.ctci.stacks_and_queues import *


class TestMinStack():

    def setUp(self):
        self.minStack = self.getImplementation()

    def getImplementation(self):
        pass

    def test_push(self):
        self.minStack.push(10)
        assert self.minStack.last.data == 10
        self.minStack.push(14)
        assert self.minStack.last.data == 14
        assert self.minStack.last.next.data == 10

    def test_push_min(self):
        self.minStack.push(10)
        assert self.minStack.min() == 10
        self.minStack.push(14)
        assert self.minStack.min() == 10

    def test_push_pop(self):
        self.minStack.push(10)
        assert self.minStack.last.data == 10
        self.minStack.push(1)
        self.minStack.push(102)
        self.minStack.push(45)
        assert self.minStack.last.data == 45

        self.minStack.pop()
        assert self.minStack.last.data == 102
        self.minStack.pop()
        assert self.minStack.last.data == 1
        self.minStack.pop()
        assert self.minStack.last.data == 10

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.minStack.pop()

    def test_push_peek(self):
        self.minStack.push(10)
        assert self.minStack.peek().data == 10
        self.minStack.push(1)
        assert self.minStack.peek().data == 1

    def test_all(self):
        self.minStack.push(10)
        assert self.minStack.peek().data == 10
        assert self.minStack.min() == 10
        self.minStack.pop()

        with self.assertRaises(Exception):
            self.minStack.min()

        self.minStack.push(10)
        self.minStack.push(100)
        self.minStack.push(2)
        self.minStack.push(25)

        assert self.minStack.min() == 2


class TestMinNodeStack(TestMinStack, unittest.TestCase):
    def getImplementation(self):
        return MinNodeStack()


class TestDoubleStackMinStack(TestMinStack, unittest.TestCase):
    def getImplementation(self):
        return DoubleStackMinStack()


if __name__ == '__main__':
    unittest.main()
