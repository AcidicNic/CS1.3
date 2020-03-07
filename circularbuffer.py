class CircularBuffer:
    def __init__(self, max_size):
        self.max = max_size
        self.size = 0
        self.list = [None] * max_size

        # index of head & tail
        self.head = None
        self.tail = None

    def __str__(self):
        """ Returns a string representation of this CircularBuffer
        Running time: O(n) depends on self.max """
        if self.is_empty():
            return "<-[]<-"
        cb_visual = []
        i = self.head - 1
        while not i == self.tail:
            i = self.increment_index_up(i)
            cb_visual.append(repr(self.list[i]))
        return f"<-[{', '.join(cb_visual)}]<-"
        # return f"{self.list}, head: {self.head}, tail: {self.tail}, size = {self.size}"

    def is_empty(self):
        """ Returns boolean indicating whether this circular buffer is empty
        Running time: O(1) """
        return self.size == 0

    def is_full(self):
        """ Returns boolean indicating whether this circular buffer is empty
        Running time: O(1) """
        return self.size == self.max

    def enqueue(self, item):
        """ insert item at the back of the buffer
        Running time: O(1) """
        if self.is_full():
            raise ValueError("Cannot enqueue to a full buffer.")
        else:
            self.tail = self.increment_index_up(self.tail)
            if self.head is None:
                self.head = self.tail
            self.list[self.tail] = item
            self.size += 1

    def front(self):
        """ return the item at the front of the buffer
        Running time: O(1) """
        if not self.is_empty():
            return self.list[self.head]
        raise ValueError("Cannot get front from an empty buffer.")

    def dequeue(self):
        """ remove and return the item at the front of the buffer
        Running time: O(1) """
        if not self.is_empty():
            item = self.list[self.head]
            # list is now empty
            if self.head == self.tail:
                self.head, self.tail = None, None
            else:
                self.head = self.increment_index_up(self.head)
            self.size -= 1
            return item
        raise ValueError("Cannot dequeue an empty buffer.")

    def increment_index_up(self, index):
        """ Helper function, returns the next index after the given index
        Running time: O(1) """
        if index is None or index == self.max-1:
            return 0
        else:
            return index + 1


if __name__ == '__main__':
    cb = CircularBuffer(4)
    abc = 'a b c d e f g h'.split()
    print(cb)
    for i in range(4):
        print(f"enqueue({abc[i]})")
        cb.enqueue(abc[i])
    print(cb)
    print(f"dequeue(): {cb.dequeue()}")
    print(cb)
    print(f"dequeue(): {cb.dequeue()}")
    print(cb)
    print(f"dequeue(): {cb.dequeue()}")
    print(cb)
    print(f"dequeue(): {cb.dequeue()}")
    print(cb)
