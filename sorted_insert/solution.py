"""
Singly Linked List Utility Module.

This module provides tools for manipulating nodes in a linked list,
specifically focusing on maintaining order during insertion operations.
"""

class Node(object):
    """Represents a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    """
    Inserts a new node into a sorted singly linked list.

    The function traverses the list to find the appropriate position for
    the new data to ensure the list remains in ascending order.

    Args:
        head (Node): The head node of the linked list.
        data (int/any): The value to be inserted into the list.

    Returns:
        Node: The head of the list (may be the new node if inserted at the start).
    """
    new_node = Node(data)
    current = head

    if head is None or data < head.data:
        new_node.next = head
        return new_node

    while current.next is not None and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head
