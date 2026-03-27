"""
Linked List Cycle Analysis Module.

This module provides tools to detect and measure cycles (loops) within
a singly linked list structure using Floyd's Cycle-Finding Algorithm.
"""

def loop_size(node):
    """
    Calculates the number of nodes in a linked list loop.

    The function uses the 'Tortoise and Hare' (Fast and Slow pointers)
    approach to first detect the existence of a cycle, and then
    traverses the cycle to count its length.

    Args:
        node (Node): Any node within a linked list that contains a loop.

    Returns:
        int: The total count of nodes that form the closed loop.

    Complexity:
        Time: O(n) - where n is the total number of nodes in the list.
        Space: O(1) - constant space as it only uses pointer references.
    """
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    count = 1
    current = slow.next
    while current != slow:
        current = current.next
        count += 1

    return count
