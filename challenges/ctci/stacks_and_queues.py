from collections import deque


# N.B. instead of implementing a vanilla stack, I will use deque to simulate it

class Stack:

    def push(self, data):
        pass

    def pop(self):
        pass

    def peek(self):
        pass


class Queue:

    def append(self, data):
        pass

    def remove(self):
        pass

    def peek(self):
        pass


class MinNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.minValue = None


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class MinStack(Stack):
    """
    Stack Min: How would you design a stack which,
    in addition to push and pop, has a function min
    which returns the minimum element?
    Push, pop and min should all operate in 0(1) time.
    """

    def min(self):
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


class StackOfPlates(Stack):
    """
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
    threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
    composed of several stacks and should create a new stack once the previous one exceeds capacity.
    SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
    (that is, pop () should return the same values as it would if there were just a single stack).
    FOLLOW UP
    Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.
    """

    def __init__(self, capacity):
        """
        We will mock the stack using a deque
        The stacks will be kept in a list of stacks
        :param capacity: the capacity for each stack
        """
        self.stack_capacity = capacity
        self.last = None
        self.stacks = []

    def push(self, data):
        # create a new stack when list of stacks is empty
        if len(self.stacks) == 0:
            self.stacks.append(deque())

        # check if we have a available stack
        for stack in self.stacks:
            if len(stack) < self.stack_capacity:
                stack.append(data)
                self.last = data
                return

        # no stack available, append new stack with element
        new_stack = deque()
        new_stack.append(data)
        self.stacks.append(new_stack)

    def pop(self):
        if len(self.stacks) == 0:
            raise Exception("Stack empty")

        last_stack = self.stacks[-1]
        data = last_stack.pop()
        # remove the last stack if empty
        if len(last_stack) == 0:
            self.stacks.pop()

        return data

    def pop_at(self, index):
        if index >= len(self.stacks) or index < 0:
            raise Exception("Stack empty")

        # normal pop if index == len - 1
        if index == len(self.stacks) - 1:
            return self.pop()

        data = self.stacks[index].pop()

        if len(self.stacks[index]) == 0:
            self.stacks.pop()
            return data

        # there are no other stacks after this one, return the element
        if len(self.stacks[index]) < 4:
            return data

        # shift elements, we can do this thanks of the deque
        # if we cannot use deque, we need to implement a
        # remove_bottom_element in the stack implementation
        for i in range(index, len(self.stacks) - 1):
            if len(self.stacks[i + 1]) > 0:
                self.stacks[i].append(self.stacks[i + 1].popleft())
            if len(self.stacks[i + 1]) == 0:
                return self.stacks.pop()

        return data


class QueueWithTwoStacks(Queue):
    """
    Implement a MyQueue class which implements a queue using two stacks

    We will use 2 deque to simulate 2 stacks
    A main_stack which is used to hold the element in the popper order
    A aux_stack used to move the elements in the right order when pushing new elements
    """

    def __init__(self):
        super().__init__()
        self.main_stack = deque()
        self.aux_stack = deque()

    def push(self, data):

        if len(self.main_stack) == 0:
            self.main_stack.append(data)
            return

        while len(self.main_stack) != 0:
            self.aux_stack.append(self.main_stack.pop())

        self.main_stack.append(data)
        while len(self.aux_stack) != 0:
            self.main_stack.append(self.aux_stack.pop())

    def peek(self):
        if len(self.main_stack) == 0:
            raise Exception("Stack empty")

        return self.main_stack[len(self.main_stack) - 1]

    def pop(self):
        if len(self.main_stack) == 0:
            raise Exception("Stack empty")

        return self.main_stack.pop()


class SortingStack(Stack):
    """
    Not in the book, accidentally implemented it
    It's basically a sorted stack where the min value is always on top
    """

    def __init__(self):
        self.last = None

    def push(self, data):

        node = Node(data)

        # base case
        if self.last is None:
            self.last = node
            return

        # value to append is min value
        if node.data < self.last.data:
            node.next = self.last
            self.last = node
            return

        # move all smaller elements in aux stack
        aux_stack = deque()
        while node.data > self.last.data:
            aux_stack.append(self.last)
            self.last = self.last.next
            if self.last is None:
                break

        node.next = self.last
        self.last = node

        # move back smaller elements
        while len(aux_stack) != 0:
            aux_node = aux_stack.pop()
            aux_node.next = self.last
            self.last = aux_node

    def pop(self):
        if self.last is None:
            raise Exception("Stack empty")

        node = self.last
        self.last = node.next
        return node

    def peek(self):
        if self.last is None:
            raise Exception("Stack empty")

        return self.last.data

    def is_empty(self):
        return self.last is None


def sort_stack(stack):
    """
    Write a program to sort a stack such that the smallest items are on the top. You can use
    an additional temporary stack, but you may not copy the elements into any other data structure
    (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
    :param stack: input stack
    :return: sorted stack

    We will use a deque to simulate a stack
    """

    # base case
    if len(stack) <= 1:
        return stack

    # used to shift elements from the main stack
    aux_stack = deque()

    # sort the main stack while we still have elements
    while len(stack) != 0:

        aux_node = stack.pop()
        while len(aux_stack) != 0 and aux_node < aux_stack[-1]:
            stack.append(aux_stack.pop())

        aux_stack.append(aux_node)

    # move back the sorted elements to the main stack
    while len(aux_stack) != 0:
        stack.append(aux_stack.pop())

    return stack


class AnimalSortedLinkedList:
    """
    Sorted linked list used to store Animals
    The sort order is given by the animal timestamp
    """

    def __init__(self):
        self.first = None

    def add(self, data):
        node = Node(data)

        # list empty, add as first
        if self.first is None:
            self.first = node
            return

        # special case, replace the head of the list
        if data.timestamp < self.first.data.timestamp:
            node.next = self.first
            self.first = node
            return

        # loop the list and find the right spot for the new node
        current_node = self.first
        while current_node.next is not None and current_node.next.data.timestamp < data.timestamp:
            current_node = current_node.next

        node.next = current_node.next
        current_node.next = node

    def remove_first(self):
        if self.first is None:
            raise Exception("List empty")

        aux = self.first
        self.first = self.first.next
        return aux

    def __len__(self):
        if self.first is None:
            return 0

        current_node = self.first
        size = 0
        while current_node is not None:
            current_node = current_node.next
            size += 1

        return size


class Animal:
    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp


class Dog(Animal):
    def __init__(self, name, timestamp):
        super().__init__(name, timestamp)


class Cat(Animal):
    def __init__(self, name, timestamp):
        super().__init__(name, timestamp)


class AnimalShelter:
    """
    An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
    out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
    or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
    that type). They cannot select which specific animal they would like. Create the data structures to
    maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
    and dequeueCat. You may use the built in LinkedList data structure.

    We will use 2 LinkedLists to manage a list of dogs and a list of cats
    both linked list will be sorted by their timestamp, therefore pop actions will always return the right animal
    """

    def __init__(self):
        self.dogs_list = AnimalSortedLinkedList()
        self.cats_list = AnimalSortedLinkedList()

    def enqueue(self, new_entry):
        if type(new_entry) is Dog:
            self.dogs_list.add(new_entry)
        else:
            self.cats_list.add(new_entry)

    def dequeue_dog(self):
        return self.dogs_list.remove_first()

    def dequeue_cat(self):
        return self.cats_list.remove_first()

    def dequeue_any(self):
        # check which animal should be removed from both lists
        if self.dogs_list.first.data.timestamp < self.cats_list.first.data.timestamp:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()
