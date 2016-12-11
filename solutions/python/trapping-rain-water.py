# trapping-rain-water.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import collections


# @include
def calculate_trapping_water(A):
    if not A:
        return 0

    # Finds the index with maximum height.
    max_h = A.index(max(A))

    # Calculates the water within [1 : max_h - 1].
    partial_sum = 0
    left = A[0]
    for i in range(1, max_h):
        if A[i] >= left:
            left = A[i]
        else:
            partial_sum += left - A[i]

    # Calculates the water within [max_h + 1 : len(A) - 2].
    right = A[-1]
    for i in range(len(A) - 2, max_h, -1):
        if A[i] >= right:
            right = A[i]
        else:
            partial_sum += right - A[i]
    return partial_sum


# @exclude

# Stack approach, O(n) time, O(n) space
HeightBound = collections.namedtuple('HeightBound',
                                     ('left_bound', 'right_bound'))


def check_answer(A):
    s = []
    sum_ = 0
    for i, a in enumerate(A):
        while s and s[-1].right_bound <= a:
            bottom = s[-1].right_bound
            del s[-1]
            if not s:
                break
            top = min(s[-1].right_bound, a)
            sum_ += (top - bottom) * (i - s[-1].left_bound - 1)
        s.append(HeightBound(i, a))
    return sum_


def small_test():
    A = (1, 0, 3, 2, 5, 0, 1)
    assert calculate_trapping_water(A) == 3
    A = (1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1)
    assert calculate_trapping_water(A) == 18


def main():
    small_test()
    for times in range(10000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 1000)
        A = [random.randint(0, 10) for i in range(n)]
        print(*A)
        print(check_answer(A), calculate_trapping_water(A))
        assert check_answer(A) == calculate_trapping_water(A)


if __name__ == '__main__':
    main()
