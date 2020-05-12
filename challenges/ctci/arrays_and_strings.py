def unique_characters(string):
    """
    Implement an algorithm to determine if a string
    has all unique characters. What if you
    cannot use additional data structures?
    :param string: input value
    :return: True if string matches the condition, False otherwise
    """
    # create a counter dictionary to count each char in the string
    counter_dict = {}

    # populate the dictionary
    for char in string:
        counter_dict[char] = counter_dict.get(char, 0) + 1

    # check if there are duplicates
    for key, value in counter_dict.items():
        if value >= 2:
            return False

    return True


def unique_characters_no_data_structure(string):
    """
    Implement an algorithm to determine if a string
    has all unique characters. What if you
    cannot use additional data structures?
    :param string: input value
    :return: True if string matches the condition, False otherwise
    """

    # we will sozrt the string (should be a O(n*log(n)) sort
    # this should be better than a for in for O(n^2)
    sorted(string)

    # check if 2 neighbours string are duplicates
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False

    return True


def check_permutation(first, second):
    """
    Given two strings, write a method
    to decide if one is a permutation of the other
    :param first: first input string
    :param second: second input string
    :return: True if first and second are permutations, False otherwise
    """

    # first of all, both strings must have the same length
    if len(first) != len(second):
        return False

    # we will use a counter dictionary to count the chars in both string
    # we will increment the values for the first string, and decrement for the second string
    # at the end, all values should be 0 if the two string are permutations

    counter_dict = {}

    for i in range(0, len(first)):
        counter_dict[first[i]] = counter_dict.get(first[i], 0) + 1
        counter_dict[second[i]] = counter_dict.get(second[i], 0) - 1

    for value in counter_dict.values():
        if value != 0:
            return False

    return True


def urlify(string):
    """
    Write a method to replace all spaces in a string with'%20' You may assume that the string
    has sufficient space at the end to hold the additional characters, and that you are given the "true"
    length of the string, (Note: if implementing in Java, please use a character array so that you can
    perform this operation in place.)
    EXAMPLE
    Input: "Mr 3ohn Smith"
    Output: "Mr%203ohn%20Smith"
    :param string: input string
    :return: output string with changes
    """

    # we will transform the input string in an array of
    # chars instead on normal string since python strings are immutable
    # this step is not required in normal conditions
    array = list(string)

    # given the fact that we know the true size of the string
    # we can count the number of spaces and get the size for the output
    # we this we can build the output string from the last position

    # we are using python count, could use a simple for
    # we assume this is O(n) operation
    no_spaces = array.count(' ')

    # initial size + number of spaces * 2
    # *2 since a space will be replaced by 3 new string -> " " -> %20
    # we need 2 extra char for each space
    output_len = len(array) + no_spaces * 2
    initial_index = len(array) - 1
    # padding the array with extra space, not required in normal conditions
    for index in range(len(array), output_len):
        array.append('X')

    current_index = len(array) - 1
    for i in range(initial_index, -1, -1):
        if string[i] == ' ':
            array[current_index] = '0'
            array[current_index - 1] = '2'
            array[current_index - 2] = '%'
            current_index -= 3
        else:
            array[current_index] = array[i]
            current_index -= 1

    return ''.join(array)


def palindrome_permutation(string):
    """
    Given a string, write a function to check if it is a permutation of a palindrome.
    A palindrome is a word or phrase that is the same forwards and backwards,
    A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
    EXAMPLE
    Input: Tac t Coa
    Output: True (permutations: "taco cat""atc o eta" etc.)
    :param string: input string
    :return: True if there is a valid permutation, False otherwise
    """

    # we will use a counter dictionary to counter each char in the string
    # a palindrome string should have all appear an even number of times
    # except for the middle char, if the string has a odd length
    # e.g. asdsa -> a x2, s x2, d x1

    counter_dict = {}
    # convert string to lowercase, should discuss this with tho
    string = string.lower()

    for char in string:
        # ignore spaces
        if char == '' or char == ' ':
            continue

        counter_dict[char] = counter_dict.get(char, 0) + 1

    found_middle_char = False
    for value in counter_dict.values():
        if value % 2 != 0:
            # already found a char with odd count
            if found_middle_char:
                return False
            else:
                found_middle_char = True

    return True


def one_way(first, second):
    """
    One Away: There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.
    EXAMPLE
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    :param first: first input string
    :param second: second input string
    :return: True if the strings are one edit away, False otherwise
    """

    # The 3 operations can be check based on the length of the string
    # l1 > l2 -> insert
    # l2 < l1 -> remove
    # l1 = l2 -> replace
    # also insert and remove can be checked with the same method
    # just swamp the params

    if len(first) == len(second):
        return check_replace(first, second)
    elif len(first) - 1 == len(second):
        return check_insert_or_remove(first, second)
    elif len(first) == len(second) - 1:
        return check_insert_or_remove(second, first)
    else:
        return False


