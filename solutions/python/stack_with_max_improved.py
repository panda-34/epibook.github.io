# Stack_with_max_improved.cpp 98875343ac034c2bd2141da5f5c9c7e25c192d76
# @include
class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max, self.count = max, count

    def __init__(self):
        self.__element = []
        self.__cached_max_with_count = []

    def empty(self):
        return len(self.__element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self.__cached_max_with_count[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self.__element.pop()
        current_max = self.__cached_max_with_count[-1].max
        if pop_element == current_max:
            self.__cached_max_with_count[-1].count -= 1
            if self.__cached_max_with_count[-1].count == 0:
                self.__cached_max_with_count.pop()
        return pop_element

    def push(self, x):
        self.__element.append(x)
        if len(self.__cached_max_with_count) == 0:
            self.__cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self.__cached_max_with_count[-1].max
            if x == current_max:
                self.__cached_max_with_count[-1].count += 1
            elif x > current_max:
                self.__cached_max_with_count.append(self.MaxWithCount(x, 1))


# @exclude


def main():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.max() == 2
    print(s.max())  # 2
    print(s.pop())  # 2
    assert s.max() == 1
    print(s.max())  # 1
    s.push(3)
    s.push(2)
    assert s.max() == 3
    print(s.max())  # 3
    s.pop()
    assert s.max() == 3
    print(s.max())  # 3
    s.pop()
    assert s.max() == 1
    print(s.max())  # 1
    s.pop()
    try:
        s.max()
        s.pop()
        s.pop()
        s.pop()
        s.pop()
    except IndexError as e:
        print(e)


if __name__ == '__main__':
    main()
