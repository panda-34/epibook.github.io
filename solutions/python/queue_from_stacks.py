# Queue_from_stacks.cpp b4b3a70d8ab942579f85b4416f980d05831af969
# @include
class Queue:
    def __init__(self):
        self.__enq = []
        self.__deq = []

    def enqueue(self, x):
        self.__enq.append(x)

    def dequeue(self):
        if not self.__deq:
            # Transfers the elements in __enq to __deq.
            while self.__enq:
                self.__deq.append(self.__enq.pop())

        if not self.__deq:  # __deq is still empty!
            raise IndexError('empty queue')
        return self.__deq.pop()


# @exclude


def main():
    Q = Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    assert 1 == Q.dequeue()  # 1
    assert 2 == Q.dequeue()  # 2
    Q.enqueue(3)
    assert 3 == Q.dequeue()  # 3
    try:
        Q.dequeue()
        assert False
    except IndexError as e:
        print(e)  # throw
    Q.enqueue(-1)
    Q.enqueue(123)
    Q.enqueue(2**64 - 1)
    Q.enqueue(-2**64)
    Q.enqueue(0)
    assert -1 == Q.dequeue()
    Q.enqueue(0)
    assert 123 == Q.dequeue()
    assert 2**64 - 1 == Q.dequeue()
    assert -2**64 == Q.dequeue()
    assert 0 == Q.dequeue()
    assert 0 == Q.dequeue()
    try:
        Q.dequeue()
        assert False
    except IndexError as e:
        print(e)  # throw


if __name__ == '__main__':
    main()
