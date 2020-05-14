from doubly_linked_list import DoublyLinkedList, EmptyError


class Queue:
    """An implementation of the queue data structure.

    This implementation uses a doubly linked list as the inner storage 
    for elements of the list.
    """

    def __init__(self):
        """Creates an empty queue."""
        self._data = DoublyLinkedList()

    def __len__(self):
        """Returns the number of elements of the queue."""
        return len(self._data)

    def enqueue(self, e):
        """Inserts the element at the end of the queueu."""
        self._data.append(e)

    def dequeue(self):
        """Removes and returns the first element of the queue."""
        if len(self) == 0:
            raise EmptyError("dequeuing from empty queue")
        return self._data.popleft()

    @property
    def front(self):
        """Returns the first element of the queue."""
        if len(self) == 0:
            raise EmptyError("searchig for front in empty queue")
        return self._data.head.element
