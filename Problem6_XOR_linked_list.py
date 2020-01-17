"""
Company:
    This problem was asked by Google.
Problem:
    An XOR linked list is a more memory efficient doubly linked list.
    Instead of each node holding next and prev fields, it holds a field named both,
    which is an XOR of the next node and the previous node. Implement an XOR linked list;
    it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

    If using a language that has no pointers (such as Python), you can assume you have access
    to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

    Because linked list are new to me I researched and created a doubly linked list
    not an XOR doubly linked list. Please note that this code is buggy. I need to learn more about linked lists. :)
"""


class Node:
    """
    The Node class with the previous and next node information
    as well as it's own data
    """
    def __init__(self, data, nxt=None, prv=None):
        self.data = data
        self.next_node = nxt
        self.prev_node = prv

    def get_next(self):
        return self.next_node

    def set_next(self, nxt):
        self.next_node = nxt

    def get_prev(self):
        return self.prev_node

    def set_prev(self, prv):
        self.prev_node = prv

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList:
    """
    The whole linked List; at initialization no root node is created
    The first node we add is the root node, and then each node we add replaces the
    root node and pushes is one place to the right
    """
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        """
        Add a new node as the root node at the beginning of the linked list
        :param data: The lists own data
        :return: None
        """
        #  create a new node with the previous root node as it's next node
        new_node = Node(data, self.root)
        #  if a root node already exists change it's previous node to the new node
        if self.root:
            self.root.set_prev(new_node)
        #  now set the new node as the root node
        self.root = new_node
        #  increment the list size
        self.size += 1

    def remove_node(self, data):
        # set the first node we look at to the root node
        this_node = self.root
        # loop through the nodes
        while this_node:
            # if we find the node with the data we want to delete, delete the node
            # by setting the previous node of it's next node to it's own previous node
            # and setting the next node of it's previous node to it's own next node
            if this_node.get_data() == data:
                nxt = this_node.get_next()
                prv = this_node.get_prev()
                if nxt:
                    nxt.set_prev(prv)
                if prv:
                    prv.set_next(nxt)
                else:
                    self.root = this_node
                self.size -= 1
                return True  # node removed
            else:
                this_node = this_node.get_next()
        return False  # node not found

    def get_node(self, data):
        # set the first node we look at to the root node
        this_node = self.root
        # loop through the nodes
        while this_node:
            if this_node.get_data == data:
                return this_node
            elif not this_node.get_next:
                return False
            else:
                this_node = this_node.get_next


def main():
    """
    The main function invoking the other functions
    """
    my_node = Node(2, 1, 3)
    print(my_node)


#  Using the special __name__ variable we can execute the code as a script in the Terminal,
#  or import the code as a module in another python file
if __name__ == "__main__":
    main()
