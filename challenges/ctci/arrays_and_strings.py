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

    for char in string:
        # ignore spaces
        if char == '':
            continue

        counter_dict[char] = counter_dict.get(char, 0) + 1

    found_middle_char = False
    for value in counter_dict.values():
        if value % 2 == 0:
            if value == 1:
                # already found a char with count 1
                if found_middle_char:
                    return False
                else:
                    found_middle_char = True
        else:
            return False

    return True
