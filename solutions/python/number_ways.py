# Number_ways.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import itertools


# @include
def number_of_ways(n, m):
    return compute_number_of_ways_to_xy(n - 1, m - 1,
                                        [[0] * m for _ in range(n)])


def compute_number_of_ways_to_xy(x, y, number_of_ways):
    if x == y == 0:
        return 1

    if number_of_ways[x][y] == 0:
        ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(
            x - 1, y, number_of_ways)
        ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(
            x, y - 1, number_of_ways)
        number_of_ways[x][y] = ways_top + ways_left
    return number_of_ways[x][y]


# @exclude


def compute_number_of_ways_space_efficient(n, m):
    if n < m:
        n, m = m, n

    A = [1] * m
    for i in range(1, n):
        prev_res = 0
        for j in range(m):
            A[j] += prev_res
            prev_res = A[j]
    return A[m - 1]


# Pythonic solution
def number_of_ways_pythonic(n, m):
    if n < m:
        n, m = m, n

    A = [1] * m
    for i in range(1, n):
        A = list(itertools.accumulate(A))
    return A[-1]


def check_ans(n, k):
    table = [[0] * (k + 1) for _ in range(n + 1)]
    # Basic case: C(i, 0) = 1.
    for i in range(n + 1):
        table[i][0] = 1
    # Basic case: C(i, i) = 1.
    for i in range(1, k + 1):
        table[i][i] = 1
    # C(i, j) = C(i - 1, j) + C(i - 1, j - 1).
    for i in range(2, n + 1):
        for j in range(1, min(i, k + 1)):
            table[i][j] = table[i - 1][j] + table[i - 1][j - 1]
    return table[n][k]


def main():
    for _ in range(1000):
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        else:
            n = random.randint(1, 10)
            m = random.randint(1, 10)
        print('n =', n, ', m =', m, ', ways =', number_of_ways(n, m))
        assert check_ans(n + m - 2,
                         m - 1) == compute_number_of_ways_space_efficient(
                             n, m) == number_of_ways_pythonic(n, m)
        if len(sys.argv) == 3:
            break


if __name__ == '__main__':
    main()
