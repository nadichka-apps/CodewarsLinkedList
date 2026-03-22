"""
This module provides a basic implementation of a Singly Linked List node
and a utility function to access elements by their index.
"""
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        """
        Initializes a new Node instance.
        """
        self.data = data
        self.next = next

def get_nth(node, index):
    """
    Retrieves the node at the specified index in a linked list.

    Args:
        node (Node): The head node of the list.
        index (int): The 0-based index of the node to retrieve.

    Returns:
        Node: The node located at the given index.

    Raises:
        Exception: If the node is None, the index is negative,
                   or the index is out of bounds.
    """
    if node is None or index<0:
        raise ValueError("Invalid error.")
    for _ in range(index):
        if node.next is None:
            raise ValueError("Invalid error.")
        node = node.next
    return node
