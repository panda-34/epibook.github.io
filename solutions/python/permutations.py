# permutations.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import itertools
import random


# @include
def permutations(A):
    return list(itertools.permutations(sorted(A)))


# @exclude


def small_test():
    A = [1, 2, 3]
    result = permutations(A)
    golden_result = [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (
        3, 2, 1)]
    assert result == golden_result


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10)
    A = list(range(n))
    result = permutations(A)
    print('n =', n)
    for vec in result:
        print(*vec)


if __name__ == '__main__':
    main()
