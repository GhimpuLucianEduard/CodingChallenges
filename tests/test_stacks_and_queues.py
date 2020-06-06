import unittest

from challenges.ctci.stacks_and_queues import *


class TestStack():

    def setUp(self):
        self.stack = self.getImplementation()

    def getImplementation(self):
        pass

    def test_push(self):
        self.stack.push(10)
        assert self.stack.last.data == 10
        self.stack.push(14)
        assert self.stack.last.data == 14
        assert self.stack.last.next.data == 10

    def test_push_pop(self):
        self.stack.push(10)
        assert self.stack.last.data == 10
        self.stack.push(1)
        self.stack.push(102)
        self.stack.push(45)
        assert self.stack.last.data == 45

        self.stack.pop()
        assert self.stack.last.data == 102
        self.stack.pop()
        assert self.stack.last.data == 1
        self.stack.pop()
        assert self.stack.last.data == 10

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.stack.pop()

    def test_push_peek(self):
        self.stack.push(10)
        assert self.stack.peek().data == 10
        self.stack.push(1)
        assert self.stack.peek().data == 1


class TestMinStack(TestStack):

    def test_push_min(self):
        self.stack.push(10)
        assert self.stack.min() == 10
        self.stack.push(14)
        assert self.stack.min() == 10

    def test_all(self):
        self.stack.push(10)
        assert self.stack.peek().data == 10
        assert self.stack.min() == 10
        self.stack.pop()

        with self.assertRaises(Exception):
            self.stack.min()

        self.stack.push(10)
        self.stack.push(100)
        self.stack.push(2)
        self.stack.push(25)

        assert self.stack.min() == 2


class TestMinNodeStack(TestMinStack, unittest.TestCase):
    def getImplementation(self):
        return MinNodeStack()


class TestDoubleStackMinStack(TestMinStack, unittest.TestCase):
    def getImplementation(self):
        return DoubleStackMinStack()


