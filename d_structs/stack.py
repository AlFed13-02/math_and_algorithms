from singly_linked_list import SinglyLinkedList, EmptyError


class Stack:
    """An implementation of the stack data type in Python."""

    def __init__(self):
        """Creates an empty stack."""
        self._data = SinglyLinkedList()

    def __len__(self):
        """Returns the number of elements of the stack."""
        return len(self._data)

    def push(self, e):
        """Add e at the top of the stack."""
        self._data.appendleft(e)

    def pop(self):
        """Removes and returns the topmost element of the stack."""
        if len(self) == 0:
            raise EmptyError("pop from empty stack")
        return self._data.popleft()

    @property
    def top(self):
        """Returns the topmost element of the stack."""
        return self._data.head.element