def check_replace(first, second):
    """
    Utility function used to check the replace case for `one_way(first, second)`
    :param first: first input string
    :param second: second input string
    :return: True if second had exactly one char replaced based of first, False otherwhise
    """
    # utility flag used to keep track fi there is one replacement
    has_one_replace = False
    for i in range(0, len(first)):
        if first[i] != second[i]:
            if has_one_replace:
                return False
            else:
                has_one_replace = True
    return True


def check_insert_or_remove(first, second):
    """
    Utility function used to check insert/remove cases for `one_way(first, second)`
    len(first) > len(second) !!!
    :param first: first input string, the one with longer len
    :param second: second input string, the smaller one
    :return: True if a single insert/remove operation make the string different, else otherwise
    """

    found_one_different = False
    i = 0
    j = 0
    while i < len(second):
        if first[j] == second[i]:
            j += 1
            i += 1
        else:
            if not found_one_different:
                found_one_different = True
                j += 1
            else:
                return False

    return True


def one_way_v2(first, second):
    """
    Same as one_way(first, second), but this time we'll try a single
    function for all 3 edit actions
    """

    if abs(len(first) - len(second)) > 1:
        return False

    # we still need to check which string has a longer length
    if len(second) > len(first):
        first, second = second, first

    found_one_different = False
    i = 0
    j = 0
    while i < len(second):
        if first[j] != second[i]:
            if found_one_different:
                return False
            else:
                found_one_different = True
                if len(first) == len(second):
                    i += 1
        else:
            i += 1
        j += 1

    return True


def string_compression(string):
    """
    Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3, If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
    :param string: input string
    :return: compressed string
    """

    # the catch here is stat using normal string append "+=" in python case
    # is very expensive so you should use other approach such as StringBuilder in Java
    # in python case we will use "".join() to simulate the string builder
    compressed = ''
    counter = 1
    for i in range(0, len(string)):
        if i < len(string) - 1 and string[i] == string[i + 1]:
            counter += 1
        else:
            compressed = ''.join([compressed, string[i], str(counter)])
            counter = 1

    return compressed


def rotate_matrix(matrix):
    """
    Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
    bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
    :param matrix: input matrix
    :return: matrix rotate 90 degrees clockwise
    ex:
    1 2 3    7 4 1
    4 5 6 -> 8 5 2
    7 8 9    9 6 3
    """

    # We will do this in 2 steps

    # First we create Matrix^t with is the transpose matrix
    # 1 2 3    1 4 7
    # 4 5 6 -> 2 5 8
    # 7 8 9    3 6 9

    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Now what's left is to reverse each row
    # 1 4 7    7 4 1
    # 2 5 8 -> 8 5 2
    # 3 6 9    9 6 3
    half_point = int(len(matrix) / 2)
    for i in range(0, len(matrix)):
        for j in range(0, half_point):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix) - j - 1]
            matrix[i][len(matrix) - j - 1] = temp

    return matrix


def zero_matrix(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0
    :param matrix: input matrix
    :return: result matrix
    """

    # we will iterate the matrix and mark all rows and columns that have at least a 0
    zero_rows = set()
    zero_cols = set()

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(0, len(matrix)):
        if i in zero_rows:
            for j in range(0, len(matrix[0])):
                matrix[i][j] = 0

    for j in range(0, len(matrix[0])):
        if j in zero_cols:
            for i in range(0, len(matrix)):
                matrix[i][j] = 0

    return matrix


def zero_matrix_o1_space(matrix):
    """
    Write an algorithm such that if an element in an MxN matrix is 0,
    its entire row and column are set to 0
    :param matrix: input matrix
    :return: result matrix
    Same as zero_matrix, but now we will use the first row and first column
    of the matrix to reduce space usage
    """

    # flag to keep track if the first row and col have zero values
    first_row_zero = False
    first_col_zero = False

    # check if first row has 0
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0:
            first_col_zero = True

    # check if first col has 0
    for j in range(0, len(matrix[0])):
        if matrix[0][j] == 0:
            first_row_zero = True

    # save zero for the rest of the matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # change rows
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            for j in range(0, len(matrix[0])):
                matrix[i][j] = 0

    # change cols
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            for i in range(0, len(matrix)):
                matrix[i][j] = 0

    # also need to check if the first row and col need to be changed
    if first_col_zero:
        for i in range(0, len(matrix)):
            matrix[i][0] = 0

    if first_row_zero:
        for j in range(0, len(matrix[0])):
            matrix[0][j] = 0

    return matrix
