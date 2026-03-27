"""
Linked List Node Manipulation Module.

This module provides functions to reorder nodes within a singly
linked list, specifically focusing on pairwise swapping.
"""

class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    """
    Swaps every two adjacent nodes in a singly linked list.

    This function uses a dummy node (fake_head) to handle cases where
    the head of the list changes. It rearranges the pointers of
    neighboring nodes to swap their positions without modifying
    the data inside the nodes.

    Args:
        head (Node): The head of the linked list.

    Returns:
        Node: The new head of the list after all adjacent pairs
              have been swapped.
    """
    fake_head = Node(head)
    prev = fake_head

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return fake_head.next
