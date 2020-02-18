#!python

from linkedlist import LinkedList
# first in last out


class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) adding an item to the top of the stack will always be just as fast."""
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.is_empty():
            return self.list.head.data
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) removing the top item will always take the same amount of time."""
        if not self.is_empty():
            popped_item = self.list.head.data
            self.list.delete(self.list.head.data)
            return popped_item
        raise ValueError('Cannot pop, stack is empty.')


class ArrayStack(object):
    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – adding an element from the end of a list is the most efficient, nothing needs to shift"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if not self.is_empty():
            return self.list[self.length() - 1]
        return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – removing an element from the end of a list is the most efficient, nothing needs to shift"""
        if not self.is_empty():
            return self.list.pop()
        raise ValueError('Cannot pop, stack is empty.')


# Stack = LinkedStack
Stack = ArrayStack
