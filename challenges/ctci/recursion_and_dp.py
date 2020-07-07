from collections import defaultdict


def triple_step(n):
    """
    A child is running up a staircase with n steps and can hop
    either 1 step, 2 steps, or 3 steps at a time. Implement a method
    to count how many possible ways the child can run up the stairs
    :param n: number of stairs
    :return: total possible ways to run the stairs
    """

    # if we calculate the first 5 values (f(1) ... f(5))
    # you will observe that f(n) = f(n-1) + f(n-2) + f(n-3)
    # note that f(n) = number of possible ways to run the stairs
    cache = defaultdict(int)
    cache[0] = 1
    cache[1] = 1
    cache[2] = 2
    return triple_step_aux(n, cache)


def triple_step_aux(n, cache):
    """
    Aux method for triple step
    :param n: number of stairs
    :param cache: a cache with the f(n) we have already computed
    :return: total possible ways to run the stairs
    """

    # base case
    if n == 0 or n == 1:
        return cache[0]

    if not cache[n]:
        cache[n] = triple_step_aux(n - 1, cache) + triple_step_aux(n - 2, cache) + triple_step_aux(n - 3, cache)

    return cache[n]


def robot_in_a_grid(grid):
    """
    Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
    The robot can only move in two directions, right and down, but certain cells are "off limits" such that
    the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
    the bottom right.
    :param grid: input grid
    :return: list of points representing the path if there is one, empty list otherwise
    """

    # to have a path for (r, c) there must a path to either
    # (r, c-1) or (r-1, c), and so we can go on
    # we will keep the visited nodes in a cache and build up the path

    path = []
    cache = defaultdict(bool)
    robot_in_a_grid_aux(grid, len(grid) - 1, len(grid[0]) - 1, path, cache)
    return path


def robot_in_a_grid_aux(grid, row, col, path, cache):
    """
    Aux method for robot_in_a_grid
    :param grid: input grid
    :param row: current row
    :param col: current col
    :param cache: used to store the nodes that we've already visited
    :param path: path that we build
    :return: True if there is a path to (row, col), False otherwise
    """

    # we will use None to mark a cell as not available
    if row < 0 or col < 0 or grid[row][col] is None:
        return False

    # we've already visited this node, we don't need to check it
    if (row, col) in cache:
        return False

    if (row == 0 and col == 0) or \
            robot_in_a_grid_aux(grid, row, col - 1, path, cache) or \
            robot_in_a_grid_aux(grid, row - 1, col, path, cache):
        path.append((row, col))
        return True

    cache[(row, col)] = False
    return False


def magic_index(array):
    """
    A magic index in an array A [ 0 ••• n -1] is
    defined to be an index such that A[ i] = i.
    Given a sorted array of distinct integers, write a
    method to find a magic index, if one exists, in array A.
    :param array: input array
    :return: The magic index if exits, -1 otherwise
    """
    if len(array) == 0:
        return -1

    return magic_index_aux(array, 0, len(array) - 1)


def magic_index_aux(array, i, j):
    # base case
    if i == j and array[i] != i:
        return -1

    mid_index = (i + j) // 2
    if array[mid_index] == mid_index:
        return mid_index

    if array[mid_index] > mid_index:
        # search in the left side
        return magic_index_aux(array, i, mid_index - 1)
    else:
        # search in the right side
        return magic_index_aux(array, mid_index + 1, j)


def magic_index_followup(array):
    """
    A magic index in an array A [ 0 ••• n -1] is
    defined to be an index such that A[ i] = i.
    Given a sorted array of distinct integers, write a
    method to find a magic index, if one exists, in array A.
    FOLLOW UP
    What if the values are not distinct?
    :param array: input array
    :return: The magic index if exits, -1 otherwise
    """
    if len(array) == 0:
        return -1

    return magic_index_followup_aux(array, 0, len(array) - 1)


def magic_index_followup_aux(array, i, j):
    # base case
    if i > j:
        return -1

    mid_index = (i + j) // 2
    if array[mid_index] == mid_index:
        return mid_index

    left_result = magic_index_followup_aux(array, i, mid_index - 1)
    if left_result != -1:
        return left_result

    right_result = magic_index_followup_aux(array, mid_index + 1, j)
    if right_result != -1:
        return right_result

    return -1


def power_set(input_set):
    """
    Write a method to return all subsets of a set
    :param input_set: Input set
    :return: All subsets of input set
    """

    if len(input_set) == 0:
        return []

    return power_set_aux(input_set, len(input_set) - 1)


def power_set_aux(input_set, index):
    subsets = []

    if index == -1:
        subsets.append([])
        return subsets

    subsets = power_set_aux(input_set, index - 1)
    new_subsets = []
    for sub_set in subsets:
        copy = sub_set.copy()
        copy.append(input_set[index])
        new_subsets.append(copy)

    subsets.extend(new_subsets)

    return subsets
