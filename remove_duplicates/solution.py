"""
Linked List Processing Module.

This module contains utilities for modifying singly linked lists,
specifically for removing redundant data.
"""

class Node(object):
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Removes duplicate nodes from a sorted singly linked list.

    The function traverses the list and skips any nodes that have
    the same data as the current node, effectively keeping only
    unique elements.

    Args:
        head (Node): The head of the sorted linked list.

    Returns:
        Node: The head of the list after duplicates have been removed.
    """
    current = head
    if head is None or head.next is None:
        return head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
