class EmptyError(Exception):
    pass

class SinglyLinkedList:
    """ An implementation of a singly linked list in Python."""

    class Node:
        """Class for representing a node of a singly linked list."""
        __slots__ = "element", "next"

        def __init__(self, element, next_):
            """Creates a new node."""
            self.element = element
            self.next = next_

    def __init__(self):
        """Creates an empty list."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Returns the number of elements in the list."""
        return self._size

    def _is_empty(self):
        """Returns True if list is empty."""
        return self._size == 0

    @property
    def head(self):
        """Returns the first node of the list."""
        if self._is_empty():
            raise EmptyError("searching head in empty list")
        return self._head
    
    @property
    def tail(self):
        """Returns the last node of the list."""
        if self._is_empty():
            raise EmptyError("searching tail in empty list")
        tail = self._head
        while tail.next != None:
            tail = tail.next
        return tail

    def append(self, e):
        """Inserts the element at the end of the list."""
        new_node = self.Node(e, None)
        if self._is_empty():
            self._head = new_node
        else:
            self.tail.next = new_node
        self._size += 1

    def appendleft(self, e):
        """Inserts the element at the front of the list."""
        new_node = self.Node(e, None)
        if not self._is_empty():
            new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self):
        """Removes and returns the last element of the list."""
        if self._is_empty():
            raise EmptyError("pop from empty list")
        if len(self) == 1:
            answer = self._head.element
            self._head = None
        else:
            second_to_last = self._head
            while second_to_last.next.next != None:
                second_to_last = second_to_last.next
            answer = second_to_last.next.element
            second_to_last.next = None
        self._size -= 1
        return answer

    def popleft(self):
        """Removes and returns the first element of the list."""
        if self._is_empty():
            raise EmptyError("popleft from empty list")
        answer = self._head.element
        self._head = self._head.next
        self._size -=1
        return answer

    def __iter__(self):
        """Returns the forward iterator for the elements of the list."""
        cursor = self._head
        while cursor is not None:
            yield cursor.element
            cursor = cursor.next

    def __contains__(self, e):
        """Returns True if e is an element of the list."""
        for element in self:
            if element == e:
                return True
        return False

    def count(self, e):
        """Count the number of occurrences of e in the list."""
        total = 0
        for x in self:
            if x == e:
                total += 1
        return total

    def clear(self):
        """Removes all elements from the list."""
        self._head = None
        self._size = 0

    def __add__(self, other):
        """Concatanates self and other."""
        if not (type(self) is type(other)):
            raise TypeError("can only concatanate SinglyLinkedList"
                            " to SinglyLinkedList")
        if self._is_empty():
            self._head = other._head
        else:
            self.tail.next = other._head
        return self

    __iadd__ = __add__
    extend = __add__

    def copy(self):
        """Create a shallow copy of the list."""
        new = self.__class__()
        new._size = self._size
        if not self._is_empty():
            new._head = self.Node(self._head.element, None)
            walk = self._head.next
            prev = new._head
            while walk is not None:
                next_ = self.Node(walk.element, None)
                prev.next = next_
                prev = next_
                walk = walk.next
        return new
            
    def reverse(self):
        """Reverse the items of the list in place."""
        if len(self) > 1:
            prev = self._head
            cur = prev.next
            prev.next = None
            while cur.next is not None:
                next_ = cur.next
                cur.next = prev
                prev = cur
                cur = next_
            self._head = cur
            self._head.next = prev

    def __str__(self):
        """Returns an informal string represantation of the list."""
        answer = "[" + ",".join([str(x) for x in self]) + "]"
        return answer

