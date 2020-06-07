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
