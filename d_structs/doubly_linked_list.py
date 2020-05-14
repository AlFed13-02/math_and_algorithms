class EmptyError(Exception):
    pass


class DoublyLinkedList:
    """An implementation of the doubly linked list data structure in Python."""

    class Node:
        """Class for representing the node of the doubly linked list."""
        __slots__ = "element", "next", "prev"

        def __init__(self, element, prev, next_):
            """Creates a node of the doubly linked list."""
            self.element = element
            self.prev = prev
            self.next = next_

    def __init__(self):
        """Creates an empty list."""
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        """Returns the number of elements of the list."""
        return self._size

    def _is_empty(self):
        """Returns True if list is empty, False otherwise."""
        return self._size == 0

    @property
    def head(self):
        """Returns the first node of the list."""
        if self._is_empty():
            raise EmptyError("searching head in empty list")
        return self._header.next

    @property
    def tail(self):
        """Returns the last node of the list."""
        if self._is_empty():
            raise EmptyError("searching tail in empty list")
        return self._trailer.prev

    def _insert_between(self, element, prev, next_):
        """Inserts the element between two nodes."""
        new_node = self.Node(element, prev, next_)
        prev.next = new_node
        next_.prev = new_node
        self._size += 1

    def _delete_node(self, node):
        """Deletes the node from the list and returns the node's element."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        answer = node.element
        node.element = node.prev = node.next = None
        return answer

    def append(self, e):
        """Inserts the element at the end of the list."""
        self._insert_between(e, self._trailer.prev, self._trailer)

    def appendleft(self, e):
        """Inserts the element at the front of the list."""
        self._insert_between(e, self._header, self._header.next)

    def pop(self):
        """Removes the last element of the list and returns its value."""
        if self._is_empty():
            raise EmptyError("can't pop from empty list")
        return self._delete_node(self._trailer.prev)

    def popleft(self):
        """Removes the first element of the list and returns its value."""
        if self._is_empty():
            raise EmptyError("can't popleft from empty list")
        return self._delete_node(self._header.next)

    def __iter__(self):
        """Returns an forward iterator over the list's elements."""
        walk = self._header.next
        while walk is not self._trailer:
            yield walk.element
            walk = walk.next

    def __contains__(self, e):
        """Returns True if e in list, False otherwise."""
        for element in self:
            if element == e:
                return True
        return False

    def count(self, e):
        """Returns the number of occurences of e in the list."""
        counter = 0
        for element in self:
            if element == e:
                counter += 1
        return counter

    def clear(self):
        """Removes all elements from the list."""
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __add__(self, other):
        """Concatenates list with other list."""
        if type(self) is not type(other):
            raise TypeError(f"can only concatenate {self.__class__.__name__}"
                            f" to {self.__class__.__name__}")
        self._trailer. prev.next = other._header.next
        self._trailer = other._trailer
        return self

    __iadd__ = extend = __add__

    def copy(self):
        """Creates a shallow copy of the list."""
        new = self.__class__()
        for e in self:
            new.append(e)
        return new

    def reverse(self):
        """Reverses the list in place."""
        walk = self._header
        while walk is not None:
            next_ = walk.next
            walk.next, walk.prev = walk.prev, walk.next
            walk = next_
        self._header, self._trailer = self._trailer, self._header

    def __str__(self):
        """Return the human readable representation of the list."""
        return str([e for e in self])
