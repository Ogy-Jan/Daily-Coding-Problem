"""
Company:
    This problem was asked by Uber.
Problem:
    Given an array of integers, return a new array such that
    each element at index i of the new array is the product
    of all the numbers in the original array except the one at i.
Examples:
    1. If our input was [1, 2, 3, 4, 5],
    the expected output would be [120, 60, 40, 30, 24].
    2. If our input was [3, 2, 1],
    the expected output would be [2, 3, 6].
Follow-up:
    what if you can't use division?
"""

input_list = [1, 2, 3, 4, 5]
# input_list = [3, 2, 1]
# input_list = [5, 10]
# input_list = [2]
# input_list = []


def mult_lst_items(m_list):
    """ Multiply all the items in a list;
        account for edge cases => empty list and single item list

    :param m_list: input list to multiply
    :return: product of all the list items
    """
    if len(m_list) == 0:
        return 0
    elif len(m_list) == 1:
        return m_list[0]
    else:
        mult = 1
        for item in m_list:
            mult = mult * item
        return mult


def gen_output_lst(in_list):
    """ Generate the output list eliminating the i-th item from the multiplication

    :param in_list: input list
    :return: output list
    """
    output_list = []
    for num in in_list:
        i_lst_copy = input_list.copy()
        i_lst_copy.remove(num)
        mult_lst_items(i_lst_copy)
        output_list.append(mult_lst_items(i_lst_copy))
    return output_list


print("The output list is: ", gen_output_lst(input_list))

#  achieved BigO of O{(N-1)^2}
#  N = number of list elements
#  N-1 iterations while looping through list (without the i-th element) -> outer loop
#  N-1 iterations while multiplying all items from the list -> inner loop
