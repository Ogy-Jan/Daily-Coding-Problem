"""
Company:
    This problem was asked by Google.
Problem:
    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
    and deserialize(s), which deserializes the string back into the tree.
Examples:
    For example, given the following Node class
        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right
    The following test should pass:
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import json


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.serializedNode = dict()  # holds the serialized node as a dictionary


def serialize_node(three_node):
    """
    Serializes the three as a dictionary and saves is a an attribute of the node object
    :param three_node: node object
    :return: a serialized three as a dictionary
    """
    three_node.serializedNode["val"] = three_node.val

    if three_node.left is not None:
        three_node.serializedNode["left"] = serialize_node(three_node.left)
    else:
        three_node.serializedNode["left"] = None

    if three_node.right is not None:
        three_node.serializedNode["right"] = serialize_node(three_node.right)
    else:
        three_node.serializedNode["right"] = None

    return three_node.serializedNode


def serialize(node_serialized_dict):
    """
    Transform node from a type dict into a type string
    :param node_serialized_dict: node as a dictionary
    :return: node as a string in json format
    """
    return json.dumps(serialize_node(node_serialized_dict))


def deserialize(s):
    """
    Deserialize a node from a string back into an object of the node class
    :param s: Node in a string notation
    :return: node as an object of the Node class
    """
    node_string = json.loads(s)
    if node_string["left"] is not None and node_string["right"] is not None:
        return Node(node_string["val"], deserialize(json.dumps(node_string["left"])), deserialize(json.dumps(node_string["right"])))
    elif node_string["left"] is not None:
        return Node(node_string["val"], deserialize(json.dumps(node_string["left"])))
    elif node_string["right"] is not None:
        return Node(node_string["val"], None, deserialize(json.dumps(node_string["right"])))
    else:
        return Node(node_string["val"])


#  Using the special __name__ variable we can execute the code as a script in the Terminal,
#  or import the code as a module in another python file
if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(deserialize(serialize(node)).left.left.val == "left.left")
