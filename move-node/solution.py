"""Module."""
class Node(object):
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """A helper class to return the updated heads of two lists."""
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Takes the node from the front of the source list and moves it
    to the front of the dest list.

    Args:
        source (Node|None): The head of the source linked list.
        dest (Node|None): The head of the destination linked list.

    Returns:
        Context: An object containing the new heads of both lists
                 (source.next and the moved node).

    Raises:
        ValueError: If the source list is empty (None).
    """
    if source is None:
        raise ValueError("Source list is empty.")
    new_node = source
    source = source.next

    new_node.next = dest
    dest = new_node

    return Context(source, dest)
