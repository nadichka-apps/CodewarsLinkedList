"""
Linked List Reversal Module.

This module provides a recursive implementation for reversing
a singly linked list by manipulating node pointers.
"""

class Node(object):
    """Represents a node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Reverses a singly linked list using recursion.

    This function traverses to the end of the list and reorients the
    next pointers as the recursion unwinds, effectively flipping
    the list direction.

    Args:
        head (Node): The head node of the list to be reversed.

    Returns:
        Node: The new head of the reversed list (the former tail).
    """
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)

    head.next.next = head
    head.next = None

    return new_head
