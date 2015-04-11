# Queue_with_max_using_deque.h 848813e190b1b85a8e75107fe8513c3be38ad1a9
# Queue_with_max_using_deque.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import collections


# @include
class Queue:

    def __init__(self):
        self.__Q = collections.deque()
        self.__D = collections.deque()

    def enqueue(self, x):
        self.__Q.append(x)
        while self.__D and self.__D[-1] < x:
            self.__D.pop()
        self.__D.append(x)

    def dequeue(self):
        if self.__Q:
            ret = self.__Q.popleft()
            if ret == self.__D[0]:
                self.__D.popleft()
            return ret
        raise IndexError('empty queue')

    def max(self):
        if self.__D:
            return self.__D[0]
        raise IndexError('empty queue')
# @exclude

    def head(self):
        return self.__Q[0]


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
