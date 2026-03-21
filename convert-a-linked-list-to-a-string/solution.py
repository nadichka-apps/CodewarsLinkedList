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

def stringify(node):
    """
        Converts a linked list into a human-readable string format.

        Args:
            node (Node): The head node of the linked list.

        Returns:
            str: A string representation of the list in the format 'data -> data -> None'.
        """
    if node is None:
        return "None"
    current = node
    result = ""
    while current:
        result += str(current.data) + ' -> '
        current = current.next
    result += 'None'
    return result

# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node2.next = node3

# print("Список:")
# print(stringify(node1))

# print("Порожній список:")
# print(stringify(None))
