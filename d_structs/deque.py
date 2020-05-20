import copy


class Deque:
    """An implementation of the deque data structure in python.
    
    An interface of the Deque is the same as the interface of collection.deque.
    Doubly linked list is used as the internal represantation of the deque.
    """

    class _Node:
        """A nested nonpublic class for representing a node of the list."""
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next_):
            """Create a node of the list."""
            self._element = element
            self._prev = prev
            self._next = next_

    def __init__(self, iterable=None, maxlen=None):
        """Create an empty deque."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        self._maxlen = maxlen
        if iterable is not None:
            for e in iterable:
                self.append(e)

    @property 
    def maxlen(self):
        """Return maximum size of the deque or None if unbounded."""
        return self._maxlen

    @maxlen.setter
    def maxlen(self, value):
        raise AttributeError(f"attribute 'maxlen' of {self.__class__.__name__}"
                             f" is not writable")

    @maxlen.deleter
    def maxlen(self):
        raise AttributeError(f"attribute 'maxlen' of {self.__class__.__name__}"
                             f" is not writeable")

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def _insert_between(self, e, prev, next_):
        """Insert e between two elements."""
        new = self._Node(e, prev, next_)
        prev._next = new
        next_._prev = new
        self._size += 1

    def _delete_node(self, node):
        """Delete node from the list and return its element."""
        node._prev._next = node._next
        node._next._prev = node._prev
        element = node._element
        node._element = node._prev = node._next = None
        self._size -= 1
        return element

    def append(self, e):
        """Add e to the right side of the deque."""
        if self._maxlen == 0:
            return
        if self._size == self._maxlen:
            self._delete_node(self._header._next)
        self._insert_between(e, self._trailer._prev, self._trailer)

    def appendleft(self, e):
        """Add e to the left side of the deque."""
        if self._maxlen == 0:
            return 
        if self._size == self._maxlen:
            self._delete_node(self._trailer._prev)
        self._insert_between(e, self._header, self._header._next)

    def clear(self):
        """Remove all elements from the deque."""
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __iter__(self):
        """Create a forward iterator over the elements of the deque."""
        walk = self._header._next
        while walk is not self._trailer:
            yield walk._element
            walk = walk._next

    def ___reversed___(self):
        """Return a backward  iterator over the elements of the deque."""
        walk = self._trailer._prev
        while walk is not self._header:
            yield walk._element
            walk = walk._next

    def _validate_index(self, index):
        """Check the validity of the index."""
        if type(index) != int:     # index must be integer
            raise TypeError(f"sequence index must be interger, not "
                            f"{index.__class__.__name__}")
        if index < 0:
            index = self._size + index
        if index > self._size - 1 or index < 0:
            raise IndexError(f"{self.__class__.__name__} index out of range")
        return index

    def _find_node_at_index(self, index):
        """Searches for the node at position with index index."""
        index = self._validate_index(index)
        node = self._header._next
        walk = 0
        while walk != index:
            node = node._next
            walk += 1
        return node
    
    def __getitem__(self, index):
        """Enable indexed access."""
        node = self._find_node_at_index(index)
        return node._element

    def __setitem__(self, index, value):
        """Enable assignment to self[index]."""
        node = self._find_node_at_index(index)
        node._element = value

    def __delitem__(self, index):
        """Enable deletion of self[index]."""
        node = self._find_node_at_index(index)
        self._delete_node(node)

    def pop(self):
        """Remove and return an element from the right side of the deque."""
        if self._size == 0:
            raise IndexError(f"pop from an empty {self.__class__.__name__}") 
        return self._delete_node(self._trailer._prev)

    def popleft(self):
        """Remove and return an element from the left side of the deque."""
        if self._size == 0:
            raise IndexError(f"popleft from an empty "
                             f"{self.__class__.__name__}")
        return self._delete_node(self._header._next)

    def copy(self):
        """Create a shallow copy of the deque."""
        return self.__class__(self, self._maxlen)

    def count(self, x):
        """Count the number of deque elements equal to x."""
        counter  = 0
        for e in self:
            if e == x:
                counter += 1
        return counter

    def extend(self, iterable):
        """Extend the right side of the deque with elements from iterable."""
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        """Extend the left side of the deque with elements form iterable."""
        for x in iterable:
            self.appendleft(x)

    def index(self, x, start=0, end=None):
        """Return the position of x in the deque after start and before end."""
        start = self._validate_index(start)
        if end is not None:
            end = self._validate_index(end)
        else:
            end = self._size - 1
        if start > end:
            raise ValueError(f"{x} is not in {self.__class__.__name__}")
        node = self._find_node_at_index(start)
        walk = start
        while walk < end:
            if node._element == x:
                return walk
            else:
                node = node._next
                walk += 1
        raise ValueError(f"{x} is not in {self.__class__.__name__}")

    def insert(self, i, x):
        """Insert x into the deque at position i."""
        node = self._find_node_at_index(i)
        self._insert_between(x, node._prev, node)

    def remove(self, value):
        """Remove first occurrence of the value.
   
        If not found raises a ValueError.
        """
        walk = self._header._next
        while walk is not self._trailer:
            if walk._element == value:
                self._delete_node(walk)
                return
            else:
                walk = walk._next
        raise ValueError(f"{value} is not in {self.__class__.__name__}")

    def reverse(self):
        """Reverse the elements of the deque in place."""
        if self._size > 1:
            cur = self._header
            while cur is not None:
                next_ = cur._next
                cur._prev, cur._next = cur._next, cur._prev
                cur = next_
            self._header, self._trailer = self._trailer, self._header

    def rotate(self, n=1):
        """Rotate the deque n steps to the right.

        If n is negative rotate n steps to the left.
        """
        if type(n) is not int:
            raise TypeError(f"number of rotations must be integer not "
                            f"'{n.__class__.__name__}'")
        n = n % self._size     # prevents unnecessary rotations
        if n > 0:
            first = self._header._next
            last = self._trailer._prev
            new_first = self._find_node_at_index(-n)     # new first element
            new_last = new_first._prev
            self._header._next = new_first
            new_first._prev = self._header
            first._prev = last
            last._next = first
            new_last._next = self._trailer
            self._trailer._prev = new_last
        
    def __contain__(self, x):
        """Enable membership testing with in operator."""
        for element in self:
            if element == x:
                return True
        return False

    def __add__(self, other):
        """Implement '+' operation for the deque."""
        if type(self) is not type(other):
            raise TypeError(f"can only concatenate {self.__class__.__name__}"
                            f" (not {other.__class__.__name__} to "
                            f"{self.__class__.__name__}")
        result = self.__class__(self)
        result.extend(other)
        return result

    def __radd__(self, other):
        """Implement '+' operation with reflected operands."""
        return self.__add__(other)

    def __mul__(self, number):
        """Implement '*' operation for the deque."""
        if type(number) is not int:
            raise TypeError(f"can't multiply sequence by non-int"
                            f" type {type(number)}")
        result = self.__class__()
        for _ in range(number):
            result.extend(self)
        return result

    def __rmul__(self, number):
        """Implement '*' operation with reflected operands."""
        return self.__mul__(number)

    def __imul__(self, number):
        """Implement an augmented assignment operation *=."""
        if type(number) is not int:
            raise TypeError(f"can't multiply sequence by non-int"
                            f" type {type(number)}")
        copy = self. copy()
        self.clear()
        for _ in range(number):
            self.extend(copy)
        return self

    def __copy__(self):
        """Return a shallow copy of the deque."""
        return self.copy()

    def __deepcopy__(self, memo=None):
        """Return a deep copy of the deque."""
        deepcopy = self.__class__(maxlen=self._maxlen)
        walk = self._header._next
        while walk is not self._trailer:
            element = copy.deepcopy(walk._element)
            deepcopy.append(element)
            walk = walk._next
        return deepcopy

    def __repr__(self):
        """Return a string representation of the deque."""
        l = [x for x in self]
        return f"{self.__class__.__name__}({l}, {self._maxlen})"

    

        

            
            

            

    
