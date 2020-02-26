from hashtable import HashTable
"""
TODO: Write unit tests to ensure the Set class is robust
    Include test cases for each class instance method

TODO: Annotate all instance methods with complexity analysis of running time and space (memory)
"""


class Set:
    def __init__(self, elements=None):
        self.size = 0
        self.set = HashTable()

        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """ Returns a string representation of this Set """
        return f"{{{', '.join(self.set.keys())}}}"

    def __iter__(self):
        """ Allows you to iterate through this Set """
        for element in self.set.keys():
            yield element

    def contains(self, element):
        """ Returns a boolean indicating whether element is in this Set
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        return self.set.contains(element)

    def add(self, element):
        """ Adds element to this set
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        self.set.set(element, element)
        self.size += 1

    def remove(self, element):
        """ Remove element from this Set, if present, or else raise KeyError
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        if self.contains(element):
            self.set.delete(element)
            self.size -= 1
        else:
            raise ValueError(f"{element} does not exist in the set.")

    def union(self, other_set):
        """ Returns a new set that is the union of this Set and other_set
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        new_set = Set()
        for element in other_set.set.keys()+self.set.keys():
            if not new_set.contains(element):
                new_set.add(element)
                new_set.size += 1
        return new_set

    def intersection(self, other_set):
        """ Returns a new set that is the intersection of this Set and other_set
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        new_set = Set()
        for element in other_set:
            if self.contains(element):
                new_set.add(element)
                new_set.size += 1
        return new_set

    def difference(self, other_set):
        """ Returns a new set that is the difference of this Set and other_set
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        new_set = Set()
        for element in other_set.set.keys()+self.set.keys():
            if not self.contains(element) or not other_set.contains(element):
                new_set.add(element)
                new_set.size += 1
        return new_set

    def is_subset(self, other_set):
        """ Returns a boolean indicating whether other_set is a subset of this Set
            Time Complexity: O(?)
            Space Complexity: O(?)
            """
        for element in other_set:
            if not self.contains(element):
                return False
        return True

    def clear(self):
        """ Removes all elements from this Set
            Time Complexity: O(1) just assigning vars
            Space Complexity: O(1) just assigning vars
            """
        self.set = HashTable()
        self.size = 0


def test_set():
    # is_subset() Test
    s1 = Set('Hello')
    subset_tests = [Set('olle'), Set('olje'), Set('Hello'), Set('hello'), Set('Hellos'), Set('Heos'), Set('4s'), Set('l'), Set('ooooo'), Set()]
    for sub in subset_tests:
        print(f"{s1}.is_subset({sub}) -> {s1.is_subset(sub)}")

    print()
    # difference() Test
    s1 = Set('Hello')
    diff_tests = [Set('ol8kcle'), Set('olje'), Set('Hello'), Set('hello'), Set('Hellos'), Set('Heos'), Set('4s'), Set('l'), Set('ooooo'), Set('75hellobt56dh6dn'), Set()]
    for set in diff_tests:
        print(f"{s1}.difference({set}) -> {s1.difference(set)}")

    print()
    # intersection() Test
    s1 = Set('Hello')
    intersection_tests = [Set('ol8kcle'), Set('olje'), Set('Hello'), Set('hello'), Set('Hellos'), Set('Heos'), Set('4s'), Set('l'), Set('ooooo'), Set('75hellobt56dh6dn'), Set()]
    for set in intersection_tests:
        print(f"{s1}.intersection({set}) -> {s1.intersection(set)}")

    print()
    # union() Test
    s1 = Set('Hello')
    union_tests = [Set('ol8kcle'), Set('olje'), Set('Hello'), Set('hello'), Set('Hellos'), Set('Heos'), Set('4s'), Set('l'), Set('ooooo'), Set('75hellobt56dh6dn'), Set()]
    for set in union_tests:
        print(f"{s1}.union({set}) -> {s1.union(set)}")

    print()
    # __iter__() Test
    s1 = Set('hey, whats up?!')
    elements = []
    for element in s1:
        elements.append(element)
    print(elements)


if __name__ == '__main__':
    test_set()
