from set import Set
import unittest


class SetTest(unittest.TestCase):
    def test_init(self):
        s = Set()
        assert s.size == 0
        assert str(s) == '{}'

    def test_init_with_list(self):
        s = Set(['0', 0, '1', 1])
        assert s.size == 4
        print(s.set)

    def test_init_with_list_of_strings(self):
        s = Set()

    def test_init_with_list_of_tuples(self):
        s = Set()

    def test_iter(self):
        s = Set()

    def test_size(self):
        s = Set()

    def test_contains(self):
        s = Set([0, '1'])
        assert s.contains('1')
        assert s.contains(0)
        assert not s.contains('0')
        assert not s.contains('2')
        assert not s.contains(1)

    def test_add(self):
        s = Set()

    def test_remove(self):
        s = Set()

    def test_union(self):
        s = Set()

    def test_intersection(self):
        s = Set()

    def test_difference(self):
        s = Set()

    def test_is_subset(self):
        s = Set()

    def test_clear(self):
        s = Set()


if __name__ == '__main__':
    unittest.main()
