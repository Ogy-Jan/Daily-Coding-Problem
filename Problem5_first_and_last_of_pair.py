"""
Company:
    This problem was asked by Jane Street.
Problem:
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    Given this implementation of cons:
    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair
    Implement car and cdr.
Examples:
    car(cons(3, 4)) returns 3
    cdr(cons(3, 4)) returns 4
"""


def cons(a, b):
    """
    Constructs a pair from of two inputs
    :param a: first pair element (int, float, string, list etz.)
    :param b: last pair element (int, float, string, list etz.)
    :return: the pair function (not the return value of the function, but the function itself)
    """
    def pair(f):
        """
        The pair function itself returns the return value from a function f with 2 inputs
        :param f: a function
        :return: the return value of the function
        """
        return f(a, b)
    return pair


def car(func):
    """
    Returns the first element of a pair
    :param func: a function
    :return: the return value of calling the input function => in this case the first value of a pair
    """
    def first(a, b):
        return a
    return func(first)


def cdr(func):
    """
    Returns the last element of a pair
    :param func: a function
    :return: the return value of calling the input function => in this case the last value of a pair
    """
    def last(a, b):
        return b
    return func(last)


def main(a, b):
    """
    The main function invoking the other functions
    :param a: first pair element
    :param b: second pair element
    :return: print statements which indicate the first and the second pair element
    """
    print("The first pair element is:", car(cons(a, b)))
    print("The second pair element is:", cdr(cons(a, b)))


#  Using the special __name__ variable we can execute the code as a script in the Terminal,
#  or import the code as a module in another python file
if __name__ == "__main__":
    main(7, 9)
