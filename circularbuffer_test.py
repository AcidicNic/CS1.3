import unittest
from circularbuffer import CircularBuffer


class SetTest(unittest.TestCase):

    def test_init(self):
        cb = CircularBuffer(2)
        assert cb.size == 0
        assert cb.max == 2
        assert cb.list == [None, None]
        assert cb.head is None
        assert cb.tail is None

    def test_properties(self):
        cb = CircularBuffer(4)
        cb.enqueue('a')
        assert cb.size == 1
        assert cb.list == ['a', None, None, None]
        cb.enqueue('b')
        assert cb.size == 2
        assert cb.list == ['a', 'b', None, None]
        cb.enqueue('c')
        assert cb.size == 3
        assert cb.list == ['a', 'b', 'c', None]
        cb.enqueue('d')
        assert cb.size == 4
        assert cb.list == ['a', 'b', 'c', 'd']


    def test_is_empty(self):
        cb = CircularBuffer(2)
        assert cb.is_empty()
        cb.enqueue('test')
        assert not cb.is_empty()
        cb.dequeue()
        assert cb.is_empty()

    def test_is_full(self):
        cb = CircularBuffer(3)
        assert not cb.is_full()
        cb.enqueue('test')
        assert not cb.is_full()
        cb.enqueue('other test')
        assert not cb.is_full()
        cb.enqueue(12345)
        assert cb.is_full()
        cb.dequeue()
        assert not cb.is_full()

    def test_enqueue_and_dequeue(self):
        abcd = ['a', 'b', 'c', 'd']
        cb = CircularBuffer(4)
        for i in range(4):
            cb.enqueue(abcd[i])
            assert cb.size == i + 1
        for i in range(3, 0):
            cb.dequeue()
            assert cb.size == i + 1

    def test_front(self):
        abcd = ['a', 1, ['dsf', 5, '324'], {'d': 1002}]
        cb = CircularBuffer(4)
        for i in range(4):
            cb.enqueue(abcd[i])
            assert cb.size == i + 1
        assert cb.front() == 'a'
        cb.dequeue()
        assert cb.front() == 1
        cb.dequeue()
        assert cb.front() == ['dsf', 5, '324']
        cb.dequeue()
        assert cb.front() == {'d': 1002}
        cb.dequeue()



if __name__ == '__main__':
    unittest.main()
