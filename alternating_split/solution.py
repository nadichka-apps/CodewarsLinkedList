"""
Linked List Partitioning Module.

This module provides tools for splitting a singly linked list into
two separate lists by alternating their nodes.
"""

class Node(object):
    """Represents a node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """A container for the two resulting lists after an alternating split."""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Splits a linked list into two separate lists by alternating nodes.

    The first list will contain nodes 1, 3, 5, etc., and the second list
    will contain nodes 2, 4, 6, etc. The function rearranges existing
    nodes rather than creating new ones.

    Args:
        head (Node): The head of the source linked list.

    Returns:
        Context: An object containing the heads of the two new lists
                 (first and second).

    Raises:
        ValueError: If the input list has fewer than two nodes.
    """
    if head is None or head.next is None:
        raise ValueError('Too short')

    first_head = head
    second_head = head.next

    first_tail = first_head
    second_tail = second_head

    current = head.next.next
    is_first = True

    while current:
        if is_first:
            first_tail.next = current
            first_tail = current
        else:
            second_tail.next = current
            second_tail = current

        current = current.next
        is_first = not is_first

    first_tail.next = None
    second_tail.next = None

    return Context(first_head, second_head)
