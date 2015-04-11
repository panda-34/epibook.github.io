# Circular_queue.cpp b4b3a70d8ab942579f85b4416f980d05831af969
# @include
class Queue:
    __k_scale_factor = 2

    def __init__(self, cap):
        self.__data = [None] * cap
        self.__head = 0
        self.__tail = 0
        self.__num_queue_elements = 0

    def enqueue(self, x):
        if self.__num_queue_elements == len(self.__data):  # Needs to resize.
            # Makes the queue elements appear consecutively.
            tmp = self.__data[:self.__head]
            del self.__data[:self.__head]
            self.__data += tmp
            # Resets head and tail.
            self.__head = 0
            self.__tail = self.__num_queue_elements
            self.__data += [None] * (len(self.__data) * (self.__k_scale_factor - 1))

        self.__data[self.__tail] = x
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__num_queue_elements += 1

    def dequeue(self):
        if not self.__num_queue_elements:
            raise IndexError('empty queue')
        self.__num_queue_elements -= 1
        ret = self.__data[self.__head]
        self.__head = (self.__head + 1) % len(self.__data)
        return ret

    def size(self):
        return self.__num_queue_elements
# @exclude

def test():
    q = Queue(8)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    # Now head = 0 tail = 0

    assert 1 == q.dequeue()
    assert 2 == q.dequeue()
    assert 3 == q.dequeue()
    # head = 3 and tail = 0

    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    # Ok till here. Now head = 3 and tail = 3

    q.enqueue(14)  # now the vector (data) is resized; but the head and tail.
                   # (or elements) does not change accordingly.
    q.enqueue(15)
    q.enqueue(16)
    q.enqueue(17)
    q.enqueue(18)
    # The elements starting from head=3 are overwritten!

    assert 4 == q.dequeue()
    assert 5 == q.dequeue()
    assert 6 == q.dequeue()
    assert 7 == q.dequeue()
    assert 8 == q.dequeue()
    assert 11 == q.dequeue()
    assert 12 == q.dequeue()


def main():
    test()
    q = Queue(8)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert 1 == q.dequeue()
    q.enqueue(4)
    assert 2 == q.dequeue()
    assert 3 == q.dequeue()
    assert 4 == q.dequeue()
    try:
        q.dequeue()
    except IndexError as e:
        print(e)
    # test resize().
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    q.enqueue(4)
    assert q.size() == 9


if __name__ == '__main__':
    main()
