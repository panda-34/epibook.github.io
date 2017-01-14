# Max-sum_subarray.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import itertools


# @include
def find_maximum_subarray(A):
    min_sum = max_sum = 0
    for sum_ in itertools.accumulate(A):
        if sum_ < min_sum:
            min_sum = sum_
        if sum_ - min_sum > max_sum:
            max_sum = sum_ - min_sum
    return max_sum


# @exclude


def rand_vector(length):
    return [random.randrange(-1000, 1000) for i in range(length)]


def check_max_sum(A, max_sum):
    for i in range(len(A)):
        sum_ = 0
        for j in range(i, len(A)):
            sum_ += A[j]
            assert sum_ <= max_sum


def small_test():
    B = [1]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)
    B = [-5]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)
    B = [0]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)
    B = [0, 0]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)
    B = [0, 0, 0]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)
    B = [0, -5, 0]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)
    B = [-2, -1]
    max_sum = find_maximum_subarray(B)
    check_max_sum(B, max_sum)


def main():
    small_test()
    for times in range(1000):
        if len(sys.argv) == 1:
            A = rand_vector(random.randint(1, 10000))
        elif len(sys.argv) == 2:
            n = int(sys.argv[1])
            A = rand_vector(n)
        else:
            A = list(map(int, sys.argv[1:]))
        max_sum = find_maximum_subarray(A)
        check_max_sum(A, max_sum)


if __name__ == '__main__':
    main()
