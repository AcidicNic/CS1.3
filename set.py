from hashtable import HashTable
"""
TODO: Write unit tests to ensure the Set class is robust
    Include test cases for each class instance method

TODO: Annotate all instance methods with complexity analysis of running time and space (memory)

TODO: class MultiSet
"""


class Set:
    def __init__(self, elements=None):
        self.size = 0
        self.set = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """  """
        return f"{{{', '.join(self.set.keys())}}}"

    def __repr__(self):
        """  """
        return f"Set({{{', '.join(self.set.keys())}}})"

    def contains(self, element):
        return self.set.contains(element)

    def add(self, element):
        self.set.set(element, element)
        self.size += 1

    def remove(self, element):
        """ Remove the given element from this set, if present, or else raise KeyError """
        if self.contains(element):
            self.set.delete(element)
            self.size -= 1
        else:
            raise ValueError(f"{element} does not exist in the set.")

    def union(self, other_set):
        """ Return a new set that is the union of this set and other_set """
        new_set = Set()
        for element in other_set.set.keys():
            if self.contains(element):
                new_set.add(element)
        return element


    def intersection(self, other_set):
        """ return a new set that is the intersection of this set and other_set """
        pass

    def difference(self, other_set):
        """ return a new set that is the difference of this set and other_set """
        pass

    def is_subset(self, other_set):
        """ return a boolean indicating whether other_set is a subset of this set """
        pass

class MultiSet:
    pass


def test_set():
    pass


if __name__ == '__main__':
    test_set()
