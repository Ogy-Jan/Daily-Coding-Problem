"""
Company:
    This problem was asked by Stripe.
Problem:
    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array. The array can
    contain duplicates and negative numbers as well.
Examples:
    input: [3, 4, -1, 1] => output = 2
    input [1, 2, 0] => output = 3
"""

# in_list = [3, 4, -1, 1]
# in_list = [1, 2, 0]
# in_list = [0]
# in_list = [3, 3, 3]
# in_list = [-1, -5, -6, -7]
in_list = [1, 2, 3, 100000]


def calc_min_max(lst):
    """
    Calculate the maximum and minimum integer in the list,
    and ignore negative values
    :param lst: a list of integers (positive, negative and zero are allowed)
    :return: the minimum and maximum integer, ignoring negative values
    """
    max_int = max(lst)
    if max_int < 0:
        max_int = 0
    min_int = min(lst)
    if min_int < 0:
        min_int = 0
    return min_int, max_int


def calc_fist_int(min_int, max_int, lst):
    """
    Calculate the first positive integer in a list of integers
    :param min_int: minimum positive integer >= 0
    :param max_int: maximum integer >= 0
    :param lst: list of integers
    :return: the first positive integer
    """

    if min_int == max_int:
        return max_int + 1

    check_int = min_int
    for i in range(max_int - min_int):
        check_int += 1
        if check_int not in lst:
            return check_int
        if check_int == max_int:
            return check_int + 1


def main(lst):
    """
    The main function invoking the other functions
    :param lst: A list of integers (positive, negative and zero are allowed)
    :return: None
    """
    i_min, i_max = calc_min_max(lst)
    answer = calc_fist_int(i_min, i_max, lst)
    print("The first missing positive integer is", answer)


#  Using the special __name__ variable we can execute the code as a script in the Terminal,
#  or import the code as a module in another python file
if __name__ == "__main__":
    main(in_list)

#  achieved BigO of O{N*(N-1)}
#  N = number of integers in the list
#  O{N} is needed to find the min and the max, generalizing from 2N, by ignoring constants
#  O{N-1} is needed to find the first in in a looping through (max - min)
#  space complexity is constant O{1} => size of list does not influence algorithm space complexity
