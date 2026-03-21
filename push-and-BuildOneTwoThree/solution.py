"""Linked lists."""
class Node:
    def __init__(self, data):
        """
        A class to represent a node in a singly linked list.

        Attributes:
            data: The value stored in the node.
            next: Pointer to the next node in the list (defaults to None).
        """
        self.data = data
        self.next = None

def push(head, data):
    """
    Inserts a new node at the beginning of the linked list.

    Args:
        head (Node): The current head of the linked list.
        data: The value to be added to the new node.

    Returns:
        Node: The new head of the linked list.
    """
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """
    Builds a linked list with three nodes containing values 1, 2, and 3.

    The nodes are pushed in reverse order (3, then 2, then 1) so that
    the resulting list structure is: 1 -> 2 -> 3 -> None.

    Returns:
        Node: The head node of the constructed list.
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
