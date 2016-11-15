# Queue_with_max.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
from stack_with_max import Stack


# @include
class QueueWithMax:
    def __init__(self):
        self.__enqueue = Stack()
        self.__dequeue = Stack()

    def enqueue(self, x):
        self.__enqueue.push(x)

    def dequeue(self):
        if self.__dequeue.empty():
            while not self.__enqueue.empty():
                self.__dequeue.push(self.__enqueue.pop())
        if not self.__dequeue.empty():
            return self.__dequeue.pop()
        raise IndexError('empty queue')

    def max(self):
        if not self.__enqueue.empty():
            return self.__enqueue.max() if self.__dequeue.empty() else max(
                self.__enqueue.max(), self.__dequeue.max())
        if not self.__dequeue.empty():
            return self.__dequeue.max()
        raise IndexError('empty queue')


# @exclude


def simple_test():
    Q = QueueWithMax()
    Q.enqueue(11)
    Q.enqueue(2)
    assert 11 == Q.max()
    assert 11 == Q.dequeue()
    assert 2 == Q.max()
    assert 2 == Q.dequeue()
    Q.enqueue(3)
    assert 3 == Q.max()
    assert 3 == Q.dequeue()
    maxint = 2**64 - 1
    Q.enqueue(maxint - 1)
    Q.enqueue(maxint)
    Q.enqueue(-2)
    Q.enqueue(-1)
    Q.enqueue(-1)
    minint = -2**64
    Q.enqueue(minint)
    assert maxint == Q.max()
    assert maxint - 1 == Q.dequeue()
    assert maxint == Q.max()
    assert maxint == Q.dequeue()
    assert -1 == Q.max()
    assert -2 == Q.dequeue()
    assert -1 == Q.max()
    assert -1 == Q.dequeue()
    assert -1 == Q.dequeue()
    assert minint == Q.max()
    assert minint == Q.dequeue()
    try:
        print('Q is empty, max() call should except = ' % Q.max())
        assert False
    except IndexError as e:
        print(e)  # throw


def main():
    simple_test()
    Q = QueueWithMax()
    Q.enqueue(1)
    Q.enqueue(2)
    assert 2 == Q.max()
    assert 1 == Q.dequeue()  # 1
    assert 2 == Q.max()
    assert 2 == Q.dequeue()  # 2
    Q.enqueue(3)
    assert 3 == Q.max()
    assert 3 == Q.dequeue()  # 3
    try:
        Q.max()
        assert False
    except IndexError as e:
        print(e)  # throw
    try:
        Q.dequeue()
        assert False
    except IndexError as e:
        print(e)  # throw


if __name__ == '__main__':
    main()
