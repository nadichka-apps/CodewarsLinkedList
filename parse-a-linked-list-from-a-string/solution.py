"Module for parsing a linked list from a string"
class Node():
    """
    Represents a single node in a singly linked list.
    """
    def __init__(self, data, next = None):
        """
        Initialize a new node.

        Args:
            data: The value to be stored in the node.
            next: Reference to the next node in the list (default is None).
        """
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Parses a string representation of a linked list and converts it into a Node structure.

    The function expects a string where elements are separated by " -> " and ends
    with a null-terminator (e.g., "null", "nil", "nullptr").

    Args:
        list_repr (str): The string representing the linked list.
                         Example: "1 -> 2 -> 3 -> null"

    Returns:
        Node | None: The head of the linked list or None if the input represents
                     an empty list.
    """
    if list_repr in ("null", "NULL", "nil", "nullptr"):
        return None
    part = list_repr.split(" -> ")
    head = None
    for i in part[:-1][::-1]:
        head = Node(int(i), head)
    return head
