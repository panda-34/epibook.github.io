# Queue_with_max.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
from stack_with_max import Stack


# @include
class Queue:

    def __init__(self):
        self.__A = Stack()
        self.__B = Stack()

    def enqueue(self, x):
        self.__A.push(x)

    def dequeue(self):
        if self.__B.empty():
            while not self.__A.empty():
                self.__B.push(self.__A.pop())
        if not self.__B.empty():
            return self.__B.pop()
        raise IndexError('empty queue')

    def max(self):
        if not self.__A.empty():
            return self.__A.max() if self.__B.empty() else max(
                self.__A.max(), self.__B.max())
        else:  # __A.empty() == True.
            if not self.__B.empty():
                return self.__B.max()
            raise IndexError('empty queue')
# @exclude


def main():
    Q = Queue()
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
    except IndexError as e:
        print(e)  # throw
    try:
        Q.dequeue()
    except IndexError as e:
        print(e)  # throw


if __name__ == '__main__':
    main()
