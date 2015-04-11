# Queue_from_stacks.cpp b4b3a70d8ab942579f85b4416f980d05831af969
# @include
class Queue:

    def __init__(self):
        self.__A = []
        self.__B = []

    def enqueue(self, x):
        self.__A.append(x)

    def dequeue(self):
        if not self.__B:
            # Transfers the elements in __A to __B.
            while self.__A:
                self.__B.append(self.__A.pop())

        if not self.__B:  # __B is still empty!
            raise IndexError('empty queue')
        return self.__B.pop()
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
    except IndexError as e:
        print(e)  # throw


if __name__ == '__main__':
    main()
