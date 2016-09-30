# Eliminate_duplicate.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import itertools
import random


# @include
class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        if self.first_name != other.first_name:
            return self.first_name < other.first_name
        return self.last_name < other.last_name
# @exclude

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)
# @include


def eliminate_duplicate(A):
    A.sort()  # Makes identical elements become neighbors.
    i = 0
    for i, (key, _) in enumerate(itertools.groupby(A)):
        A[i] = key
    del A[i+1:]
# @exclude


def check_ans(A):
    for i in range(1, len(A)):
        assert A[i] != A[i - 1]


def small_test():
    A = [Name('Foo', 'Bar'), Name('ABC', 'XYZ'), Name('Foo', 'Widget')]
    eliminate_duplicate(A)
    assert len(A) == 2


def main():
    small_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(0, 100000)
        A = [Name(str(random.randrange(n)), str(random.randrange(n))) for i in range(n)]
        eliminate_duplicate(A)
        check_ans(A)


if __name__ == '__main__':
    main()
