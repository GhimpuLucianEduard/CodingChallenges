from collections import defaultdict
import itertools


def sum_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


def equal_digit_sum(A):
    """
    Given an array A consisting of N integers, return the maximum sum of
    two numbers whose digits add up to an equal sum. If there are no two numbers
    whose digits have an equal sum, the function should return -1.

    Examples:

    Given A = [51, 71, 17, 42], the function should return 93.
    There are two pairs of numbers whose digits add up to an equal sum:
    (51, 42) and (17, 71). The first pair sums up to 93.

    Given A = [42, 33, 60], the function should return 102.
    The digits of all numbers in A add up to the same sum, and choosing
    to add 42 and 60 given the result 102.

    Given A = [51, 32, 43], the function should return -1, since all
    numbers in A have digits that add up to different, unique sums.
    :param A: input array
    :return: return the maximum sum of two numbers whose digits add up to an equal sum or -1
    """

    # we create a dictionary that will hold the largest number
    # the key will be the sum
    sum_dict = defaultdict(int)
    max_sum = -1

    for current_number in A:
        sum_digit = sum_digits(current_number)
        dict_number = sum_dict[sum_digit]
        if dict_number != 0:
            max_sum = max(max_sum, dict_number + current_number)
            sum_dict[sum_digit] = max(dict_number, current_number)
        else:
            sum_dict[sum_digit] = current_number
    return max_sum


def jafar_checkers(board):
    max_pawns = 0
    pawn_i = -1
    pawn_j = -1

    # first of all let's get jafar's pawn position
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 'O':
                pawn_i = i
                pawn_j = j

    # pawn at the end of the board
    if pawn_i == 0:
        return 0

    return check_move('O', pawn_i, pawn_j, board)


def check_move(old_element, next_i, next_j, board):
    cur_element = board[next_i][next_j]

    # check if we are on the last possible move
    if next_i < 2:
        return 0

    # check left
    left_value = 0
    middle_left_i = next_i - 1
    middle_left_j = next_j - 1
    upper_left_i = middle_left_i - 1
    upper_left_j = middle_left_j - 1

    if middle_left_j >= 0 and middle_left_i >= 0 and upper_left_i >= 0 and upper_left_j >= 0:
        # we can continue to the left side, check if we can attack a pawn
        middle_left_element = board[middle_left_i][middle_left_j]
        upper_left_element = board[upper_left_i][upper_left_j]
        if (cur_element == 'O' and middle_left_element == 'X' and upper_left_element == '.') or (
                cur_element == '.' and middle_left_element == 'X' and upper_left_element == '.'):
            left_value = 1 + check_move(upper_left_element, upper_left_i, upper_left_j, board)

    # same as above both fir the right side
    right_value = 0
    middle_right_i = next_i - 1
    middle_right_j = next_j + 1
    upper_right_i = middle_right_i - 1
    upper_right_j = middle_right_j + 1

    if middle_right_j < len(board[0]) and middle_right_i >= 0 and upper_right_i >= 0 and upper_right_j < len(board[0]):
        # we can continue to the left side, check if we can attack a pawn
        middle_right_element = board[middle_right_i][middle_right_j]
        upper_right_element = board[upper_right_i][upper_right_j]
        if (cur_element == 'O' and middle_right_element == 'X' and upper_right_element == '.') or (
                cur_element == '.' and middle_right_element == 'X' and upper_right_element == '.'):
            right_value = 1 + check_move(upper_right_element, upper_right_i, upper_right_j, board)

    return max(left_value, right_value)


def airplane(n, s):
    res = 0
    h = {}

    for i in range(1, n + 1):
        h[i] = set()
    for v in s.split():
        h[int(v[0])].add(v[1])

    case1 = {'D', 'E', 'F', 'G'}
    case2 = {'B', 'C', 'D', 'E'}
    case3 = {'F', 'G', 'H', 'J'}
    case4 = {'A', 'K'}

    valid = [case1, case2, case3]
    for _, v in h.items():
        print(_)
        print(v)
        print(len(case4 ^ v))
        if len(v) == 0 or len(case4 ^ v) == 0:
            res += 2
        elif any(case not in v for case in valid):
            res += 1
    return res