class TestStackOfPlates(unittest.TestCase):

    def setUp(self):
        self.stack = StackOfPlates(5)

    def test_push_empty(self):
        self.stack.push(19)
        self.assertEqual(len(self.stack.stacks), 1)
        self.assertEqual(len(self.stack.stacks[0]), 1)
        self.assertEqual(self.stack.stacks[0][0], 19)

    def test_push_new_stack(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(len(self.stack.stacks), 1)
        self.stack.push(6)
        self.assertEqual(len(self.stack.stacks), 2)
        self.assertEqual(len(self.stack.stacks[1]), 1)
        self.assertEqual(self.stack.stacks[1][0], 6)

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.stack.pop()

    def test_push_pop_non_empty(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        self.assertEqual(len(self.stack.stacks), 1)
        self.assertEqual(len(self.stack.stacks[0]), 2)
        self.assertEqual(self.stack.stacks[0][0], 1)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(len(self.stack.stacks), 1)
        self.stack.push(6)
        self.assertEqual(len(self.stack.stacks), 2)
        self.assertEqual(len(self.stack.stacks[1]), 1)
        self.assertEqual(self.stack.stacks[1][0], 6)
        self.stack.pop()
        self.assertEqual(len(self.stack.stacks), 1)

    def test_pop_at_empty(self):
        with self.assertRaises(Exception):
            self.stack.pop_at(0)

    def test_push_pop_at_non_empty(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop_at(0)
        self.assertEqual(len(self.stack.stacks), 1)
        self.assertEqual(len(self.stack.stacks[0]), 2)
        self.assertEqual(self.stack.stacks[0][0], 1)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(len(self.stack.stacks), 1)
        self.stack.push(6)
        self.assertEqual(len(self.stack.stacks), 2)
        self.assertEqual(len(self.stack.stacks[1]), 1)
        self.assertEqual(self.stack.stacks[1][0], 6)
        self.stack.pop_at(1)
        self.assertEqual(len(self.stack.stacks), 1)

    def test_push_pop_at_multiple_stacks(self):
        for i in range(0, 17):
            self.stack.push(i)

        self.assertEqual(len(self.stack.stacks), 4)
        self.stack.pop_at(2)
        self.assertEqual(len(self.stack.stacks), 4)
        self.stack.pop_at(2)
        self.assertEqual(len(self.stack.stacks), 3)
        self.assertEqual(self.stack.stacks[2][self.stack.stack_capacity - 1], 16)


class TestQueueWithTwoStacks(unittest.TestCase):

    def setUp(self):
        self.queue = QueueWithTwoStacks()

    def test_push_empty(self):
        self.queue.push(20)
        self.assertEqual(self.queue.main_stack[0], 20)

    def test_push_multiple(self):
        self.queue.push(20)
        self.queue.push(40)
        self.queue.push(60)
        self.assertEqual(self.queue.main_stack[1], 40)

    def test_peek_empty(self):
        with self.assertRaises(Exception):
            self.queue.peek()

    def test_push_peek(self):
        self.queue.push(20)
        self.queue.push(40)
        self.queue.push(60)
        self.assertEqual(self.queue.peek(), 20)

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.queue.pop()

    def test_push_pop(self):
        self.queue.push(20)
        self.queue.push(40)
        self.queue.push(60)
        self.assertEqual(self.queue.pop(), 20)

    def test_all(self):
        with self.assertRaises(Exception):
            self.queue.pop()

        self.queue.push(20)
        self.queue.push(40)
        self.queue.push(60)
        self.assertEqual(self.queue.peek(), 20)
        self.assertEqual(self.queue.pop(), 20)
        self.assertEqual(self.queue.pop(), 40)
        self.assertEqual(self.queue.pop(), 60)

        with self.assertRaises(Exception):
            self.queue.pop()


class TestSortingStack(unittest.TestCase):
    def setUp(self):
        self.stack = SortingStack()

    def test_push(self):
        self.stack.push(10)
        assert self.stack.last.data == 10
        self.stack.push(14)
        assert self.stack.last.data == 10
        assert self.stack.last.next.data == 14
        self.stack.push(22)
        assert self.stack.last.data == 10

    def test_peek_empty(self):
        with self.assertRaises(Exception):
            self.stack.peek()

    def test_push_peek(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(14)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.push(22)
        self.assertEqual(self.stack.peek(), 2)

    def test_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_not_empty(self):
        self.stack.last = Node(10)
        self.assertFalse(self.stack.is_empty())

    def test_pop_empty(self):
        with self.assertRaises(Exception):
            self.stack.pop()

    def test_push_pop(self):
        self.stack.push(10)
        self.stack.push(14)
        self.assertEqual(self.stack.pop().data, 10)
        self.stack.push(2)
        self.stack.push(5)
        self.assertEqual(self.stack.pop().data, 2)

    def test_all(self):
        with self.assertRaises(Exception):
            self.stack.pop()

        self.stack.push(14)
        self.assertEqual(self.stack.peek(), 14)
        self.stack.push(2)
        self.stack.push(5)

        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()

        with self.assertRaises(Exception):
            self.stack.peek()


class TestSortStack(unittest.TestCase):

    def test_sort_stack_empty(self):
        stack = deque()
        stack = sort_stack(stack)
        self.assertEqual(len(stack), 0)

    def test_sort_stack_one_element(self):
        stack = deque()
        stack.append(10)
        stack = sort_stack(stack)
        self.assertEqual(len(stack), 1)

    def test_sort_stack_multiple_elements(self):
        stack = deque()
        stack.append(2)
        stack.append(7)
        stack.append(4)
        stack.append(1)
        stack = sort_stack(stack)
        self.assertEqual(len(stack), 4)
        self.assertEqual(stack[0], 7)
        self.assertEqual(stack[1], 4)
        self.assertEqual(stack[2], 2)
        self.assertEqual(stack[3], 1)

    def test_sort_stack_multiple_elements_sorted(self):
        stack = deque()
        stack.append(4)
        stack.append(3)
        stack.append(2)
        stack.append(1)
        stack = sort_stack(stack)
        self.assertEqual(len(stack), 4)
        self.assertEqual(stack[0], 4)
        self.assertEqual(stack[1], 3)
        self.assertEqual(stack[2], 2)
        self.assertEqual(stack[3], 1)

    def test_sort_stack_multiple_elements_sorted_reverse(self):
        stack = deque()
        for i in range(0, 19):
            stack.append(i)
        stack = sort_stack(stack)
        self.assertEqual(len(stack), 19)
        self.assertEqual(stack[0], 18)
        self.assertEqual(stack[7], 11)
        self.assertEqual(stack[18], 0)


class TestAnimalShelter(unittest.TestCase):

    def setUp(self):
        self.animal_shelter = AnimalShelter()

    def test_enqueue_empty(self):
        self.animal_shelter.enqueue(Dog("dog1", 1))
        self.assertEqual(len(self.animal_shelter.dogs_list), 1)
        self.assertEqual(len(self.animal_shelter.cats_list), 0)

    def test_enqueue_multiple(self):
        self.animal_shelter.enqueue(Dog("dog1", 4))
        self.animal_shelter.enqueue(Dog("dog2", 1))
        self.animal_shelter.enqueue(Dog("dog3", 7))
        self.assertEqual(len(self.animal_shelter.dogs_list), 3)
        self.assertEqual(self.animal_shelter.dogs_list.first.data.timestamp, 1)

        self.animal_shelter.enqueue(Cat("cat1", 17))
        self.animal_shelter.enqueue(Cat("cat2", 11))
        self.animal_shelter.enqueue(Cat("cat3", 5))
        self.animal_shelter.enqueue(Cat("cat4", 12))
        self.animal_shelter.enqueue(Cat("cat5", 11))

        self.assertEqual(len(self.animal_shelter.cats_list), 5)
        self.assertEqual(self.animal_shelter.cats_list.first.data.timestamp, 5)

    def test_enqueue_dequeue_dog(self):
        self.animal_shelter.enqueue(Dog("dog1", 4))
        self.animal_shelter.enqueue(Dog("dog2", 1))
        self.animal_shelter.enqueue(Dog("dog3", 7))
        self.assertEqual(len(self.animal_shelter.dogs_list), 3)
        self.assertEqual(self.animal_shelter.dequeue_dog().data.name, "dog2")
        self.assertEqual(len(self.animal_shelter.dogs_list), 2)

    def test_enqueue_dequeue_cat(self):
        self.animal_shelter.enqueue(Cat("cat1", 17))
        self.animal_shelter.enqueue(Cat("cat2", 11))
        self.animal_shelter.enqueue(Cat("cat3", 5))
        self.assertEqual(len(self.animal_shelter.cats_list), 3)
        self.assertEqual(self.animal_shelter.dequeue_cat().data.name, "cat3")
        self.assertEqual(len(self.animal_shelter.cats_list), 2)

    def test_enqueue_dequeue_any(self):
        self.animal_shelter.enqueue(Dog("dog1", 4))
        self.animal_shelter.enqueue(Dog("dog2", 1))
        self.animal_shelter.enqueue(Dog("dog3", 7))
        self.assertEqual(len(self.animal_shelter.dogs_list), 3)
        self.animal_shelter.enqueue(Cat("cat1", 17))
        self.animal_shelter.enqueue(Cat("cat2", 11))
        self.animal_shelter.enqueue(Cat("cat3", 5))
        self.assertEqual(len(self.animal_shelter.cats_list), 3)
        self.assertEqual(self.animal_shelter.dequeue_any().data.name, "dog2")
        self.assertEqual(self.animal_shelter.dequeue_any().data.name, "dog1")
        self.assertEqual(self.animal_shelter.dequeue_any().data.name, "cat3")

    def test_dequeue_dog_empty(self):
        with self.assertRaises(Exception):
            self.animal_shelter.dequeue_dog()

    def test_dequeue_cat_empty(self):
        with self.assertRaises(Exception):
            self.animal_shelter.dequeue_cat()

    def test_dequeue_any_empty(self):
        with self.assertRaises(Exception):
            self.animal_shelter.dequeue_any()


if __name__ == '__main__':
    unittest.main()
