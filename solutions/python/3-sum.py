# 3-sum.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import itertools
import sys
import random
from two_sum import has_two_sum


# @include
def has_three_sum(A, t):
    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)


# @exclude


# n^3 solution.
def check_ans(A, t):
    return any(i + j + k == t for i, j, k in itertools.combinations(A, 3))


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        T = random.randrange(n)

        A = [random.randint(-100000, 100000) for i in range(n)]

        print(has_three_sum(A, T))
        assert check_ans(A, T) == has_three_sum(A, T)


if __name__ == '__main__':
    main()
