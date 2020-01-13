"""
Company:
    This problem was asked by Stripe.
Problem:
    Given an array of integers, find the first missing positive integer  in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array. The array can
    contain duplicates and negative numbers as well.
Examples:
    input: [3, 4, -1, 1] => output = 2
    input [1, 2, 0] => output = 3
"""

# in_list = [3, 4, -1, 1]
in_list = [1, 2, 0]
# in_list = [0]
# in_list = [-1, -5, -6, -7]
# in_list = [1, 2, 3, 100000]


def main(lst):
    max_int = max(lst)
    if max_int <= 0:
        return 1
    min_int = min(lst)
    if min_int < 0:
        min_int = 0
    check_int = min_int
    for i in range(max_int - min_int):
        check_int += 1
        if check_int not in lst:
            return check_int


#  Using the special __name__ variable we can execute the code as a script in the Terminal,
#  or import the code as a module in another python file
if __name__ == "__main__":
    answer = main(in_list)
    print(answer)