def permutef(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            for perm in permutef(s[:i] + s[i + 1:]):
                out += [let + perm]
    return out


def particles(input):
    moments = 0
    for i in range(0, len(input) - 2):
        if input[i + 2] - input[i + 1] == input[i + 1] - input[i]:
            moments += 1
            for j in range(i + 3, len(input)):
                if input[j] - input[j - 1] == input[i + 2] - input[i + 1]:
                    moments += 1
    return moments


def largest_k(array):
    array = set(array)
    dict = defaultdict(int)
    for element in array:
        dict[abs(element)] += 1

    return max(reversed(dict), key=dict.get)


def demo_codility(array):
    set_a = list(set(array))
    max = -1
    for i in range(0, len(set_a) - 1):
        if set_a[i] > 0 and set_a[i + 1] - set_a[i] > 1:
            max = set_a[i] + 1
            break

    # check for last
    if max == -1 and set_a[len(set_a) - 1] == 2:
        max = set_a[len(set_a) - 1] + 1

    return max if max > 0 else 1

def build_nr(n):

    neg = False
    if n < 0:
        neg = True
        n = abs(n)

    digits = len(str(n))
    copy_n = 0
    five_added = False
    while digits > 0:
        # get first digit python way
        first = n // pow(10, digits - 1)
        if not five_added:
            if (first > 5 and not neg) or (first < 5 and neg):
                copy_n = copy_n * 10 + first
            else:
                # add the 5
                copy_n = copy_n * 10 + 5
                copy_n = copy_n * 10 + first
                five_added = True
        else:
            # copy the rest
            copy_n = copy_n * 10 + first

        n = n % pow(10, digits - 1)
        digits -= 1

    if not five_added:
        copy_n = copy_n * 10 + 5

    return -1 * copy_n if neg is True else copy_n

def mc_5(n):
    if n == 0:
        return 50
    neg = False
    if n < 0:
        neg = True
        n = abs(n)

    digits = len(str(n))
    copy_n = 0
    five_added = False
    while digits > 0:
        # get first digit python way
        first = n // pow(10, digits - 1)
        if not five_added:
            if (first > 5 and not neg) or (first < 5 and neg):
                copy_n = copy_n * 10 + first
            else:
                # add the 5
                copy_n = copy_n * 10 + 5
                copy_n = copy_n * 10 + first
                five_added = True
        else:
            # copy the rest
            copy_n = copy_n * 10 + first

        n = n % pow(10, digits - 1)
        digits -= 1

    if not five_added:
        copy_n = copy_n * 10 + 5

    return -1 * copy_n if neg is True else copy_n


# def mc_52(n):
#     if n == 0:
#         return 50
#
#     if n > 0:
#         # we add the 5 at the begging and the we shift it
#         # until al larger numbers are on the left
#
#         # count the digits, should take O(n)
#         digits = len(str(n))
#         print(digits)
#
#         n = 5 * pow(10, digits) + n
#         # convert it to a string since it's easier to manipulate
#         n_str = str(n)
#         copy_s = ""
#         for i in range(1, len(n_str)):
#             if int(n_str[i]) > 5:
#                 copy_s
#
#
#     return n


def perm_ms(a, b, c, d):
    # build permutations
    permutations = list(itertools.permutations([a, b, c, d]))

    # remove duplicates
    permutations = list(set(permutations))
    valid_permutations = 0

    for perm in permutations:
        # check if permutation is valid
        hours = perm[0] * 10 + perm[1]
        minutes = perm[2] * 10 + perm[3]
        if hours <= 23 and minutes <= 59:
            valid_permutations += 1

    return valid_permutations


def expend(S):
    s_expanded = ""
    i = 0
    while i < len(S):
        n = 0
        # we have a number
        if S[i].isdigit():
            while i < len(S) and S[i].isdigit():
                n = n * 10 + int(S[i])
                i += 1
            while n > 0:
                s_expanded += "?"
                n -= 1
            n = 0
        else:
            s_expanded += S[i]
            i += 1

    return s_expanded


def ocr(S, T):
    s_exp = expend(S)
    t_exp = expend(T)
    print(s_exp, t_exp)

    if len(s_exp) != len(t_exp):
        print(len(s_exp), len(t_exp))
        return False

    for i in range(0, len(s_exp)):
        if s_exp[i] != t_exp[i] and (s_exp[i] != '?' and t_exp[i] != '?'):
            return False

    return True


def main():
    input = "1A 2F 1C"
    # print(airplane(2, input))
    # print(permutef("abc"))
    # print(particles([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]))
    # print(largest_k([3, 2, -2, 5, -3, -8, 8, 10]))
    # print(demo_codility([1, 2, 3]))

    print(mc_5(123))
    # print(mc_52(7999))

    # print(perm_ms(1, 8, 3, 2))
    # print(perm_ms(1, 0, 0, 2))

    # print(ocr("ba1", "1AD"))
    # print(ocr("A2Le", "2pL1"))
    # print(ocr("3x2x", "8"))
    # print(ocr('a12b', 'a11aa'))



if __name__ == "__main__":
    main()
